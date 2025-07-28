from django.db import models

# Create your models here.
class Student(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)
    age = models.CharField(max_length=200)