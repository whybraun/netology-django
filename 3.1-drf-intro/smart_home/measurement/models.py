from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)