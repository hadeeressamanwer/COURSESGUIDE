from django.db import models


class Languages(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    place = models.CharField(max_length=255)
    description = models.CharField(max_length=2083)
    image_url = models.CharField(max_length=2083)


class Technical(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    place = models.CharField(max_length=255)
    description = models.CharField(max_length=2083)
    image_url = models.CharField(max_length=2083)


class Music(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    place = models.CharField(max_length=255)
    description = models.CharField(max_length=2083)
    image_url2 = models.CharField(max_length=2083)





