from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('classes', views.classes, name='classes'),
]