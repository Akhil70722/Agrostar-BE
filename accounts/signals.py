from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # If you have a profile model, create it here; otherwise remove this
        pass

@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    # instance.profile.save()  # Only if you have a profile model
    pass
