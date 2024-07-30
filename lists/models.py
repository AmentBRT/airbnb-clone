from django.db import models
from core import models as core_models
from rooms import models as rooms_models
from users import models as users_models


class List(core_models.TimeStampedModel):
    """List Model"""

    user = models.ForeignKey(users_models.User, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(rooms_models.Room, blank=True)
    name = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.name
