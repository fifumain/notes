import pytest
from core_apps.notes_app.admin import NoteAdmin
from core_apps.notes_app.models import Note
from django.contrib.admin.sites import site
from django.contrib.auth.models import User
from django.test import Client, RequestFactory


@pytest.mark.django_db
def test_save_model_method():
    """save_model admin panel test"""

    # Создаем пользователей
    user = User.objects.create_user(username="testuser", password="password")
    new_user = User.objects.create_user(username="newuser", password="newpassword")

    # Создаем заметку
    note = Note.objects.create(user=user, title="Test Note", content="Some content")

    # Создаем объект NoteAdmin
    admin = NoteAdmin(Note, site)

    # Создаем фейковый запрос для эмуляции нового пользователя в request.user
    request = RequestFactory().get("/admin/notes_app/note/add/")
    request.user = new_user  # Эмулируем, что запрос был от нового пользователя

    # Вызываем save_model с фейковым запросом
    admin.save_model(request, note, None, None)

    # Проверяем, что пользователь заметки обновился
    note.refresh_from_db()
    assert note.user == new_user
