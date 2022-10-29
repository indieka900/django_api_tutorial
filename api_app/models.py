from django.db import models


class Advocate(models.Model):
    username = models.CharField(max_length=60)
    bio = models.TextField(max_length = 300, null = True, blank=True)
    
    def __str__(self):
        return self.username
# Create your models here.
