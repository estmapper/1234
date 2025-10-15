from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Group
from django.utils.text import slugify
from django.db.models import Q


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "placeholder": "login"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"type": "password", "placeholder": "password"}
        ),
    )


class RegistrationForm(forms.Form):
    last_name = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)
    custom_group = forms.CharField(max_length=100, required=False)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned = super().clean()
        g = cleaned.get("group")
        cg = cleaned.get("custom_group")
        if not g and not cg:
            self.add_error("custom_group", "Укажите группу или введите свою")
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")
        if p1 and p2 and p1 != p2:
            self.add_error("password2", "Пароли не совпадают")
        return cleaned

    def _transliterate(self, text: str) -> str:
        mapping = {
            "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e",
            "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
            "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
            "ф": "f", "х": "h", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "sch", "ъ": "",
            "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
        }
        s = text.strip().lower()
        res = []
        for ch in s:
            res.append(mapping.get(ch, ch))
        return "".join(res)

    def _generate_username(self, last_name: str, first_name: str) -> str:
        base = f"{self._transliterate(last_name)}_{self._transliterate(first_name)}"
        base = slugify(base).replace("-", "_")
        if not base:
            base = "user"
        username = base
        i = 1
        while CustomUser.objects.filter(username=username).exists():
            i += 1
            username = f"{base}_{i}"
        return username

    def save(self):
        last_name = self.cleaned_data["last_name"]
        first_name = self.cleaned_data["first_name"]
        password = self.cleaned_data["password1"]
        grp = self.cleaned_data.get("group")
        custom_group = self.cleaned_data.get("custom_group")
        if not grp and custom_group:
            grp, _ = Group.objects.get_or_create(name=custom_group)
        username = self._generate_username(last_name, first_name)
        user = CustomUser(
            username=username,
            first_name=first_name,
            last_name=last_name,
            role=1,
            group=grp,
        )
        user.set_password(password)
        user.save()
        return user
