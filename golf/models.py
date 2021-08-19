from django.db import models

# Create your models here.

class Fieldscore(models.Model):
    club = models.TextField(default=0)
    year = models.IntegerField(default=0)
    date = models.DateField(default=0)
    score = models.IntegerField(default=0)
    companion1 = models.TextField(default=0)
    companion2 = models.TextField(default=0)
    companion3 = models.TextField(default=0)