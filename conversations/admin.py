from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Conversation Admin Model"""

    list_display = ['__str__', 'count_messages', 'count_participants']
    filter_horizontal = ['participants']

    @admin.display(description='Number of Messages')
    def count_messages(self, obj: models.Conversation) -> int:
        return obj.count_messages()

    @admin.display(description='Number of Participants')
    def count_participants(self, obj: models.Conversation) -> int:
        return obj.count_participants()


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """Message Admin Model"""

    list_display = ['__str__', 'created_at']
