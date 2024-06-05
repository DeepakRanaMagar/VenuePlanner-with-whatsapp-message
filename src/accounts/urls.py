from django.urls import path

from .views import CustomerRegisterView, VenueRegisterView, VenueLoginView, CustomerLoginView

urlpatterns = [
    path('register/venue/', VenueRegisterView.as_view()),
    path('register/customer/', CustomerRegisterView.as_view()),


    path('login/venue/', VenueLoginView.as_view()),
    path('login/customer/', CustomerLoginView.as_view()),
]
