# myapp/models.py
from django.db import models

class MyModel(models.Model):
    value = models.CharField(max_length=255, null=True)
