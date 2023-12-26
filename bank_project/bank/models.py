from django.db import models


# Create your models here.


class Examble(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    number = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    materials = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    branches = models.CharField(max_length=100)
    account = models.CharField(max_length=100)

    def __str__(self):
        return self.name
