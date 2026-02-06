from django.db import models


class MediaAsset(models.Model):
    title = models.CharField(max_length=160)
    image = models.ImageField(upload_to="media-assets/", blank=True, null=True)
    image_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
