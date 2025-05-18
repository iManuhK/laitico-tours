from django import forms
from .models import Inquiry, Booking

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone', 'subject', 'message']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['destination', 'name', 'email', 'from_date', 'to_date', 'pax']
        widgets = {
            'destination': forms.HiddenInput(),
            'from_date': forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'}),
            'pax': forms.NumberInput(attrs={'min': 1}),
        }

class TailorPackageForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['destination', 'name', 'email', 'from_date', 'to_date', 'pax']
        labels = {
            'destination': 'Preferred Destination',
            'name': 'Full Name',
            'email': 'Email Address',
            'from_date': 'Start Date',
            'to_date': 'End Date',
            'pax': 'Number of People',
        }
        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'}),
            'pax': forms.NumberInput(attrs={'min': 1}),
        }
