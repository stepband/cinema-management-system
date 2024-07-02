from django import forms
from .models import Ticket, Screening, Seat


class BookingForm(forms.ModelForm):
    screening = forms.ModelChoiceField(queryset=Screening.objects.all(), empty_label=None, label="Select Screening")
    seat = forms.ModelChoiceField(queryset=Seat.objects.filter(is_available=True), label="Select seat")

    class Meta:
        model = Ticket
        fields = ['screening', 'seat']
