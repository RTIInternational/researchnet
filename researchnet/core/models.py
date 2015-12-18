from datetime import datetime
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


class Submission(models.Model):
    user = models.ForeignKey(User)
    time_start = models.DateTimeField(default=datetime.now)
    time_complete = models.DateTimeField(default=datetime.now)
    timestamp = models.DateTimeField(db_index=True, auto_now_add=True)
    device_id = models.TextField()
    response = JSONField()

class StudyUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    gender = models.TextField()

class Consent(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    scope = models.TextField()
    consent_date = models.DateTimeField(default=datetime.now)

