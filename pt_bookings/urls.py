from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_a_session, name='bookings'),
    path('booked_sessions', views.view_booked_sessions, name='booked_sessions'),
]
