from datetime import timedelta

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django_redis import get_redis_connection
from rest_framework_simplejwt.tokens import RefreshToken


@receiver(user_logged_in)
def store_tokens_in_redis(sender, request, user, **kwargs):
    """Realisation for the 'Store token data in Redis for session management'"""
    print(f"User {user.username} logged in successfully.")

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    redis_conn = get_redis_connection("default")

    redis_conn.set(
        f"user:{user.id}:access_token", access_token, ex=timedelta(minutes=30)
    )
    redis_conn.set(f"user:{user.id}:refresh_token", refresh_token, ex=timedelta(days=1))
