from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PastOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    order_id = models.IntegerField(unique=True)
    order_placed_at=models.DateTimeField()
    mobile_number=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    total_payment=models.DecimalField(max_digits=10,decimal_places=2)
    payment_id=models.CharField(max_length=100)

class OrderItem(models.Model):
    order=models.ForeignKey(PastOrder,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=100)
    quantity=models.IntegerField()

class TableBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_number=models.CharField(max_length=12)
    booking_date=models.DateField()
    booking_time=models.TimeField()
    number_of_people=models.IntegerField()
