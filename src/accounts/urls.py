from django.urls import path

from .views import CustomerRegisterView, VenueRegisterView

urlpatterns = [
    path('register/venue/', VenueRegisterView.as_view()),
    path('register/customer/', CustomerRegisterView.as_view())

]
