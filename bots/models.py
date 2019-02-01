import uuid

from django.db import models


class Bot(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=65535)

