from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import BookingForm
from .models import Movie


class MovieListView(ListView):
    model = Movie
    template_name = 'index.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.prefetch_related('screening_set').all()


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail_view.html'
    context_object_name = 'movie'


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            seat = ticket.seat
            seat.is_available = False
            seat.save()

            return redirect("/booking")
    else:
        form = BookingForm()

    return render(request, 'ticket_booking.html', {'form': form})

