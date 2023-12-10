from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.forms import ModelForm
from django.db import transaction

    
class PatientForm(ModelForm):
    username=forms.CharField(widget=forms.TextInput())
    first_name=forms.CharField(widget=forms.TextInput())
    last_name=forms.CharField(widget=forms.TextInput())
    address=forms.CharField(widget=forms.TextInput())
    profile_Picture=forms.ImageField(widget=forms.FileInput())
    email=forms.EmailField(widget=forms.EmailInput())
    set_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields = ('username','email','password')
    @transaction.atomic
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_patient=True
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        patient = Patient.objects.create(
            user = user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            address=self.cleaned_data['address'],
            profile_Picture=self.cleaned_data['profile_Picture'],
        )
        return user
    
class DoctorForm(ModelForm):
    username=forms.CharField(widget=forms.TextInput())
    first_name=forms.CharField(widget=forms.TextInput())
    last_name=forms.CharField(widget=forms.TextInput())
    address=forms.CharField(widget=forms.TextInput())
    profile_Picture=forms.ImageField(widget=forms.FileInput())
    email=forms.EmailField(widget=forms.EmailInput())
    set_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields = ('username','email','password')
    @transaction.atomic
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_doctor=True
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        doctor = Doctor.objects.create(
            user = user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            address=self.cleaned_data['address'],
            profile_Picture=self.cleaned_data['profile_Picture'],
        )
        return user