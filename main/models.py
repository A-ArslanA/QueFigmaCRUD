from django.db import models


class Post(models.Model):
    name = models.CharField("Name", max_length=255)
    content = models.TextField("Content")
    little_content = models.CharField("littleContent", max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/'
