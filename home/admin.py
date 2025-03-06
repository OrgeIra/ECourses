from django.contrib import admin

# Register your models here.
from .models import Course, Teacher, Student, ContactMessage

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(ContactMessage)

