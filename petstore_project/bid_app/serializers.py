from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import PetBid, Pet


class PostPetBidSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetBid
        fields = ['pet_owner', 'pet_bidder', 'pet_id', 'price']


class GetUserSerlaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class GetPetBidsSerializer(serializers.ModelSerializer):
    #pet_owner = GetUserSerlaizer(many=False, read_only=True)
    pet_bidder = GetUserSerlaizer(many=False, read_only=True)

    class Meta:
        model = PetBid
        fields = ['pet_bidder', 'price' ]


class GetBidsOfPetPerOwnerSerlaizer(serializers.ModelSerializer):
    bids = GetPetBidsSerializer(many=True, read_only=True)
    class Meta:
        model = Pet
        fields = ['id', 'bids']