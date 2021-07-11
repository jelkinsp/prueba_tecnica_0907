from django.contrib import admin

from asteroid.models import Observatory, Device, Asteriod


@admin.register(Observatory)
class ObservatoryAdmin(admin.ModelAdmin):
    list_display = ("id", "observatory_code", "name")
    ordering = ("-id",)

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("id", "device_code", "device_resolution")
    ordering = ("-id",)

@admin.register(Asteriod)
class AsteriodAdmin(admin.ModelAdmin):
    list_display = ("id", "device_matrix", "date", "time")
    ordering = ("-time",)

