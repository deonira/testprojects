from django.db import models
class Book(models.Model):
    author = models.TextField()
    title = models.TextField()
    description = models.TextField()
    def __str__(self):
        return self.title
# Create your models here.

class MediaFile(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

