from django.forms import ValidationError
from rest_framework import status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import NoteSerializer
from .services import (
    create_note,
    delete_note,
    get_cached_notes,
    get_note_by_id,
    update_note,
)


class NoteViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        notes = get_cached_notes(request.user)
        return Response(notes, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            note = create_note(request.user, request.data)
            return Response(note, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):

        note = get_note_by_id(user=request.user, note_id=pk)
        if note:
            return Response(NoteSerializer(note).data, status=status.HTTP_200_OK)

        raise NotFound(detail="Note not found.")

    def update(self, request, pk=None):

        updated_note = update_note(request.user, pk, request.data)
        if updated_note:
            return Response(updated_note, status=status.HTTP_200_OK)

        raise NotFound(detail="Note not found.")

    def destroy(self, request, pk=None):
        success = delete_note(request.user, pk)
        if success:
            return Response(
                {"detail": "Note deleted."}, status=status.HTTP_204_NO_CONTENT
            )

        raise NotFound(detail="Note not found.")
