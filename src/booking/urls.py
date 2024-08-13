from django.urls import path
from .views import CustomerBookingView, VenueBookingView

urlpatterns = [
    path('create/', CustomerBookingView.as_view()),
    path('view/', VenueBookingView.as_view()),
]
