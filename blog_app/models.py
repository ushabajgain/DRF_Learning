from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)