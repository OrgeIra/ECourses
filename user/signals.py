# user/signals.py
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.core.mail import mail_admins
from django.utils.timezone import now
import os

from django.conf import settings
from .models import User


# 1. Создание профиля при регистрации пользователя
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(f"Created new user: {instance.username}")
        # Здесь можно добавить логику создания профиля, если он отдельный


# 2. Удаление файлов профиля при удалении пользователя
@receiver(post_delete, sender=User)
def delete_user_files(sender, instance, **kwargs):
    if instance.profile_image:
        image_path = os.path.join(settings.MEDIA_ROOT, str(instance.profile_image))
        if os.path.isfile(image_path):
            os.remove(image_path)
            print(f"Profile image deleted: {image_path}")


# 3. Обновление даты последнего изменения профиля
@receiver(pre_save, sender=User)
def update_last_modified(sender, instance, **kwargs):
    if instance.pk:  # Проверяем, что объект уже существует
        instance.updated_at = now()


# 4. Уведомление админа при создании нового пользователя
@receiver(post_save, sender=User)
def notify_admins_on_new_user(sender, instance, created, **kwargs):
    if created:
        mail_admins(
            subject="New user registred",
            message=f"User {instance.username} ({instance.email}) registred in platform."
        )
