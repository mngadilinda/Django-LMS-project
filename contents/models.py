
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Program(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    program_id = models.AutoField(primary_key=True)
    program_img = models.FileField(upload_to='static/images/programs/', blank=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    module_id = models.AutoField(primary_key=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='course')

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField(blank=True)
    lesson_id = models.AutoField(primary_key=True)
    textual_lesson = RichTextField(blank=True)
    less_images = models.FileField(upload_to='static/images/lessons/', blank=True)
    less_video = models.FileField(upload_to='static/lessons/videos/', blank=True)
    less_notes = models.FileField(upload_to='static/lesson/notes/', blank=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='subject')

    def __str__(self):
        return self.title

class Tests_Exams(models.Model):
    title = models.CharField(max_length=300)
    overview = RichTextField(blank=True)
    programs = models.ForeignKey(Program, on_delete=models.CASCADE)
    modules = models.ForeignKey(Module, on_delete=models.CASCADE)
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    test_ex_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
