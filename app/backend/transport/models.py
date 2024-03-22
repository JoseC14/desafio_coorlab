from django.db import models


class Transport(models.Model):
    id = models.IntegerField().primary_key
    name = models.CharField(max_length=150)
    price_confort = models.CharField(max_length=9)
    price_econ = models.CharField(max_length=9)
    city = models.CharField(max_length=150)
    duration = models.CharField(max_length=3)
    seat = models.CharField(max_length=3)
    bed = models.CharField(max_length=2)
