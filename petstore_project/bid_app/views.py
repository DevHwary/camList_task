from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from . serializers import PostPetBidSerializer
from django.db import IntegrityError


@api_view(['POST'])
@parser_classes([JSONParser])
def user_bid_on_pet(request):
    bid_data_serializer = PostPetBidSerializer(data=request.data)
    try :
        if bid_data_serializer.is_valid():
            bid_data_serializer.save()
            return Response(bid_data_serializer.data, status=status.HTTP_201_CREATED)
        return Response(bid_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except IntegrityError as e:
        return Response(str(e), status=status.HTTP_406_NOT_ACCEPTABLE)