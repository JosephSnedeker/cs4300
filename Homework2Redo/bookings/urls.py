from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("movies", views.movieview, name="movies"),
    path("seats/<int:movie_id>", views.seatview, name="seatview"),
    path("mybookings", views.bookingview, name="bookingview"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)