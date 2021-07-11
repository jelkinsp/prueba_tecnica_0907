import uuid

from django.db import models


class Observatory(models.Model):
    id = models.URLField(primary_key=True, default=uuid.uuid4(), editable=False)
    observatory_code = models.CharField(max_length=32, unique=True, null=False, blank=False)
    name = models.CharField(max_length=32, null=False, blank=False)


class Device(models.Model):
    id = models.URLField(primary_key=True, default=uuid.uuid4(), editable=False)
    device_code = models.CharField(max_length=32, unique=True, null=False, blank=False)
    device_resolution = models.CharField(max_length=5, null=False, blank=False)
    observatories = models.ManyToManyField(Observatory)


class Asteriod(models.Model):
    id = models.URLField(primary_key=True, default=uuid.uuid4(), editable=False)
    device_matrix = models.CharField(max_length=64, null=False, blank=False, unique=True)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    devices = models.ManyToManyField(Device)
