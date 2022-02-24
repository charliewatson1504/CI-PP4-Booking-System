from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
import datetime

from .models import BookPTSession
from .forms import BookingForm


# Create your views here.
class BookASession(View):
    """
    This view allows users to book a session
    """
    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            booking_form = BookingForm()
        else:
            messages.add_message(
                request, messages.ERROR,
                "Sorry, you are not logged in."
                "Please login here.")
            url = reverse('login')
            return HttpResponseRedirect(url)
        
        return render(request, "bookings.html",
                        {'booking_form': booking_form})


