import json
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import PetBid, Pet


class GetBidsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="hwary")
        self.pet = Pet.objects.create(owner_id=self.user)
        self.bid_on_pet = PetBid.objects.create(
                pet_owner=self.user,
                pet_bidder=self.user,
                pet_id=self.pet, price=50.00)
        self.client = APIClient() 


    def test_get_bids_of_pet_per_owner(self):
        data = {"pet_id" : 1}
        response = self.client.generic(
                method='GET', 
                path='/bids/pet_bids/', 
                data=json.dumps(data), 
                content_type="application/json")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.bid_on_pet.id)
        self.assertEquals(response.data['bids'][0]['price'], '50.00')
        self.assertEquals(response.data['bids'][0]['pet_bidder']['username'], 'hwary')
