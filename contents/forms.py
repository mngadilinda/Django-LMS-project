from django.forms import ModelForm, Textarea
from ckeditor.fields import RichTextField
from contents.models import Program, Module, Lesson


class ProgramForms(ModelForm):
    class Meta:
        model = Program
        fields = ['title', 'description', 'program_img']
        widgets = { 'description' : Textarea}

class ModuleForms(ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'description', 'program']
        widgets = { 'description' : Textarea}

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'overview', 'textual_lesson', 'less_video', 'less_images', 'less_notes', 'module']
        widgets = { 'description' : Textarea, 'textual_lesson': RichTextField()}