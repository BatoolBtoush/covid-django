from django.db import models


class CountryData(models.Model):
    country = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.country
