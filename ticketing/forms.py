from django import forms
from django.forms import ModelChoiceField

from .models import Ticket, Screening, Seat


class BookingForm(forms.ModelForm):
    seat = ModelChoiceField(queryset=Seat.objects.all(), required=True, label="Select seat")

    class Meta:
        model = Ticket
        fields = ['seat']

    def __init__(self, *args, **kwargs):
        screening = kwargs.pop('screening', None)
        super().__init__(*args, **kwargs)
        if screening:
            self.fields['seat'].queryset = Seat.objects.filter(
                theater_room=screening.theater_room
            ).exclude(
                id__in=Ticket.objects.filter(screening=screening).values_list('seat_id', flat=True)
            )

