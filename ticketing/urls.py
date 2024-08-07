from django.urls import path

from . import views
from .views import MovieListView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name='index'),
    path('movies/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('booking/<int:screening_id>/', views.booking, name='booking')
]
