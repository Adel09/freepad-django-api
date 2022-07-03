from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=80, blank=True)
    phone = models.CharField(max_length=80, blank=True)
    image = models.FileField(null=True, upload_to="profile/", default="profile/placeholder.png")
    city = models.CharField(max_length=80, blank=True)
    state = models.CharField(max_length=80, blank=True)
    pharmacy = models.CharField(max_length=90, blank=True)
    people_helped = models.IntegerField(default=0)
    wallet = models.DecimalField(max_digits=7, default=0.00, decimal_places=2)

    def __str__(self):
        return f'{self.owner.first_name} {self.owner.last_name}'



class PadRequest(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, blank=True)
    title = models.CharField(max_length=80, blank=True)
    quantity = models.IntegerField(default=1)
    image = models.CharField(max_length=90, blank=True, default="https://complianz.io/wp-content/uploads/2019/03/placeholder-300x202.jpg")
    donated = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    city = models.CharField(max_length=80, blank=True)
    state = models.CharField(max_length=80, blank=True)
    pharmacy = models.CharField(max_length=90, blank=True)

    def __str__(self):
        return self.title

class Donation(models.Model):
    donated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    donated_to = models.ForeignKey(PadRequest, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    when = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return f'Donation by {self.donated_by.first_name} to {self.donated_to}'

