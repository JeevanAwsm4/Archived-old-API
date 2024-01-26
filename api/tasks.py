# tasks.py
from celery import shared_task
from django.utils import timezone
from .models import Want

@shared_task
def delete_expired_data(instance_id):
    expiration_time = timezone.now() - timezone.timedelta(hours=24)
    Want.objects.filter(created_at__lte=expiration_time).delete()
