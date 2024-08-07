from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import BookingForm
from .models import Movie, Screening


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


def booking(request, screening_id):
    screening = get_object_or_404(Screening, id=screening_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, screening=screening)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.screening = screening
            ticket.user = request.user
            ticket.save()
            return redirect('index')
    else:
        form = BookingForm(screening=screening)

    return render(request, 'ticket_booking.html', {'form': form, 'screening': screening})

