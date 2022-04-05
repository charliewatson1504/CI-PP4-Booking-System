# # Imports
# # ---------------------------------------------------------------
# # 3rd party:
# from django.test import TestCase
# from django.contrib.auth.models import User

# # # Internal:
# from pt_bookings.models import BookPTSession

# # ---------------------------------------------------------------


# class TestBookingsModels(TestCase):
#     """
#     A class for testing the PT Bookings models
#     """
#     def setUp(self):
#         """
#         Create a test user, staff member and booking
#         """
#         test_user = User.objects.create_user(
#             username='tester', password='Testing123')

#         test_staff = User.objects.create_user(
#             username='test_staff', password='staff1234', is_staff=True)

#         self.booking = BookPTSession(
#             user=test_user,
#             staff=test_staff.username,
#             requested_date='2022-05-01',
#             requested_time='10:00',
#             status='pending',
#         )

#     def test_create_booking(self):
#         """
#         This test tests the booking of a PT session
#         """
#         self.assertEqual(self.booking.user.username, 'tester')
#         self.assertEqual(self.booking.staff, 'test_staff')
#         self.assertEqual(self.booking.requested_date, '2022-05-01')
#         self.assertEqual(self.booking.requested_time, '10:00')
#         self.assertEqual(self.booking.status, 'pending')

#     def test_user_on_delete_cascade_works(self):
#         """
#         This test test if all bookings are deleted
#         for user are removed when user is deleted
#         """
#         User.objects.all().delete()

#         booking = len(BookPTSession.objects.all())

#         self.assertAlmostEqual(booking, 0)