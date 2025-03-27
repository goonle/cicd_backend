from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
