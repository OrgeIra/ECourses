from django.shortcuts import render, get_object_or_404
from .models import Course, Teacher

def index(request):
    courses = Course.objects.all()
    return render(request, 'home/index.html', {'courses': courses})

def courses(request,):
    courses = Course.objects.all()
    return render(request, 'home/course.html',  {'courses': courses})

def about(request):
    return render(request, 'home/about.html')

def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'home/teacher.html', {'teachers': teachers})

def contact(request):
    return render(request, 'home/contact.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


