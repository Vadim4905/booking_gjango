from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView,DetailView,DeleteView
from . import models
from .forms import BookingForm


# Create your views here.

class RooomsListView(ListView):
    template_name = "booking/housings_list.html"
    model = models.Housing
    context_object_name = "housings"


class HousingDetailView(DetailView):
    template_name = "booking/housing_detail.html"
    model = models.Housing
    context_object_name = "housing"

class BookingDetailView(LoginRequiredMixin,DetailView):
    template_name = "booking/booking_detail.html"
    model = models.Booking
    context_object_name = "booking"
    
class BookingDeleteView(DeleteView):
    template_name = 'booking/confirm_delete.html'
    model = models.Booking
    success_url ="/"
    
    
class BookingCreateView(LoginRequiredMixin,CreateView):
    template_name= 'booking/booking_form.html'
    form_class = BookingForm
    
    def form_valid(self, form):
        housing_id = self.kwargs.get('pk')
        booking = form.save(commit=False)
        booking.housing = get_object_or_404(models.Housing, pk=housing_id)
        booking.user = self.request.user
        booking.save()
        return redirect('booking-detail',pk=booking.pk)
    
