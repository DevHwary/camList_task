from django.urls import path
from .views import user_bid_on_pet, get_bids_of_pet_per_owner

urlpatterns = [
    path('bid_on_pet/', user_bid_on_pet),
    path('pet_bids/', get_bids_of_pet_per_owner),
]