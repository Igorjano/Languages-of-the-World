import json

from django.db import models


class Languages(models.Model):
    name = models.CharField(max_length=100)
    sign = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=100)
    sign = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Countries(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2048)
    capital = models.CharField(max_length=100)
    population = models.IntegerField(default=0)
    lat = models.IntegerField(default=0)
    long = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, null=True, on_delete=models.SET_NULL)


class LanguagesByCountries(models.Model):
    country = models.ForeignKey(Countries, null=True, on_delete=models.SET_NULL)
    language = models.ForeignKey(Languages, null=True, on_delete=models.SET_NULL)





