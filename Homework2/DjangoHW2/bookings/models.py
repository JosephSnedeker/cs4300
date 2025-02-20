from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateTimeField("Date Released")
    duration = models.IntegerField("Duration")

class Seat(models.Model):
    seat_number = models.CharField(max_length=3)
    is_booked = models.BooleanField()

class User(models.Model): #only used for foreign key of Booking
    name = models.TextField()

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)





"""
Movie:
    Fields: title (CharField), description (TextField), release_date (DateField), duration (IntegerField).

Seat: 
    Fields: seat_number (CharField), is_booked (BooleanField).

Booking:
    Fields: movie (ForeignKey to Movie), seat (ForeignKey to Seat), user (ForeignKey to User), booking_date (DateTimeField).

"""