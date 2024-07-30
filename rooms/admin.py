from django.contrib import admin
from . import models


@admin.register(models.RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    """Room Type Admin Model"""


@admin.register(models.Amenity)
class AmenityAdmin(admin.ModelAdmin):
    """Amenity Admin Model"""


@admin.register(models.Facility)
class FacilityAdmin(admin.ModelAdmin):
    """Facility Admin Model"""


@admin.register(models.HouseRule)
class HouseRule(admin.ModelAdmin):
    """House Rule Admin Model"""


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Model"""


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Model"""
