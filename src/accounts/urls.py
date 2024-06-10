from django.urls import path

from .views import (CustomerLoginView, CustomerRegisterView, LogoutView,
                    UpdateProfileView, VenueLoginView, VenueRegisterView, SubscriptionView, SubPassView)

urlpatterns = [
    path('register/venue/', VenueRegisterView.as_view()),
    path('register/customer/', CustomerRegisterView.as_view()),


    path('login/venue/', VenueLoginView.as_view()),
    path('login/customer/', CustomerLoginView.as_view()),

    # logout
    path('logout/', LogoutView.as_view()),
    
    #update profile
    path('venue/update/', UpdateProfileView.as_view()),

    #subscription
    path('subcription/', SubscriptionView.as_view()),

    #subcription privileges
    path('subcription/update/', SubPassView.as_view()),
]
