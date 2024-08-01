from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    """Review Admin Model"""

    list_display = ['__str__', 'rating_average']
    autocomplete_fields = ['user', 'room']

    @admin.display(description='AVG.')
    def rating_average(self, obj: models.Review) -> float:
        return obj.rating_average()
