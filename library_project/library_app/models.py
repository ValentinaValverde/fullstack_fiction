from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField(null=True)
    author = models.TextField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title