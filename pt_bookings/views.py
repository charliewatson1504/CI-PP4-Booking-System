import datetime
from django.shortcuts import render, reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import BookPTSession
from .forms import BookingForm


def check_if_available(user_requested_staff, user_requested_date,
                       user_requested_time):
    """
    Check to see if time slot has already been booked
    """

    booking_slot = len(BookPTSession.objects.filter(
        staff=user_requested_staff, requested_date=user_requested_date,
        requested_time=user_requested_time))

    return booking_slot


# Create your views here.
class BookASession(View):
    """
    This view allows users to book a session
    """
    def get(self, request, *args, **kwargs):
        """
        Opens booking form
        """
        if request.user.is_authenticated:
            booking_form = BookingForm()
        else:
            messages.add_message(
                request, messages.ERROR,
                "Sorry, you are not logged in."
                "Please login here.")
            url = reverse('login')
            return HttpResponseRedirect(url)

        return render(request, "pt_bookings/bookings.html",
                      {'booking_form': booking_form})

    def post(self, request, *args, **kwargs):
        """
        Post form if valid
        """
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            user_requested_staff = request.POST.get('staff')
            user_requested_date = request.POST.get('requested_date')
            user_requested_time = request.POST.get('requested_time')

            correct_date_format = datetime.datetime.strptime(
                user_requested_date, "%d/%m/%Y").strftime('%Y-%m-%d')

            booking_available = check_if_available(
                user_requested_staff,
                correct_date_format,
                user_requested_time)

            if booking_available > 0:
                messages.add_message(
                    request, messages.ERROR,
                    "Unfortunately this slot is already booked"
                    f"{user_requested_time} on {user_requested_date}.")

                return render(
                    request,
                    'pt_bookings/bookings.html',
                    {'booking_form': booking_form})
            else:
                booking_form.save()

                messages.add_message(
                    request, messages.SUCCESS,
                    f"Your booking with {user_requested_staff} "
                    f"on {user_requested_date} at {user_requested_time}"
                    f" has been submitted.")
                url = reverse('bookings')
                return HttpResponseRedirect(url)

        else:
            messages.add_message(
                request, messages.ERROR,
                "Sorry, something was not quite right. "
                "Please try again.")

            return render(
                request,
                'pt_bookings/bookings.html',
                {'booking_form': booking_form})
