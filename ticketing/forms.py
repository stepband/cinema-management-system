from django import forms
from models import Ticket, Screening, Seat


class BookingForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['screening', 'seat']