from django.db import models

from .relationships .fk import Musician, Album

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

    def save(self, *args, **kwargs):
        self.first_name = self.first_name[0].upper() + self.first_name[1:]
        self.last_name = self.last_name[0].upper() + self.last_name[1:]
        super().save(*args, **kwargs)
