from django.db import models
from core import models as core_models
from rooms import models as rooms_models
from users import models as users_models


class List(core_models.TimeStampedModel):
    """List Model"""

    user = models.ForeignKey(
        users_models.User,
        on_delete=models.CASCADE,
        related_name='lists',
    )
    rooms = models.ManyToManyField(rooms_models.Room, related_name='lists', blank=True)
    name = models.CharField(max_length=80)

    def count_rooms(self) -> int:
        return self.rooms.count()

    def __str__(self) -> str:
        return self.name
