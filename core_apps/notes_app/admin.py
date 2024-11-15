from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):

    list_display = ("user", "title", "content", "created_at", "updated_at")

    list_filter = ("created_at", "updated_at")

    search_fields = ("title", "content")

    fields = ("user", "title", "content")

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Note, NoteAdmin)
