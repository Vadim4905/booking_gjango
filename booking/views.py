from django.shortcuts import render
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
    