from django.test import TestCase
from django.core.mail import send_mail
from django.conf import settings

# Create your tests here.


class SendEmail(TestCase):
  
    def test_email(self):
    	send_mail('Whoa, this thing works', 'Here is the message.', 'researchnet@ictedge.org', ['adam704a@hotmail.com'], fail_silently=False)

    def test_confirm_settings(self):
    	self.assertIsNotNone(settings.EMAIL_HOST)
    	self.assertTrue(settings.EMAIL_HOST_USER)
    	self.assertTrue(settings.EMAIL_HOST_PASSWORD)
    	self.assertIsNotNone(settings.EMAIL_PORT)
    	self.assertIsNotNone(settings.EMAIL_USE_TLS)

    def test_print_settings(self):
    	print("EMAIL_HOST: " + str(settings.EMAIL_HOST))
    	print("EMAIL_HOST_USER: " + settings.EMAIL_HOST_USER)
    	print("EMAIL_HOST_PASSWORD: " + settings.EMAIL_HOST_PASSWORD)
    	print("EMAIL_PORT: " + str(settings.EMAIL_PORT))
    	print("EMAIL_USE_TLS: " + str(settings.EMAIL_USE_TLS))