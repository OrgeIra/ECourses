from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role="student", **extra_fields):
        """
        Создаёт обычного пользователя (по умолчанию — студент).
        """
        if not email:
            raise ValueError("Users must have an email address")

        extra_fields.setdefault("is_active", True) 
        user = self.model(email=self.normalize_email(email), role=role, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_teacher(self, email, password=None, **extra_fields):
        """
        Создаёт учителя (по сути, то же самое, но с role='teacher').
        """
        extra_fields.setdefault("role", "teacher")
        return self.create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Создаёт суперюзера (администратора).
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, role="teacher", **extra_fields)
