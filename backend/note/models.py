from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status_item = [
        (1, 'To Do'),
        (2, 'In Progress'),
        (3, 'Done'),
    ]
    status = models.IntegerField(choices=status_item, default=1)

    def __str__(self):
        return self.title