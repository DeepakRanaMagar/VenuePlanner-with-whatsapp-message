from django.urls import path
from .views import CustomerBookingView

urlpatterns = [
    path('create/', CustomerBookingView.as_view()),
]
