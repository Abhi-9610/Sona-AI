from django.urls import path
from .views import *
# from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('signout/', signout_api, name='signout_api'),
    path('signin/', signin_api, name='signin_api'),
    path('signup/', signup_api, name='signup_api'),
    path('hotel-details/',enter_hotel_details,name='enter-hotel-detials'),
    path('setup/', roomsetup,name="room_setup"),
    path('staff-management/', staff_management, name='staff_api'),
    path('room-details/<int:room_id>',room_details_api),
    path('profile/', user_profile_api, name='user_profile'),
    path('get-rooms/',room_details),
    path('get-staff/',staff_details),
    path('update-staff/<str:unique_id>',updatestaff),
    
   
    
]
