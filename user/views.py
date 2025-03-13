from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model
from user.forms import LoginForm, RegisterForm, UserProfileForm
from django.contrib.auth.decorators import login_required

User = get_user_model()

from django.views.decorators.csrf import csrf_exempt
from social_django.views import complete

@csrf_exempt  
def google_auth_complete(request, *args, **kwargs):
    return complete(request, *args, **kwargs)


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "user/register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"]) 
            user.save()
            login(request, user)  
            messages.success(request, "Registration successful!")
            return redirect("home:home")
        
        messages.error(request, "Registration failed. Please correct the errors.")
        return render(request, "user/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data["username_or_email"] 
            password = form.cleaned_data["password"]

            
            try:
                user = User.objects.get(username=username_or_email)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email=username_or_email)
                except User.DoesNotExist:
                    user = None

            if user:
                authenticated_user = authenticate(request, username=user.username, password=password)
                if authenticated_user is not None:
                    login(request, authenticated_user)
                    messages.success(request, "Login successful!")
                    return redirect("home:home")
            
            messages.error(request, "Invalid username, email, or password.")

    else:
        form = LoginForm()

    return render(request, "user/login.html", {"form": form})


@login_required
def profile_view(request):
    user = request.user
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect("user:profile")
    else:
        form = UserProfileForm(instance=user)

    return render(request, "user/profil.html", {"form": form, "profile_user": user})
