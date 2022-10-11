from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from .models import Program, Module, Lesson
from contents.forms import ProgramForms, ModuleForms, LessonForm

# Create your views here.


class Home(ListView):
    template_name = 'home.html'
    model = Program
    context_object_name = 'programs'
    

class Programvw(LoginRequiredMixin, TemplateView):
    template_name = 'programss.html'
    login_url = 'login'
    redirect_field_name = 'home'

class About(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'
    login_url = 'login'
    redirect_field_name = 'home'
    