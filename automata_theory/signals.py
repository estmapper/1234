from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import CustomUser


@receiver(user_logged_in)
def update_user_group(sender, request, user, **kwargs):
    # Поведение обновления группы больше не требуется: поле group теперь FK на Group
    if isinstance(user, CustomUser):
        return None
