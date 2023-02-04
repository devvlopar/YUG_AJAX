from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.
class AllUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=13)

    def __str__(self):
        return self.name
    

