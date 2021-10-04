from django.db import models


class UserT(models.Model):
    name = models.TextField(max_length=36)
    surname = models.TextField(max_length=36)
    login = models.CharField(max_length=36)
    password = models.CharField(max_length=8)
    telephone = models.CharField(max_length=36)
    picture = models.CharField(max_length=36)
    mail = models.CharField(max_length=36)
    address = models.CharField(max_length=36)
    country = models.CharField(max_length=36)

class Lemodele(models.Model):
    col = models.CharField(max_length=36)