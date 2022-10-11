from django.shortcuts import render
from django.urls import reverse_lazy
from contents.forms import ProgramForms, ModuleForms, LessonForm
from users.forms import Registration
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.

class CreateProgram(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('contents.add_program')
    template_name = 'program.html'
    success_url = reverse_lazy('home')
    login_url = 'login'
    redirect_field_name = 'home'
    form_class = ProgramForms

class CreateModule(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('Module')
    template_name = 'module.html'
    form_class = ModuleForms
    login_url = 'login'
    redirect_field_name = 'home'

class CreateLesson(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('Lesson')
    template_name = 'lesson.html'
    form_class = LessonForm
    login_url = 'login'
    redirect_field_name = 'home'