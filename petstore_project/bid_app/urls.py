from django.urls import path
from .views import user_bid_on_pet

urlpatterns = [
    path('bid_on_pet/', user_bid_on_pet),
]