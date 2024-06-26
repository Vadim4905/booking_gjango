from  django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('login',views.LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('register',views.RegisterView.as_view(),name='register'),
    path('my-bookings',views.ProfileView.as_view(),name='profile'),
]
