from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.forms import SplitDateTimeWidget
from  . import models
# SplitDateTimeField
class BookingForm(ModelForm):
    class Meta:
        model = models.Booking
        fields = (
            "start_time",
            'end_time',
        )
        widgets ={
            "start_time" :AdminDateWidget,
            "end_time" :AdminDateWidget,
        }
