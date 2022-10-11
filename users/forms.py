
from django import forms
from admins.models import Instructor, Student
#from .models import Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


User_types = (
        ('Student','Student'),
        ('Instructor','Instructor'),
    )

class Registration(UserCreationForm):
    user_type = forms.ChoiceField(choices=User_types)
    """"username = forms.CharField(max_length=200)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)"""""
    email = forms.EmailField()
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username','email','password1','password2', 'user_type']

"""""
        def save(self, commit=True):
            user = super(Registration, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

            """""