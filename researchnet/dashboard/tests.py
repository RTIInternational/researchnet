from django.test import TestCase
from django.core.mail import send_mail
from django.conf import settings

# Create your tests here.


class SendEmail(TestCase):
  
    def test_email(self):
    	send_mail('Whoa, this thing works', 'Here is the message.', 'researchnet@ictedge.org', ['apreston@rti.org'], fail_silently=False)

    def test_confirm_settings(self):
    	self.assertIsNotNone(settings.EMAIL_HOST)
    	self.assertTrue(settings.EMAIL_HOST_USER)
    	self.assertTrue(settings.EMAIL_HOST_PASSWORD)
    	self.assertIsNotNone(settings.EMAIL_PORT)
    	self.assertIsNotNone(settings.EMAIL_USE_TLS)