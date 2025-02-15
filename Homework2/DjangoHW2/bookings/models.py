Movie:
    Fields: title (CharField), description (TextField), release_date (DateField), duration (IntegerField).

Seat: 
    Fields: seat_number (CharField), is_booked (BooleanField).

Booking:
    Fields: movie (ForeignKey to Movie), seat (ForeignKey to Seat), user (ForeignKey to User), booking_date (DateTimeField).

