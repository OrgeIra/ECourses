from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Teacher
from django.contrib import messages
from .forms import ContactForm
from django.db.models import Sum, Avg, Max, Min, Count

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

def course_detail(request, pk):
    course = get_object_or_404(Course, id=pk)
    return render(request, 'home/course_detail.html', {'course': course})





def learn_more(request):
    stats = Course.objects.aggregate(
        total_students=Sum('students_count'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )

    teachers = Teacher.objects.annotate(course_count=Count('course'))

    context = {
        'stats': stats,
        'teachers': teachers
    }
    return render(request, 'home/learn_more.html', context)
