from django.template import loader
from django.http import HttpResponse
from .models import Booking

from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm

# Create your views here.

# all_booking.html
def bookings(request):
    mybookings = Booking.objects.all().values()
    template = loader.get_template('all_bookings.html')
    context = {
        'mybookings': mybookings,
    }
    return HttpResponse(template.render(context, request))

# details.html
def details (request, id):
    mybooking = Booking.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mybooking': mybooking,
    }
    return HttpResponse(template.render(context, request))

# index.html
def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# add_booking.html
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('bookings')
    else:
        form = BookingForm()
    return render(request, 'add_booking.html', {'form': form})

# edit_booking.html
def edit_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'edit_booking.html', {'form': form})

# delele_booking.html
def delete_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        booking.delete()
        return redirect('bookings')
    return render(request, 'delete_booking.html', {'booking': booking})