from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Model"""

    list_display = ['name', 'used_by']
    search_fields = ['name']

    @admin.display(ordering='rooms')
    def used_by(self, obj) -> int:
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):
    """Photo Inline Model"""

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Model"""

    inlines = [PhotoInline]
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
        'total_rating',
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
    autocomplete_fields = ['host', 'room_type']

    @admin.display(ordering='amenities')
    def amenities_count(self, obj: models.Room) -> int:
        return obj.amenities.count()

    @admin.display(ordering='photos')
    def photos_count(self, obj: models.Room) -> int:
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Model"""

    list_display = ['__str__', 'get_thumbnail']
    autocomplete_fields = ['room']

    @admin.display(description='Thumbnail')
    def get_thumbnail(self, obj: models.Photo) -> str:
        return mark_safe(f'<img width=50px src="{obj.file.url}"/>')
