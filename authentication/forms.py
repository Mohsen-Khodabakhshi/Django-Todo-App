from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.req = kwargs.pop('req', None)
        super(SignUpForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        queryset = User.objects.filter(username=username)
        if queryset.exists():
            messages.error(self.req, 'Username before used')
            raise forms.ValidationError("Username before used")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        queryset = User.objects.filter(email=email)
        if queryset.exists():
            messages.error(self.req, 'Email before used')
            raise forms.ValidationError("Email before used")
        return email

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('password2')
        if password == confirm:
            return self.cleaned_data
        else:
            messages.error(self.req, 'Passwords not match!')
            raise forms.ValidationError('Passwords not match!')
            return redirect('/')

class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
