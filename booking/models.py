from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.  

class Housing(models.Model):
    title = models.CharField(max_length=50)
    capacity =models.IntegerField()
    description = models.TextField()
    price_per_day = models.DecimalField(decimal_places=2, max_digits=5)
    location = models.CharField(max_length=100)
    images = models.ManyToManyField('Image',related_name='housings')
    rating = models.DecimalField(decimal_places=1, max_digits=3)

    def __str__(self): 
        return self.title
    
class Booking(models.Model):
    housing = models.ForeignKey(Housing,on_delete=models.CASCADE,related_name='bookings')
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='bookings')
    start_time = models.DateField(null=False,blank=False)
    end_time = models.DateField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"booking for housing : {self.housing.title}"
    
class Image(models.Model):
    image = models.ImageField(upload_to='images')
    
    # def __str__(self):
    #     title = self.image.housings.all()[0].images.all().get(self.pk)
    #     return f'{self.image.housings.all()[0].images.all()}  '
    
