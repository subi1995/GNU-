from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):

    class Meta:
            model = Reservation
            fields = ('tel_num','major','room_number','rend_date','return_date')
