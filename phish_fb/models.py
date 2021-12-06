from django.db import models

# Create your models here.
class Victim(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(null =False)
    password =models.TextField(null=False)
    date = models.DateTimeField('Date')
    