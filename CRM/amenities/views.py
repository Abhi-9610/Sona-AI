from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.
from booking.models import *


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_item(request):
    data={
        "name":request.data.get('name'),
    "price":request.data.get('price'),
    "types":request.data.get('types'),
    "desc":request.data.get('desc'),
    "quantity":request.data.get('quantity'),
    "category":request.data.get('category'),
    "restro_owner_id":str(request.user.id_hotel),
    'image':request.data.get('image')
}
    serializer=resturantSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

        return Response({'status':True,'message':'Successfully added item','data':serializer.data},status=status.HTTP_201_CREATED)

    return Response({'status':False,'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_item(request):

    try:
        rooms = Resturant.objects.filter(restro_owner_id=request.user.id_hotel)
        
    except Resturant.DoesNotExist:
        return Response({'status': False, 'message': 'No Item found for Resturant'}, status=status.HTTP_404_NOT_FOUND)

    serializer = resturantSerializer(rooms, many=True)

    
    return Response({'status': True, 'message': 'Items Details  retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])

@permission_classes([IsAuthenticated])
def update_item(request,item_id):
    try:
        room = Resturant.objects.get(item_id=item_id)
    except Resturant.DoesNotExist:
        return Response({'status': False, 'message': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)

    
    if request.method == 'PUT':
        # Update room details
        serializer = resturantSerializer(room, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'item details updated successfully.','data':serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete room
        room.delete()
        return Response({'status': True, 'message': 'Item deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)








@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_bar(request):
    data={
        "name":request.data.get('name'),
    "price":request.data.get('price'),
    
    "desc":request.data.get('desc'),
    "quantity":request.data.get('quantity'),
    "category":request.data.get('category'),
    "bar_owner_id":str(request.user.id_hotel),
    'image':request.data.get('image')
}
    serializer=barserializer(data=data)
    if serializer.is_valid():
        serializer.save()

        return Response({'status':True,'message':'Successfully added item','data':serializer.data},status=status.HTTP_201_CREATED)

    return Response({'status':False,'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_bar_item(request):

    try:
        rooms = bar.objects.filter(bar_owner_id=request.user.id_hotel)
        
    except bar.DoesNotExist:
        return Response({'status': False, 'message': 'No Item found for bar'}, status=status.HTTP_404_NOT_FOUND)

    serializer = barserializer(rooms, many=True)

    
    return Response({'status': True, 'message': 'Items Details  retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])

@permission_classes([IsAuthenticated])
def update_bar_item(request,item_id):
    try:
        room = bar.objects.get(item_id=item_id)
    except bar.DoesNotExist:
        return Response({'status': False, 'message': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)

    
    if request.method == 'PUT':
        # Update room details
        serializer = barserializer(room, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'item details updated successfully.','data':serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete room
        room.delete()
        return Response({'status': True, 'message': 'Item deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def inverntry(request):
    data={
    "name":request.data.get('name'),
    "price":request.data.get('price'),
    "quantity":request.data.get('quantity'),
    'status':request.data.get('status'),
    "owner_id":str(request.user.id_hotel),
    'image':request.data.get('image'),
    'item_for':request.data.get('for')
}
    serializer=inverntorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()

        return Response({'status':True,'message':'Successfully added item','data':serializer.data},status=status.HTTP_201_CREATED)

    return Response({'status':False,'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_invetory_item(request):

    try:
        owner = inverntory.objects.filter(owner_id=request.user.id_hotel)
        
    except inverntory.DoesNotExist:
        return Response({'status': False, 'message': 'No Item found for inventory'}, status=status.HTTP_404_NOT_FOUND)

    serializer = inverntorySerializer(owner, many=True)

    
    return Response({'status': True, 'message': 'Items Details  retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT', 'DELETE'])

@permission_classes([IsAuthenticated])
def update_inventory_item(request,unique_id):
    try:
        room = inverntory.objects.get(unique_id=unique_id)
    except inverntory.DoesNotExist:
        return Response({'status': False, 'message': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)

    
    if request.method == 'PUT':
        # Update room details
        serializer = inverntorySerializer(room, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'item details updated successfully.','data':serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete room
        room.delete()
        return Response({'status': True, 'message': 'Item deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def laundary(request):
    data={
    "name":request.data.get('name'),
    "price":request.data.get('price'),
    "desc":request.data.get('desc'),
    "owner_id":str(request.user.id_hotel),
    'image':request.data.get('image'),
    
}
    serializer=laundrySerializer(data=data)
    if serializer.is_valid():
        serializer.save()

        return Response({'status':True,'message':'Successfully added item','data':serializer.data},status=status.HTTP_201_CREATED)

    return Response({'status':False,'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

