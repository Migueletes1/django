from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    email = models.EmailField(max_length=30, null=True)
    gener = models.CharField(
        max_length=1, choices=[("M", "Male"), ("F", "Female")], null=True
    )
    birth_date = models.DateField(null=True)


# Create your models here.
