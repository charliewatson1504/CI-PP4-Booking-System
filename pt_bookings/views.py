import datetime
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
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


def book_a_session(request):
    """
    A view for booking a PT session

    Args:
        request (object): HTTP request object

    Returns:
        renders the booking form
    """
    if request.method == 'GET':
        if request.user.is_authenticated:
            booking_form = BookingForm()
        else:
            messages.add_message(
                request, messages.ERROR,
                "Sorry, you are not logged in."
                "Please login here.")
            url = reverse('account_login')
            return HttpResponseRedirect(url)

        return render(request, "pt_bookings/bookings.html",
                      {'booking_form': booking_form})
    else:
        if request.method == 'POST':
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
                    booking_data = booking_form.save(commit=False)
                    booking_data.user = request.user
                    booking_data.save()

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
        else:
            messages.add_message(
                request, messages.ERROR,
                "Sorry, something was not quite right. "
                "Please try again.")
            url = reverse('bookings')
            return HttpResponseRedirect(url)


def view_booked_sessions(request):
    """
    A view to view booked sessions    

    Args:
        request (object): HTTP request object
    
    Returns:
        renders booked sessions for user
    """
    if request.user.is_authenticated:
        if request.user.is_superuser:
            booked_sessions = BookPTSession.objects.filter(staff=request.user).order_by('requested_date')
        else:
            booked_sessions = BookPTSession.objects.filter(user=request.user).order_by('requested_date')

        template = 'pt_bookings/booked_sessions.html'
        context = {
            'sessions': booked_sessions
        }

        return render(request, template, context)


def edit_booking(request, booking_id):
    """
    A view to edit a booked session

    Args:
        request (object): HTTP request object
        booking_id: Booked session id
    """
    if not request.user.is_authenticated:
        messages.add_message(
            request, messages.ERROR,
            "Sorry, you are not logged in."
            "Please login here.")
        url = reverse('account_login')
        return HttpResponseRedirect(url)

    booking_to_edit = get_object_or_404(BookPTSession, pk=booking_id)
    booking_to_edit.requested_date = datetime.datetime.strftime(
                            booking_to_edit.requested_date, '%d/%m/%Y')

    if request.method == 'POST':
        booking_form = BookingForm(request.POST, instance=booking_to_edit)

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
                    'pt_bookings/edit_booking.html',
                    {'booking_form': booking_form})
            else:
                booking_form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    "Your booking has been updated")
                url = reverse('booked_sessions')
                return HttpResponseRedirect(url)
        else:
            messages.add_message(
                request, messages.ERROR, "Sorry, edit was not successful.")
            url = reverse('booked_sessions')
            return HttpResponseRedirect(url)
    else:
        booking_form = BookingForm(instance=booking_to_edit)

    template = 'pt_bookings/edit_booking.html'
    context = {
        'booking_form': booking_form,
        'booked_session': booking_to_edit,
    }
    return render(request, template, context)
