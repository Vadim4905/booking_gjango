from . import views
from django.urls import path

urlpatterns = [
    path('', views.RooomsListView.as_view(),name='index'),
    path('housing/<int:pk>/', views.HousingDetailView.as_view(),name='housing-detail'),
    path('booking/<int:pk>/', views.BookingDetailView.as_view(),name='booking-detail'),
    path('delete/booking/<int:pk>/', views.BookingDeleteView.as_view(),name='booking-delete'),
    path('create/booking/<int:pk>/', views.BookingCreateView.as_view(),name='booking-form'),
]
