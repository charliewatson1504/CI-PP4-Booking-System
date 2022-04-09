from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('classes/', views.classes, name='classes'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]