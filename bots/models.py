import uuid

from django.db import models


class Bot(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=65535)


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    conversationId = models.UUIDField(null=False, db_index=True)
    timestamp = models.DateTimeField(null=False)
    # Instead of "from" and "to", use "bot", "client" and "direction"
    # That way we don't mix different actors. Save direction to complete the info
    bot = models.ForeignKey(Bot, null=False, on_delete=models.PROTECT)
    MESSAGE_DIRECTION = (
            ('F', 'FROM'),
            ('T', 'TO'),
    )
    direction = models.CharField(null=False, max_length=1, choices=MESSAGE_DIRECTION)
    client = models.UUIDField(null=False)
    text = models.TextField(null=False)
