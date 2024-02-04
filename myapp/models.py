from django.db import models

# Create your models here.
class Book(models.Model):
    Name=models.CharField(max_length=150)
    author=models.CharField(max_length=150)

    def __str__(self):
        return self.Name