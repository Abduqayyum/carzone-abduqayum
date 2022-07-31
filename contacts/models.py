from datetime import datetime
from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    car_id = models.IntegerField(blank=True)
    customer_need = models.CharField(max_length=120)
    car_title = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=120)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email