from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_a_session, name='bookings'),
]
