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

    fieldsets = (
        (
            'Basic Info',
            {'fields': ('name', 'description', 'country', 'city', 'price', 'address')},
        ),
        (
            'Times',
            {'fields': ('check_in', 'check_out', 'instant_book')},
        ),
        (
            'Spaces',
            {'fields': ('guests', 'beds', 'bedrooms', 'baths')},
        ),
        (
            'More about the space',
            {
                'classes': ('collapse',),
                'fields': ('amenities', 'facilities', 'house_rules'),
            },
        ),
        (
            'Last details',
            {'fields': ('host',)},
        ),
    )
    list_display = [
        'name',
        'country',
        'city',
        'price',
        'guests',
        'beds',
        'bedrooms',
        'baths',
        'check_in',
        'check_out',
        'instant_book',
        'amenities_count',
        'photos_count',
    ]
    list_filter = [
        'instant_book',
        'host__superhost',
        'room_type',
        'amenities',
        'facilities',
        'house_rules',
        'city',
        'country',
    ]
    search_fields = ['city', '^host__username']
    filter_horizontal = ['amenities', 'facilities', 'house_rules']

    @admin.display(ordering='amenities')
    def amenities_count(self, obj: models.Room):
        return obj.amenities.count()

    @admin.display(ordering='photos')
    def photos_count(self, obj: models.Room):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Model"""
