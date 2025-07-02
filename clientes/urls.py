from django.urls import path
from . import views
from .views import clientes

urlpatterns = [
    path('', views.estudiantes),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    
    ]