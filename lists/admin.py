from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    """List Admin Model"""

    list_display = ['name', 'user', 'count_rooms']
    search_fields = ['name']
    filter_horizontal = ['rooms']
    autocomplete_fields = ['user']

    @admin.display(description='Number of Rooms')
    def count_rooms(self, obj: models.List) -> int:
        return obj.count_rooms()
