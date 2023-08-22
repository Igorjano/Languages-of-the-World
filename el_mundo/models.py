from django.db import models
import json


class Languages(models.Model):
    name = models.CharField(max_length=100)
    sign = models.CharField(max_length=100)


class Currency(models.Model):
    name = models.CharField(max_length=100)
    sign = models.CharField(max_length=100)


class Countries(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2048)
    capital = models.CharField(max_length=100)
    population = models.IntegerField(default=0)
    lat = models.IntegerField(default=0)
    long = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, null=True, on_delete=models.SET_NULL)


class LanguageCountry(models.Model):
    country = models.ForeignKey(Countries, null=True, on_delete=models.SET_NULL)
    language = models.ForeignKey(Languages, null=True, on_delete=models.SET_NULL)





