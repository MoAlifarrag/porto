from django.db import models

# Create your models here.
class Envoytable(models.Model):
    Id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Count = models.IntegerField(default=0)

class StreetData(models.Model):
    pass