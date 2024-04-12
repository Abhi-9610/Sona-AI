from django.urls import path
from .views import *

urlpatterns=[
    path('booking/',booking),
    path('get-booking/',get_bookingdetails),
    path('update-booking/<str:booking_id>',update_booking)
]