from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from . serializers import PostPetBidSerializer, GetBidsOfPetPerOwnerSerlaizer
from django.db import IntegrityError
from . models import Pet


'''
Need some permissions
'''
@api_view(['POST'])
@parser_classes([JSONParser])
def user_bid_on_pet(request):
    try :
        bid_data_serializer = PostPetBidSerializer(data=request.data)
        if bid_data_serializer.is_valid():
            bid_data_serializer.save()
            return Response(bid_data_serializer.data, status=status.HTTP_201_CREATED)
        return Response(bid_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except IntegrityError as e:
        return Response(str(e), status=status.HTTP_406_NOT_ACCEPTABLE)


'''
Need some permissions
'''
@api_view(['GET'])
@parser_classes([JSONParser])
def get_bids_of_pet_per_owner(request):
    try :
        id=request.data['pet_id']
        pet = Pet.objects.get(id=id)
        bids_data_serializer = GetBidsOfPetPerOwnerSerlaizer(pet, many=False)
        return Response(bids_data_serializer.data, status=status.HTTP_200_OK)
        
    except Pet.DoesNotExist:
        return Response("There is no bid for this pet", status=status.HTTP_404_NOT_FOUND)
    except KeyError as e:
        return Response("Please provide a valid: " + str(e), status=status.HTTP_400_BAD_REQUEST)