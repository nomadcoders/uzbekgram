from django.db import models


class Image(models.Model):

    caption = models.TextField()
    file = models.FileField()
    location = models.CharField(max_length=80)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
