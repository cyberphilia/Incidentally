from django.contrib import admin

# Register your models here.
from .models import Manufacturer
from .models import Device

admin.site.register(Manufacturer)
admin.site.register(Device)
