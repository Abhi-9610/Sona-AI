import genericpath
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token




@api_view(['POST'])
@permission_classes([AllowAny])
def signup_api(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.otp = '1234'  # Set the predefined OTP value
        user.save()
        return Response({'message': 'Account created successfully. OTP sent.','status':True}, status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors,'status':False}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def signin_api(request):
    phone_number = request.data.get('phone_number', '')
    otp_entered = request.data.get('otp', '')

    try:
        user = CustomUser.objects.get(username=phone_number)
    except ObjectDoesNotExist:
        return Response({'message': 'User not found.', 'status':False}, status=status.HTTP_404_NOT_FOUND)

    if user and user.otp == otp_entered:
        user.otp = ''
        user.save()
        
        token, created = Token.objects.get_or_create(user=user)

        if not created:
            return Response({'message': 'User already logged in.','status':False}, status=status.HTTP_400_BAD_REQUEST)

        if not user.hotel_name:
            response_data={
                'status': True,
                'has_hotel_details': False,
                'message': 'Please enter your hotel details.',
                'token': str(token),
                'user': UserSerializer(user).data
            }

            return JsonResponse(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                'status':True,
                'message': 'Welcome back!',
                'data': str(token),
                'user': UserSerializer(user).data
            }
            response = JsonResponse(response_data, status=status.HTTP_200_OK)
            response['Authorization'] = f'Bearer {token}'
            return response
    else:
        new_otp = generate_new_otp()
        user.otp = new_otp
        user.save()
        return Response({'message': 'Invalid OTP. New OTP sent.','status':False}, status=status.HTTP_401_UNAUTHORIZED)

def generate_new_otp():
    
    new_otp = '4567'  # Replace with your actual OTP generation logic
    return new_otp




# views.py


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def enter_hotel_details(request):
    user = request.user

    if request.method == 'POST':
   
        # Update the user object with the entered details
        user.hotel_name = request.data.get('hotel_name','')
        user.reg_num = request.data.get('reg_num','')
        user.gst_number = request.data.get('gst_number','')
        user.official_email = request.data.get('official_email','')
        user.geo_location = request.data.get('geo_location','')
        user.total_rooms = request.data.get('total_rooms')
        user.hotel_logo= request.data.get('hotel_logo')
        user.save()

        if not user.hotel_name:
            return Response({
                'message': 'Please enter your hotel details',
                'data': UserSerializer(user).data
             }, status=status.HTTP_400_BAD_REQUEST)
            

        return Response({
            'message': 'Hotel details successfully entered',
            "data":UserSerializer(user).data
            # 'details': UserSerializer(user).data
        }, status=status.HTTP_200_OK)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def staff_management(request):
    user = request.user

    if request.method == 'POST':
        # Token validation and blacklist check
       

        # Your existing logic for staff management
        email = request.data.get('email')
        role = request.data.get('role')
        name = request.data.get('name')
        auth_token=request.headers.get('Authorization').split()[1]
        token=Token.objects.get(key=auth_token)
        user = CustomUser.objects.get(email=token.user.email)
        print(user.name)
        owner_id = user.unique_id
        


        if (email==None or name==None or role==None):
         return Response({'status':False,'message':"Insufficient data"},status=status.HTTP_400_BAD_REQUEST)
        dataobj={
            'name':name,
            'email':email,
            'role':role,
            'owner_id':str(owner_id)
        }
   
        serializer=staffSerializer(data=dataobj)
        if serializer.is_valid():
            serializer.save()





        return Response({
            'status':True,
            'message': 'Staff setup successfully completed',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    return Response({
        'status':False,
        'message': 'Invalid request method',
    }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def signout_api(request):
    user = request.user

    try:
      
        token = Token.objects.get(user=user)

        # Delete the token
        token.delete()

        
        
        user.save()

        return Response({'detail': 'Successfully signed out.',
                         "name":UserSerializer(user).data['name']}
                         , status=status.HTTP_200_OK)

    except :
        return Response({'detail': 'Error during sign-out.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        




@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def roomsetup(request):
    # Include the owner_id in the request data
    room_types=request.data.get('room_types',0)
    room_number=request.data.get('room_number')
    auth_token=request.headers.get('Authorization').split()[1]
    token=Token.objects.get(key=auth_token)
    user = CustomUser.objects.get(email=token.user.email)
        # print(user.name)
    owner_id = user.unique_id
    dataobject={
        'room_types':room_types,
        'room_number':room_number,
        'owner_id':str(owner_id)
    }

    

    
    serializer=Roomserializer(data=dataobject)
    # print(serializer)
    if serializer.is_valid():
        serializer.save()
        datanew={
            'room types':serializer.data
        }
    

    return Response({'status': False, 'message': datanew}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile_api(request):
    user = request.user

    if request.method == 'GET':
        try:
            subuser = CustomUser.objects.get(unique_id=user.unique_id)
            serializer = UserSerializer(subuser)
        

        
                

            data={
                    'name':serializer.data.get('name'),
                    'mobile':serializer.data.get('phone_number'),
                    'email':serializer.data.get('email'), }
                
            

            return Response({'message':'successfull','status': True, 'data':data,
                            }, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
           return Response({'message': 'Not found', 'status': False}, status=status.HTTP_404_NOT_FOUND)

   
    elif request.method == 'PUT':
        subuser = CustomUser.objects.get(unique_id=user.unique_id)
            # serializer = UserSerializer(subuser)
        # Update user profile information
        serializer = UserSerializer(subuser, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            data={
                    'name':serializer.data.get('name'),
                    'mobile':serializer.data.get('phone_number'),
                    'email':serializer.data.get('email'), }
            return Response({'status': True, 'message': 'successfull.','data':data}, status=status.HTTP_200_OK)
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete user profile
        user.delete()
        return Response({'status': True, 'message': 'User profile deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def staff_details(request):
    unique_id = request.user.unique_id
    print(unique_id)
    
    staff_members = staff.objects.filter(owner_id=unique_id)

    if staff_members.exists():
        serializer = staffSerializer(staff_members, many=True)
        return JsonResponse({'message':'successfull','status':True,'data':serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse({'message': 'Staff not found','status':False}, status=status.HTTP_404_NOT_FOUND)
@api_view(['PUT',"DELETE"])
@permission_classes([IsAuthenticated])
def updatestaff(request, unique_id):
    try:
        # Retrieve the staff member by unique ID
        staff_member = staff.objects.get(unique_id=unique_id, owner_id=request.user.unique_id)
    except staff.DoesNotExist:
        return JsonResponse({'status': False, 'message': 'Staff member not found'}, status=status.HTTP_404_NOT_FOUND)
  

    if request.method=='PUT':
    # Update the staff member's details with the request data
            serializer = staffSerializer(staff_member, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
            
                    

                data={
                        'name':serializer.data.get('name'),
                        'role':serializer.data.get('role'),
                        'email':serializer.data.get('email'),
                    
                        

                        
                    }


                return JsonResponse({'message':'successfull','status':True,'data':data}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        serializer.delete()
        return Response({'status':True,'message':'Staff deleted Successfully'},status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def room_details_api(request, room_id):
    try:
        room = Roomdata.objects.get(id=room_id,owner_id=request.user.unique_id)
    except ObjectDoesNotExist:
        return Response({'status': False, 'message': 'Room not found.'}, status=status.HTTP_404_NOT_FOUND)

    
    if request.method == 'PUT':
        # Update room details
        serializer = Roomserializer(room, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'Room details updated successfully.','data':serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete room
        room.delete()
        return Response({'status': True, 'message': 'Room deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def room_details(request):
    owner_id = str(request.user.unique_id)

    try:
        rooms = Roomdata.objects.filter(owner_id=owner_id)
    except Roomdata.DoesNotExist:
        return Response({'status': False, 'message': 'No rooms found for the user'}, status=status.HTTP_404_NOT_FOUND)

    serializer = Roomserializer(rooms, many=True)
    return Response({'status': True, 'message': 'Rooms retrieved successfully', 'total_rooms': serializer.data}, status=status.HTTP_200_OK)



