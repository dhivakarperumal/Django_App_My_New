from django.contrib.auth.forms import UserCreationForm
from .models import User,Contact
from django import forms


class userCustomForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Conform Password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email', 'required': True}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 6, 'required': True}),
        }