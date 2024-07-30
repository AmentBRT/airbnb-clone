from django.db import models
from core import models as core_models
from users import models as users_models
from rooms import models as rooms_models


class Review(core_models.TimeStampedModel):
    """Review Model"""

    user = models.ForeignKey(users_models.User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(rooms_models.Room, on_delete=models.CASCADE)
    review = models.TextField()
    accuracy = models.PositiveSmallIntegerField()
    communication = models.PositiveSmallIntegerField()
    cleanliness = models.PositiveSmallIntegerField()
    location = models.PositiveSmallIntegerField()
    check_in = models.PositiveSmallIntegerField()
    value = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'{self.review} - {self.room}'
