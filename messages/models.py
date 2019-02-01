import uuid

from django.db import models

from bots.models import Bot


class Message(models.Model):

    class Meta:
        db_table = 'bots_messages'

    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
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

    # from is a reserved word
    from_ = None
    to    = None

    @classmethod
    def from_db(cls, db, field_names, values):
        message = super().from_db(db, field_names, values)
        if message.direction == 'F':
            message.from_ = message.bot
            message.to = message.client
        else:
            message.to = message.bot
            message.from_ = message.client
        return message

    def save(self, *args, **kwargs):
        try:
            b = Bot.objects.get(id=self.from_)
            self.bot = b
            self.direction = 'F'
            self.client = self.to
        except Bot.DoesNotExist:
            try:
                b = Bot.objects.get(id=self.to)
                self.bot = b
                self.direction = 'T'
                self.client = self.from_
            except Bot.DoesNotExists:
                raise ValueError("Bot not found")
        super().save(*args, **kwargs)
