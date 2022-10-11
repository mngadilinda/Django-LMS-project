from django.urls import path
from users import views



urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/',views.ULogin.as_view(), name='login'),
    path('logout/',views.ULogout.as_view(), name='logout'),
    
]
