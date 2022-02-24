from django.urls import path
from pt_bookings import views

urlpatterns = [
    path('', views.BookASession.as_view(), name='bookings'),
]