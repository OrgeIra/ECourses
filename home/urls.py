from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('courses/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
    path('teacher/', views.teacher, name='teacher'),
    path('contact/', views.contact, name='contact'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    
]
