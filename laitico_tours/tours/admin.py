from django.contrib import admin
from .models import Destination, Booking, Inquiry

# Register your models here.
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_popular')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'destination', 'from_date', 'to_date', 'booking_date', 'pax', 'price')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
        list_display = ('email', 'subject', 'phone', 'message')