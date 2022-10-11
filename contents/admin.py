from django.contrib import admin
from .models import Program, Module, Lesson, Tests_Exams

# Register your models here.
admin.site.register(Program)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Tests_Exams)