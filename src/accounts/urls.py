from django.urls import path

from .views import (CustomerLoginView, CustomerRegisterView, VenueLoginView,
                    VenueRegisterView)

urlpatterns = [
    path('register/venue/', VenueRegisterView.as_view()),
    path('register/customer/', CustomerRegisterView.as_view()),


    path('login/venue/', VenueLoginView.as_view()),
    path('login/customer/', CustomerLoginView.as_view()),
]
