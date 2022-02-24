# Imports
# ---------------------------------------------------------------
# 3rd party:
from django.db import models
from django.contrib.auth.models import User

# Internal
# ---------------------------------------------------------------

# Time choices for booking PT session
time_choices = [
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ]

# Status of PT booking
status_choices = [
    ("confirmed", "confirmed"),
    ("rejected", "rejected"),
    ("pending", "pending"),
    ]

# Staff choices for PT booking
ptStaff = []
staff = User.objects.filter(is_staff=True)
for stf in staff:
    ptStaff.append((str(stf.username), str(stf.username)))

class BookPTSession(models.Model):
    """
    Model for booking a PT session using information from
    User model
    """
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE
    )
    staff = models.CharField(max_length=15, choices=ptStaff, default='karen')
    requested_date = models.DateField()
    requested_time = models.CharField(
        max_length=10, choices=time_choices, default='10:00')
    status = models.CharField(
        max_length=10, choices=status_choices, default='pending')

    def __str__(self):
        """
        Return primary key
        """
        return str(self.pk)
