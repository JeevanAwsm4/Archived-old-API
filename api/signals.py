# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Want
from .tasks import delete_expired_data

@receiver(post_save, sender=Want)
def schedule_deletion(sender, instance, **kwargs):
    delete_expired_data.apply_async((instance.id,), countdown=24*60*60)
