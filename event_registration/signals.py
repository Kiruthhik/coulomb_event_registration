from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Participant

@receiver(post_save, sender=User)
def create_participant_profile(sender, instance, created, **kwargs):
    if created:  # If it's a new user, create a Participant profile
        Participant.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_participant_profile(sender, instance, **kwargs):
    """ Saves the participant profile every time the user is saved """
    if hasattr(instance, 'participant'):
        instance.participant.save()
