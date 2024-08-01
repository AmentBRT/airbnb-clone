from django.db import models
from core import models as core_models
from users import models as users_models


class Conversation(core_models.TimeStampedModel):
    """Conversation Model"""

    participants = models.ManyToManyField(
        users_models.User,
        related_name='conversations',
        blank=True,
    )

    def count_messages(self) -> int:
        return self.messages.count()

    def count_participants(self) -> int:
        return self.participants.count()

    def __str__(self) -> str:
        users = self.participants.all()
        usernames = map(lambda u: u.username, users)
        return ', '.join(usernames)


class Message(core_models.TimeStampedModel):
    """Message Model"""

    user = models.ForeignKey(
        users_models.User,
        on_delete=models.CASCADE,
        related_name='messages',
    )
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages',
    )
    message = models.TextField()

    def __str__(self) -> str:
        return f'{self.user} says: {self.message}'
