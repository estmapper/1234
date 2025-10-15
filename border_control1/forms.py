from django import forms


class BorderControl1Form(forms.Form):
    float_bin = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    float_oct = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    float_hex = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    int_bin = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "10"}),
    )
    int_oct = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    int_hex = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    int_sec_bin = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "10"}),
    )
    int_sec_p = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    int_trd = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "3"}),
    )
    int_trd_p = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    int_fth = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "3"}),
    )
    int_fth_bin = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )