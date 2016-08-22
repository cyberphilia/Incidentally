from django.contrib import admin

# Register your models here.
from .models import Manufacturer,Device,MAC,Ip,Hostname


admin.site.register(Manufacturer)
# admin.site.register(Device)
# admin.site.register(MAC)
# admin.site.register(Ip)
# admin.site.register(Hostname)

class MacInline(admin.TabularInline):
    model = MAC


class IpInline(admin.TabularInline):
    model = Ip


class HostnameInline(admin.TabularInline):
    model = Hostname


class DeviceAdmin(admin.ModelAdmin):
    inlines = [
        MacInline,HostnameInline,
    ]

class MACAdmin(admin.ModelAdmin):
    inlines = [
        IpInline,
    ]

admin.site.register(Device,DeviceAdmin)
admin.site.register(MAC,MACAdmin)
