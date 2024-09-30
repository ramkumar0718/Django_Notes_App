from django.db import models
from django.contrib.auth.models import User

COLOR_CHOICES = [
    ('#808080', 'Grey'),
    ('#FF0000', 'Red'),
    ('#00FF00', 'Green'),
    ('#0000FF', 'Blue'),
    ('#FFFF00', 'Yellow'),
    ('#FFA500', 'Orange'),
    ('#800080', 'Purple'),
    ('#000000', 'Black'),
]

class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=8, choices=COLOR_CHOICES, default='#808080')

    def __str__(self):
        return self.title + "\n" + self.description
