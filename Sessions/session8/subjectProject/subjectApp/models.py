from django.db import models

# Create your models here.
class Major(models.Model):
    title= models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Subject(models.Model):
    major = models.ForeignKey(
        "Major", on_delete=models.CASCADE, related_name='subject')
    name = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    Memo = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
