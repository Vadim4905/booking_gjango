from django.shortcuts import redirect,get_object_or_404,render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView,DetailView,DeleteView
from django.urls import reverse_lazy

from . import models
from .forms import BookingForm
import datetime
from calendar import monthrange 
from django.utils import timezone


# Create your views here.


class CustomRenderContext():
    def render_calendar_context(self,context,housing):
        today = timezone.now()
        context['today'] = today
        first_day_of_month = datetime.date(today.year, today.month, 1)
        last_day_of_month = datetime.date(today.year, today.month, monthrange(today.year, today.month)[1])
        
        bookings = models.Booking.objects.filter(housing=housing, start_time__range=(first_day_of_month, last_day_of_month))
        booked_days = []
        for booking in bookings:
            for i in range(booking.start_time.day, booking.end_time.day + 1):
                booked_days.append(i)
        context['booked_days'] = booked_days
        days_of_month = range(1, monthrange(today.year, today.month)[1] + 1)   
        context['days_of_month'] = days_of_month
        return context    


class RooomsListView(ListView):
    template_name = "booking/housings_list.html"
    model = models.Housing
    context_object_name = "housings"


class HousingDetailView(CustomRenderContext,DetailView):
    template_name = "booking/housing_detail.html"
    model = models.Housing
    context_object_name = "housing"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context = self.render_calendar_context(context,kwargs['object'])
        return context

        
class BookingDetailView(LoginRequiredMixin,DetailView):
    template_name = "booking/booking_detail.html"
    model = models.Booking
    context_object_name = "booking"
    

    
    
class BookingDeleteView(DeleteView):
    template_name = 'booking/confirm_delete.html'
    model = models.Booking
    success_url =reverse_lazy('index')

    
    
class BookingCreateView(CustomRenderContext,LoginRequiredMixin,CreateView):
    template_name= 'booking/booking_form.html'
    form_class = BookingForm

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        housing_id = self.kwargs.get('pk')
        housing=get_object_or_404(models.Housing, pk=housing_id)
        context['housing']=housing
        context = self.render_calendar_context(context,housing)
        return context
    
    def form_valid(self, form):
        housing_id = self.kwargs.get('pk')
        booking = form.save(commit=False)
        booking.housing = get_object_or_404(models.Housing, pk=housing_id)
        booking.user = self.request.user
        booking.save()
        return redirect('booking-detail',pk=booking.pk)
    

    



