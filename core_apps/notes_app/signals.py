from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django_redis import get_redis_connection

from .models import Note


@receiver(post_save, sender=Note)
def update_cache_after_save(sender, instance, **kwargs):
    redis_conn = get_redis_connection("default")
    redis_conn.delete(f"user_notes_{instance.user.id}")


@receiver(post_delete, sender=Note)
def update_cache_after_delete(sender, instance, **kwargs):
    redis_conn = get_redis_connection("default")
    redis_conn.delete(f"user_notes_{instance.user.id}")
