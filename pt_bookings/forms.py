import imp
from pyexpat import model
from django import forms

from .models import BookPTSession


class BookingForm(forms.ModelForm):
    """
    A class for the PT booking form
    """
    class Meta:
        model = BookPTSession
        fields = ('staff', 'requested_date', 'requested_time')