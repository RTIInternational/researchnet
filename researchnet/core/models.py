from django.db import models
from django.contrib.postgres.fields import JSONField


class Submission(models.Model):
    username = models.TextField()
    timestamp = models.DateTimeField(db_index=True)
    device_id = models.TextField()
    response = JSONField()


