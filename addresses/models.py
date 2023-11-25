import geocoder
from django.db import models

# Rest of your model code


# Create your models here.

access_token = 'pk.eyJ1Ijoic29oYW1wYW4yNCIsImEiOiJjbG1ydjhsdTMwOXpqMmxwOTk0N3Vuc25sIn0.SWJt_UOZ69_P_ToW6mZVqA'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=access_token)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        super(Address, self).save(*args, **kwargs)
