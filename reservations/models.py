from django.db import models
from django.utils import timezone
from core import models as core_models
from rooms import models as rooms_models
from users import models as users_models


class Reservation(core_models.TimeStampedModel):
    """Reservation Model"""

    class Status(models.TextChoices):
        PENDING = 'pe', 'Pending'
        CONFIRMED = 'co', 'Confirmed'
        CANCELED = 'ca', 'Canceled'

    guest = models.ForeignKey(
        users_models.User,
        on_delete=models.CASCADE,
        related_name='reservations',
    )
    room = models.ForeignKey(
        rooms_models.Room,
        on_delete=models.CASCADE,
        related_name='reservations',
    )
    status = models.CharField(max_length=2, choices=Status, default=Status.PENDING)
    check_in = models.DateField()
    check_out = models.DateField()

    def in_progress(self) -> bool:
        now = timezone.now().date()
        return self.check_in <= now <= self.check_out

    def is_finished(self) -> bool:
        now = timezone.now().date()
        return now > self.check_out

    def __str__(self) -> str:
        return f'{self.room} - {self.check_in}'
