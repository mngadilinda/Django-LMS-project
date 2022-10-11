from django.urls import path
from admins import views


urlpatterns = [
    path('programs/',views.CreateProgram.as_view(), name='createprog'),
    path('modules/',views.CreateModule.as_view(), name='createmodule'),
    path('lessons/',views.CreateLesson.as_view(), name='createless'),
]
