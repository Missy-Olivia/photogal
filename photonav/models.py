from django.db import models
import datetime as dt

class Category(models.Model):
    name = models.CharField(max_length =50)