from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models


# Create your views here.

def get_room_list(request):
    rooms = models.Room.objects.all()
    context = {
        'rooms':rooms
    }
    
    return render(request,'booking/rooms_list.html',context=context)


def get_room_details(request,pk):
    room = models.Room.objects.get(id=pk)
    context = {
        'room':room
    }
    return render(request,'booking/room_detail.html',context=context)
    
    
def get_booking_detail(request,pk):
    booking = models.Booking.objects.get(id=pk)
    context = {
        'booking': booking
    }  
    return render(request,'booking/booking_detail.html',context)

def booking_from(request):
    if request.method == 'GET':
        return render(request,'booking/booking_form.html')
    elif request.method == 'POST':
        room_number = request.POST.get('room_number')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        
        try:
            room = models.Room.objects.get(number=room_number)
        except ValueError:
            return HttpResponse('wrong room number',status=404)
        except models.Room.DoesNotExist:
            return HttpResponse('room does not exist',status=404)
        
        booking =models.Booking.objects.create(
            room=room,
            user= request.user,
            start_time = start_time,
            end_time = end_time,
            )
        booking.save()
        return redirect('booking-detail',pk=booking.pk)