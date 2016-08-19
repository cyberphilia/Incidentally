from django.contrib import admin

# Register your models here.
from .models import Manufacturer,Device,MAC,Ip


admin.site.register(Manufacturer)
admin.site.register(Device)
admin.site.register(MAC)
admin.site.register(Ip)
