from django.shortcuts import render
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home:home')  
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
