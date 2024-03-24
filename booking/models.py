from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    number = models.CharField(max_length=50)
    capacity =models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.number
    
class Booking(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='bookings')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"booking room number: {self.room.number}"
    
