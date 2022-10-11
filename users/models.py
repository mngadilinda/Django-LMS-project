from django.db import models
from django import forms
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


"""""
    class Meta:
        model = User
        fields = '__all__'
"""""