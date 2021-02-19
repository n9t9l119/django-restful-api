from django.db import models


class Timezones(models.Model):
    country_code = models.CharField(max_length=2)
    timezone_id = models.CharField(max_length=64)
    gmt = models.FloatField()


class GeoNames(models.Model):
    geonameid = models.IntegerField(unique=True)
    name = models.CharField(max_length=64)
    asciiname = models.CharField(max_length=64)
    alternatenames = models.CharField(max_length=256)
    latitude = models.CharField(max_length=64)
    longitude = models.CharField(max_length=256)
    feature_class = models.CharField(max_length=1)
    feature_code = models.CharField(max_length=10)
    country_code = models.CharField(max_length=2)
    cc2 = models.CharField(max_length=200)
    admin1_code = models.CharField(max_length=20)
    admin2_code = models.CharField(max_length=80)
    admin3_code = models.CharField(max_length=20)
    admin4_code = models.CharField(max_length=20)
    population = models.IntegerField(unique=False)
    elevation = models.IntegerField(unique=False, null=True)
    dem = models.IntegerField(unique=False)
    timezone = models.ForeignKey(Timezones, null =True, on_delete=models.SET_NULL)
    modification_date = models.CharField(max_length=40)


class NameId(models.Model):
    name = models.CharField(max_length=384)
    geonameid = models.ForeignKey(GeoNames, on_delete=models.CASCADE)


