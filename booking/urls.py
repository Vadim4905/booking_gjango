from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_room_list,name='rooms'),
    path('room/<int:pk>/', views.get_room_details,name='room-detail'),
    path('booking/<int:pk>/', views.get_booking_detail,name='booking-detail'),
    path('booking/create', views.booking_from,name='booking-form'),
]
