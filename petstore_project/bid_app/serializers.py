from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import PetBid


class PostPetBidSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetBid
        fields = ['pet_owner', 'pet_bidder', 'pet_id', 'price']

