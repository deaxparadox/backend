from django.db import models

class Base(models.Model):
    name: models.CharField = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Manufacturer(models.Model):
    pass 

class Car(Base):
    manufacturer: models.ForeignKey = models.ForeignKey(
        Manufacturer, 
        related_name="manufacturer",
        on_delete=models.CASCADE
    )