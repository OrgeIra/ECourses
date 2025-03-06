from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control border-0 py-3 px-4', 'rows': 5, 'placeholder': 'Message'}),
        }
