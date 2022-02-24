import imp
from pyexpat import model
from django import forms
from django.conf import settings

from .models import BookPTSession


class BookingForm(forms.ModelForm):
    """
    A class for the PT booking form
    """

    requested_date = forms.DateField(input_formats=['%d/%m/%y %H:%M'])

    class Meta:
        model = BookPTSession
        fields = ('staff', 'requested_date', 'requested_time')