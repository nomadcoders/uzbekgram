from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):

    caption = models.TextField()
    file = models.FileField()
    location = models.CharField(max_length=80)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} - {}'.format(self.caption, self.location)


class Comment(models.Model):

    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_for = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.comment} - {self.created_for.caption}'


class Like(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    created_for = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.created_by.username} - {self.created_for.caption}'
