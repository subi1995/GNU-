from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Reservation
from .forms import ReservationForm

# Create your views here.

## Reservation

def Room_Reservation (request):
    reservations = Reservation.objects.all()
    return render (request, 'reservation/reservation_list.html',{'reservations': reservations})

def reservation_detail(request, pk_2):
    reservation = get_object_or_404(Reservation, pk=pk_2)
    return render(request, 'reservation/reservation_detail.html', {'reservation': reservation})

def reservation_new(request):
    print(request.method, '1')
    if request.method == "POST":
        print(request.method, '2')
        form = ReservationForm(request.POST)
        print(form, '4156')
        if form.is_valid():
            print(request.method, '3')
            reservation = form.save(commit=False)
            reservation.author = request.user
            reservation.updated_date = timezone.now()
            reservation.save()
            return redirect('reservation_detail', pk_2=reservation.pk)
    else:
        print(request.method, '4')
        form = ReservationForm()
    return render(request, 'reservation/reservation_edit.html', {'form': form})
