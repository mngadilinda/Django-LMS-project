from django.urls import path
from contents import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('program/', views.Programvw.as_view(), name='program'),
    path('about/',views.About.as_view(), name='about'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
