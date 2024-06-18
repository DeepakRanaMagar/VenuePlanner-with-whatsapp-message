from django.urls import path

from .views import VenueView

urlpatterns = [
    path('venues/', VenueView.as_view())
]
