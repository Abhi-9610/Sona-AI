from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
@api_view(['POST'])

@permission_classes([AllowAny])
def booking(request):
    name=request.data.get('name')
    email=request.data.get('email')
    mobile=request.data.get('mobile')
    no_guest=request.data.get('no_guest')
    no_room=request.data.get('no_room')
    date_from=request.data.get('date_from')
    date_to=request.data.get('date_to')
    
    data={
        'name':name,
        'email':email,
        'mobile':mobile,
        'no_guest':no_guest,
        'no_room':no_room,
        'date_from':date_from,
        'date_to':date_to,
        'hotel_id':request.data.get('hotel_id'),
        'govt_id':request.data.get('govt_id'),
        'govt_id_no':request.data.get('id_no'),
        'gender':request.data.get('gender'),
        'nationality':request.data.get('nationality'),
        'no_adult':request.data.get('no_adult'),
        'no_children':request.data.get('no_children')
        

    }

    serializer=bookingserializer(data=data)
    if serializer.is_valid():
        serializer.save()

        return Response({'status':True,'data':serializer.data,'message':'successfully Booked Room'},status=status.HTTP_201_CREATED)
    return Response({'status':False,'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])

@permission_classes([IsAuthenticated])
def get_bookingdetails(request):
    hotel_id = str(request.user.id_hotel)

    try:
        rooms = Bookingdetails.objects.filter(hotel_id=hotel_id)
    except Bookingdetails.DoesNotExist:
        return Response({'status': False, 'message': 'No Booking found for the Hotel'}, status=status.HTTP_404_NOT_FOUND)

    serializer = bookingserializer(rooms, many=True)
    
    return Response({'status': True, 'message': 'Booking Details  retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])

@permission_classes([AllowAny])
def update_booking(request, booking_id):
    try:
        room = Bookingdetails.objects.get(booking_id=booking_id)
    except Bookingdetails.DoesNotExist:
        return Response({'status': False, 'message': 'Booking not found.'}, status=status.HTTP_404_NOT_FOUND)

    
    if request.method == 'PUT':
        # Update room details
        serializer = bookingserializer(room, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'Booking details updated successfully.','data':serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete room
        room.delete()
        return Response({'status': True, 'message': 'Booking deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)