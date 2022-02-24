# Imports
# ---------------------------------------------------------------
# 3rd party:
from curses.ascii import US
from django.db import models
from django.contrib.auth.models import User

# # Internal
# ---------------------------------------------------------------

# Time choices for booking PT session
time_choices = (
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    )

# Status of PT booking
status_choices = (
    ("confirmed","confirmed"),
    ("rejected","rejected"),
    ("pending","pending"),
)


class BookPTSession(models.Model):
    """
    Model for booking a PT session using information from
    User model
    """
    member = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE
    )
    staff = models.ForeignKey(
        User.is_staff,
        null=True,
        on_delete=models.CASCADE
    )
    requested_date = models.DateField()
    requested_time = models.CharField(
        max_length=10, choices=time_choices, default='10:00')
    status = models.CharField(
        max_length=10, choices=status_choices, default='pending')
    
    def __str__(self):
        return str(self.pk)
