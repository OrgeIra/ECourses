from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username or not password:  # Проверяем, что оба значения есть
            return None

        try:
            # Проверяем, это email или username
            if "@" in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        # Проверяем пароль
        if user.check_password(password):
            return user
        return None
