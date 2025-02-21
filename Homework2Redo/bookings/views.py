from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from . models import Movie, Seat


def index(request):
    return HttpResponse("This is the index view")

def movieview(request):
    all_movies_list = Movie.objects.all()
    context = {"all_movies_list": all_movies_list}    
    return render(request, "bookings/movie_list.html", context)

def seatview(request, movie_id): #movie id only used for pathing at this point, will be checked again when seat is booked
    
    seat_list = Seat.objects.all()
    context = {"seat_list": seat_list}
    return render(request, "bookings/seat_booking.html", context)

def bookingview(request):
    return HttpResponse("This is the booking view")