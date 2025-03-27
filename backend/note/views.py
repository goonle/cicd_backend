from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Note

class NoteViewManual(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        user = request.user
        title = request.data.get('title')
        content = request.data.get('content')

        if not title or not content:
            return Response({"error": "Title and content are required"}, status=status.HTTP_400_BAD_REQUEST)

        note = Note.objects.create(user=user, title=title, content=content)
        return Response({"message": "Note created successfully", "note_id": note.id}, status=status.HTTP_201_CREATED)

    def put(self, request):
        note = Note.objects.get(id=request.data.get("note_id"))
        note.title = request.data.get('title', note.title)
        note.content = request.data.get('content', note.content)
        note.save()

        return Response({"message": "Note updated successfully"}, status=status.HTTP_200_OK)

    def delete(self, request):
        note = get_object_or_404(Note, id=request.data.get("note_id"))
        note.delete()
        return Response({"message": "Note deleted successfully"}, status=status.HTTP_200_OK)