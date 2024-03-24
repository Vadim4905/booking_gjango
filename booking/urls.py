from . import views
from django.urls import path

urlpatterns = [
    path('rooms/', views.get_room_list,name='rooms'),
    path('rooms/<int:pk>/', views.get_room_details,name='room'),
]
