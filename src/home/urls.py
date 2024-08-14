from django.urls import path

from .views import VenueSeatCapacityView, VenueView

urlpatterns = [
    path('venues/', VenueView.as_view()),
    path('venues/seats/', VenueSeatCapacityView.as_view())

]
