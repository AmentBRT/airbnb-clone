from django.db import models
from core import models as core_models
from users import models as users_models


class Conversation(core_models.TimeStampedModel):
    """Conversation Model"""

    participants = models.ManyToManyField(users_models.User, blank=True)

    def __str__(self) -> str:
        return str(self.created_at)


class Message(core_models.TimeStampedModel):
    """Message Model"""

    user = models.ForeignKey(users_models.User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self) -> str:
        return f'{self.user} says: {self.message}'
