from django.contrib import admin

from asteroid.models import Sighting


@admin.register(Sighting)
class SightingAdmin(admin.ModelAdmin):
    list_display = ("id", "observatory_code", "device_matrix", "device_matrix_clear", "date", "time", "device_code",
                    "device_resolution")
    ordering = ("-date",)
