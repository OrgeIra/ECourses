import os
import subprocess
from django.db import models
from django.utils.text import slugify

class Course(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    duration = models.IntegerField(blank=True, null=True)  
    price = models.PositiveIntegerField(default=99)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    students_count = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='images/courses/', blank=True, null=True)

    @property
    def get_absolute_url(self):
        return self.image.url if self.image else ''

    @property
    def get_video_url(self):
        return self.video.url if self.video else ''

    def get_video_duration(self, video_path):
        try:
            result = subprocess.run(
                ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                 "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", video_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return int(float(result.stdout.strip())) if result.stdout else None
        except Exception as e:
            print(f"Ошибка при определении длительности видео: {e}")
            return None

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            counter = 1
            original_slug = self.slug
            while Course.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1

        if self.video and self.video.path:
            self.duration = self.get_video_duration(self.video.path)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/teachers/', blank=True, null=True)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="teachers")
    
    @property
    def get_absolute_url(self):
        if self.image:
            return self.image.url
        return ''
    

    def __str__(self):
        return f"{self.name} ({self.course.name})"


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return f"{self.name} - {self.course.name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
