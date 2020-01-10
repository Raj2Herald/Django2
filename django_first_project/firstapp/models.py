from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=10)
    location = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.code} is located at {self.location}"

    def count_arrivals(self):
        return self.arrivals.all().count()


class Flight(models.Model):
    origin = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
    duration = models.IntegerField()
    passengers = models.ManyToManyField(User,blank=True,related_name="flights")
  

    def __str__(self):
        return f"From {self.origin.code} to {self.destination.code} in {self.duration} hrs has {list(self.passengers.all())}" 
    
    def is_valid_flight(self):
        return (self.origin != self.destination) and (self.duration >= 0)