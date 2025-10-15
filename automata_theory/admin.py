from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, KRTime, Group


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "role",
        "group",
    )
    list_filter = ("is_staff", "is_superuser", "role", "group")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Персональная информация",
            {"fields": ("first_name", "last_name", "email", "role", "group")},
        ),
        (
            "Разрешения",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "role", "group"),
            },
        ),
    )
    search_fields = ("username", "first_name", "last_name", "email")
    autocomplete_fields = ("group",)
    ordering = ("username",)


@admin.register(KRTime)
class KRTimeAdmin(admin.ModelAdmin):
    list_display = (
        "kr_number",
        "duration",
        "is_active",
        "created_at",
        "updated_at",
    )
    list_filter = ("kr_number", "is_active")
    search_fields = ("kr_number",)
    ordering = ("kr_number",)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
