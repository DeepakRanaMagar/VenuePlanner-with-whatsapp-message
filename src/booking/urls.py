from django.urls import path
from .views import BookingView

urlpatterns = [
    path('create/', BookingView.as_view()),
]
