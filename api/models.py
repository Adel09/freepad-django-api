from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=80, blank=True)
    phone = models.CharField(max_length=80, blank=True)
    image = models.FileField(null=True, upload_to="profile/", default="media/profile/placeholder.png")
    city = models.CharField(max_length=80, blank=True)
    state = models.CharField(max_length=80, blank=True)
    pharmacy = models.CharField(max_length=90, blank=True)
    people_helped = models.IntegerField(default=0)
    wallet = models.DecimalField(max_digits=7, default=0.00, decimal_places=2)



class PadRequest(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, blank=True)
    title = models.CharField(max_length=80, blank=True)
    quantity = models.IntegerField(default=1)
    donated = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    city = models.CharField(max_length=80, blank=True)
    state = models.CharField(max_length=80, blank=True)
    pharmacy = models.CharField(max_length=90, blank=True)

