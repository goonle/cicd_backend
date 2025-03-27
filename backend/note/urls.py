from django.urls import path, include

from .views import NoteViewManual#, NoteGetOneView

# router = DefaultRouter()
# router.register(r'notes', NoteViewSet)
# urlpatterns = router.urls

urlpatterns = [
    path('', NoteViewManual.as_view(), name='create'),
    # path('note/<int:note_id>/', NoteGetOneView.as_view(), name='note-get-one'),
]
