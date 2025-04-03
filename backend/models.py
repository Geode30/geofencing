from django.contrib.gis.db import models

class OfficeLocation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    radius_meter = models.IntegerField(default=50)