from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import PROTECT


class User(AbstractUser):
    pass


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Genre: {self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre, related_name="movie", blank=True)
    release_date = models.DateField(null=True)
    duration = models.DurationField(null=True)


class TheaterRoom(models.Model):
    room_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Room Name: {self.room_name}"


class Seat(models.Model):
    theater_room = models.ForeignKey('TheaterRoom', on_delete=models.CASCADE)
    row_number = models.IntegerField()
    column_number = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Seat {self.row_number}-{self.column_number} ({'Available' if self.is_available else 'Booked'})"


class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    theater_room = models.ForeignKey(TheaterRoom, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.movie.title} - {self.date} {self.time}"


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=PROTECT)
    screening = models.ForeignKey(Screening, on_delete=PROTECT)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
