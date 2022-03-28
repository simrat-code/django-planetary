from django.db import models

#
# CharField     : "short text"
# TextField     : "long text summary..."
# EmailField    : "emailaddr@example.com"
# URLField      : "www.example.com"
#
# IntegerField  : -1, 0, 1, 2, ...
# DecimalField  : 3.14
#
# BooleanField  : True, False
# DateTimeField : datetime()
#
# ForeignKey    : 1 (id of record to another table)
# ManyToManyField: NA
#

class Planet(models.Model):
    planet_id = models.IntegerField(primary_key=True)
    planet_name = models.CharField(max_length=24, unique=True)
    planet_type = models.CharField(max_length=2, default='NA')
    home_star = models.CharField(max_length=24)
    mass = models.DecimalField(max_digits=19, decimal_places=10)
    radius = models.DecimalField(max_digits=19, decimal_places=10)
    distance = models.DecimalField(max_digits=19, decimal_places=10)


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    email = models.EmailField()
    password = models.CharField(max_length=32)
