from django.db import models

# Create your models here.


class Person(models.Model):
    username = models.CharField(db_index=True, max_length=256, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)


class Organization(models.Model):
    name = models.CharField(max_length=256)
    created_date = models.DateField(auto_now=True)