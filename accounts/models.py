from django.db import models


class User(models.Model):
    username = models.CharField(max_length=36)
    fullName = models.TextField()
    password = models.TextField()
    email = models.EmailField(max_length=254)
    phoneNumber = models.IntegerField()
