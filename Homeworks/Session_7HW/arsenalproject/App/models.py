from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.title
