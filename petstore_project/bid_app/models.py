from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Pet(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')


class PetBid(models.Model):
    pet_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owen_pets_bids')
    pet_bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='bids')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])


    class Meta:
        constraints = [
            ## Bidder can not have 2 bids on same pet
            models.UniqueConstraint(fields=['pet_bidder', 'pet_id'], name='pets_bids')
        ]