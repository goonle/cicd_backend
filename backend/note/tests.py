from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Note

class NoteViewManualTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='test123')
        self.token = Token.objects.create(user=self.user)
        self.url = '/note/'  # Using the direct RESTful endpoint

    def test_create_note_successfully(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        data = {
            "title": "My Note",
            "content": "This is a test note."
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("note_id", response.data)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.first().title, "My Note")
        print("✅ note.tests.py > Note Create : loaded")

    def test_create_note_missing_fields(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.post(self.url, {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        print("✅ note.tests.py > Note Create : missing fields")

    def test_unauthorized_note_creation(self):
        response = self.client.post(self.url, {"title": "x", "content": "y"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print("✅ note.tests.py > Note Create : unauthorized")

class NoteUpdateTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='test123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create a note to update
        self.note = Note.objects.create(
            user=self.user,
            title="Old Title",
            content="Old Content"
        )

        self.url = '/note/'  # your PUT endpoint

    def test_update_note_successfully(self):
        data = {
            "note_id": self.note.id,
            "title": "Updated Title",
            "content": "Updated Content"
        }

        response = self.client.put(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Note updated successfully")

        # Refresh the note from DB
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Title")
        self.assertEqual(self.note.content, "Updated Content")
        print("✅ note.tests.py > Update Note : updated")

    def test_update_note_partial_fields(self):
        data = {
            "note_id": self.note.id,
            "title": "New Title Only"
        }

        response = self.client.put(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "New Title Only")
        self.assertEqual(self.note.content, "Old Content")  # Unchanged
        print("✅ note.tests.py > Update Note : partial")

    def test_update_note_unauthorized(self):
        self.client.credentials()  # remove auth

        data = {
            "note_id": self.note.id,
            "title": "Hacky Update"
        }

        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print("✅ note.tests.py > Update Note : unauthorized")