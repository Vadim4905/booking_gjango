from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView,View
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class LoginView(LoginView):
    template_name = "auth_system/login.html"
    
    
class RegisterView(CreateView):
    template_name = "auth_system/register.html"
    form_class = CustomUserCreationForm
    
    def form_valid(self, form: CustomUserCreationForm):
        user = form.save()
        login(self.request, user)
        return redirect("index")
    
class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        return render(
            request,
            "auth_system/profile.html",
            {
                "title": "Profile",
                "user": self.request.user,
                
            },
        )
