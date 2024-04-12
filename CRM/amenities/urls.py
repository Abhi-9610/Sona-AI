from django.urls import path
from .views import *

urlpatterns=[
    path('resturant/add-item/',add_item),
    path('resturant/get-items/',get_item),
    path('resturant/update-item/<str:item_id>',update_item),
    path('bar/add-item/',add_bar),
    path('bar/get-item/',get_bar_item),
    path('bar/update-item/<str:item_id>',update_bar_item),
    path('inventory/add-item/', inverntry),
    path('inventory/get-items/',get_invetory_item),
    path('inventory/update-item/<str:unique_id>',update_inventory_item),
    path('laundary/add-item/',laundary)
]