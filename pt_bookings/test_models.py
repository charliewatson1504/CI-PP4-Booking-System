# Imports
# ---------------------------------------------------------------
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User

# # Internal:
from pt_bookings.models import BookPTSession

# ---------------------------------------------------------------


class TestBookingsModels(TestCase):
    """
    A class for testing the PT Bookings models
    """
    def setUp(self):
        """
        Create a test user, staff member and booking
        """
        test_user = User.objects.create_user(
            username='tester', password='Testing')

        test_staff = User.objects.create_user(
            username='test_staff', password='staff123', is_staff=True)

        test_booking = BookPTSession.objects.create(
            member=test_user,
            staff=test_staff,
            requested_date='01/05/2022',
            requested_time='10:00',
            status='pending',
        )

    def tearDown(self):
        """
        Delete test user, staff member and booking
        """
        User.objects.all().delete()
        BookPTSession.objects.all().delete()
