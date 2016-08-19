"""
Devices Models
"""

from django.db import models


class Manufacturer(models.Model):
    """
    Manufacturer Model
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name[:50]


class Device(models.Model):
    """
    Device Model
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    operating_system = models.CharField(max_length=30, blank=True)
    virtualized = models.BooleanField(default=False)
    model = models.CharField(max_length=30, blank=True)
    users = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.name[:50]


class MAC(models.Model):
    """
    MAC Model
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=30)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    def __str__(self):
        return self.address


class Ip(models.Model):
    """
    An history of IPs associated with a Device
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    address = models.GenericIPAddressField()
    mac = models.ForeignKey(MAC, on_delete=models.CASCADE)
    def __str__(self):
        return self.address

class Hostname(models.Model):
    """docstring for hostname"""
    name = models.CharField(max_length=30, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
        