from django.db import models


class WeatherData(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255)
    description = models.CharField(max_length=50)
    temperature = models.FloatField()
    pressure = models.IntegerField()
    icon = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']



