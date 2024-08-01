from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """Reservation Admin Model"""

    list_display = [
        'room',
        'status',
        'check_in',
        'check_out',
        'guest',
        'in_progress',
        'is_finished',
    ]
    list_filter = ['status']

    @admin.display(boolean=True)
    def in_progress(self, obj: models.Reservation) -> bool:
        return obj.in_progress()

    @admin.display(boolean=True)
    def is_finished(self, obj: models.Reservation) -> bool:
        return obj.is_finished()
