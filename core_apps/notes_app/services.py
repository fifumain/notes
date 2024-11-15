from django_redis import get_redis_connection
from rest_framework.exceptions import ValidationError

from .models import Note
from .serializers import NoteSerializer

"""List of simple srvice functions for view file"""


def get_note_by_id(note_id, user):
    return Note.objects.get(id=note_id, user=user)


def get_cached_notes(user):
    redis_conn = get_redis_connection("default")
    cache_key = f"user_notes_{user.id}"
    cached_notes = redis_conn.get(cache_key)

    if cached_notes:
        return eval(cached_notes)

    notes = Note.objects.filter(user=user)
    serializer = NoteSerializer(notes, many=True)
    redis_conn.set(cache_key, str(serializer.data), ex=300)
    return serializer.data


def invalidate_notes_cache(user):
    redis_conn = get_redis_connection("default")
    cache_key = f"user_notes_{user.id}"
    redis_conn.delete(cache_key)


def create_note(user, data):
    serializer = NoteSerializer(data=data)
    if serializer.is_valid():
        note = serializer.save(user=user)
        invalidate_notes_cache(user)
        return serializer.data
    raise ValidationError(serializer.errors)


def update_note(user, note_id, data):

    note = Note.objects.filter(user=user, id=note_id).first()
    if not note:
        return None

    serializer = NoteSerializer(note, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        invalidate_notes_cache(user)
        return serializer.data
    raise ValidationError(serializer.errors)


def delete_note(user, note_id):
    note = Note.objects.filter(user=user, id=note_id).first()
    if note:
        note.delete()
        invalidate_notes_cache(user)
        return True
    return False
