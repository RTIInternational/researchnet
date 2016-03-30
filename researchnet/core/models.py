from datetime import datetime
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Submission(models.Model):
    user = models.ForeignKey(User)
    time_start = models.DateTimeField(default=datetime.now)
    time_complete = models.DateTimeField(default=datetime.now)
    timestamp = models.DateTimeField(db_index=True, auto_now_add=True)
    device_id = models.TextField()
    long = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    response = JSONField()


# a profile model
class Participant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.TextField()
    dob = models.DateField(blank=True, null=True)

class Consent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    scope = models.TextField()
    imageData = models.ImageField(blank=True)
    consent_date = models.DateTimeField(default=datetime.now)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
