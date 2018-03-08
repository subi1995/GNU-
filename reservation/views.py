from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Reservation

# Create your views here.

## Reservation

def Room_Reservation (request):
    reservations = Reservation.objects.all()
    return render (request, 'reservation/reservation_list.html',{'reservations': reservations})

def reservation_detail(request, pk_2):
    reservation = get_object_or_404(Reservation, pk=pk_2)
    return render(request, 'reservation/reservation_detail.html', {'reservation': reservation})
