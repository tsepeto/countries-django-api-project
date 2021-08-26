from django.db import models


class Country(models.Model):
    """Class model for countries - first level"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    type = models.CharField(max_length=50, blank=False, default='Country', editable=False)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
	    return self.name


class Region(models.Model):
    """Class model for Regions - second level"""
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, unique=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    type = models.CharField(max_length=50, blank=False, default='Region', editable=False)

    def __str__(self):
	    return self.name


class City(models.Model):
    """Class model for Cities - third level"""
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, unique=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    type = models.CharField(max_length=50, blank=False, default='City', editable=False)
    
    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
	    return self.name