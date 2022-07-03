from django.contrib import admin
from .models import Profile, PadRequest, Donation
# Register your models here.
admin.site.register(Profile)
admin.site.register(PadRequest)
admin.site.register(Donation)
