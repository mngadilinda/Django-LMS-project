from django.db import models
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your models here.
class Instructor(models.Model):
    firsttname = models.CharField(max_length=200)
    lassttname = models.CharField(max_length=200)



    def __str__(self):
        return self.name


class Student(models.Model):
    firsttname = models.CharField(max_length=200)
    lassttname = models.CharField(max_length=200)

    def __str__(self):
        return self.name


"""""
this is for Instructors
    class Meta:
        permissions = (
            ('contents.add_program'),
            ('contents.add_module'),
            ('contents.add_lesson'),
            ('contents.view_program'),
            ('contents.view_module'),
            ('contents.view_lesson'),
            ('contents.change_porgram'),
            ('contents.change_module'),
            ('contents.change_lesson'),
        )
This is for Students
        class Meta:
        permissions = (
            ('contents.view_program'),
            ('contents.view_module'),
            ('contents.view_lesson'),
            
        )

"""""