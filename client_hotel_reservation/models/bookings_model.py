import uuid
from .rooms_model import Room
# from django.contrib.auth.models import User
from django.db import models

class Booking(models.Model):
    uid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    # user = models.ForeignKey(User , on_delete= models.CASCADE, null=True)
    rooms = models.ForeignKey(Room , on_delete= models.CASCADE, null=True)
    booking_name = models.CharField(max_length=255, null=True)
    phone_num = models.CharField(max_length=15, null=True)
    no_of_guest = models.IntegerField(null=True)
    description = models.TextField(null=True)
    
    class Meta:
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return str(self.booking_name)
