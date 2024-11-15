import pytest
from core_apps.notes_app.models import Note
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_note_str_method():
    """test __str__  Note model"""

    user = User.objects.create_user(username="testuser", password="password")

    note = Note.objects.create(
        user=user, title="Test Note", content="This is a test note content."
    )

    assert str(note) == "Test Note"
