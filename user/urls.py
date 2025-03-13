from django.urls import path
from user import views


app_name = 'user'

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("social-auth/complete/google-oauth2/", views.google_auth_complete, name="google_complete"),
    path("profile/", views.profile_view, name="profile"),
]
