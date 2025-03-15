from django import forms
from user.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class LoginForm(forms.Form):
    username_or_email = forms.CharField(
        label="Username or Email",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 bg-yellow-200 rounded-lg focus:outline-none',
            'placeholder': 'Enter your username or email'
        })
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-3 bg-transparent focus:outline-none',
            'placeholder': 'Enter your password'
        })
    )


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-3 bg-yellow-200 rounded-lg focus:outline-none',
            'placeholder': 'Enter your password'
        })
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-3 bg-yellow-200 rounded-lg focus:outline-none',
            'placeholder': 'Confirm your password'
        })
    )

    class Meta:
        model = User
        fields = ["email", "username", "password"]  
        widgets = {
            "email": forms.EmailInput(attrs={
                'class': 'w-full p-3 bg-yellow-200 rounded-lg focus:outline-none',
                'placeholder': 'Enter your email'
            }),
            "username": forms.TextInput(attrs={  # добавил username, чтобы было консистентно
                'class': 'w-full p-3 bg-yellow-200 rounded-lg focus:outline-none',
                'placeholder': 'Enter your username'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already in use.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'profile_image', 'bio']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'role': forms.Select(attrs={'class': 'form-control'}), 
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
