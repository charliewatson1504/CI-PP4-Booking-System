from django.contrib import admin
from .models import BookPTSession

# Register your models here.


@admin.register(BookPTSession)
class BookPTSessionAdmin(admin.ModelAdmin):
    """
    Admin class for the BookPTSession model
    """
    list_display = ('user', 'staff', 'requested_date',
                    'requested_time', 'status')
