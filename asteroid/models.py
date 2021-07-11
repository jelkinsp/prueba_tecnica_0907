import uuid

from django.db import models


class Sighting(models.Model):
    id = models.URLField(primary_key=True, default=uuid.uuid4, editable=False)
    observatory_code = models.CharField(max_length=32, unique=True, null=False, blank=False)
    device_code = models.CharField(max_length=32, unique=True, null=False, blank=False)
    device_resolution = models.CharField(max_length=5, null=False, blank=False)
    device_matrix = models.CharField(max_length=64, null=False, blank=False, unique=True)
    device_matrix_clear = models.CharField(max_length=64, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
