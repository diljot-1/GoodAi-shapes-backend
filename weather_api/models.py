from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    met_office_location_id = models.IntegerField(null=False, blank=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
