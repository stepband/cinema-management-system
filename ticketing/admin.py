from django.contrib import admin


from .models import Movie, TheaterRoom, Seat, Screening, Ticket, Genre

admin.site.register(Movie)
admin.site.register(TheaterRoom)
admin.site.register(Seat)
admin.site.register(Screening)
admin.site.register(Ticket)
admin.site.register(Genre)
