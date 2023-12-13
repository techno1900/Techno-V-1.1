from django.db import models
from django.db.models.signals import post_save

from django.conf import settings
from django.core.mail import send_mail

class contactTable(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=2000)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
    


def contactEmail(sender, instance, created, **kwargs):
    if created:
        user = instance
        email = user.email  
        subject = 'welcome to techno'
        message = 'thank you for reaching us we will contact you soon'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )




post_save.connect(contactEmail, sender=contactTable)