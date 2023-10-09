from django.db import models


class Manufacturer(models.Model):
    # ...
    pass


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    instrument = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.last_name.__len__() > 0:
            return f"{self.first_name} {self.last_name}"
        return f"{self.first_name}"


    def save(self, *args, **kwargs):
        self.first_name = self.first_name[0].upper() + self.first_name[1:]
        if self.last_name.__len__() > 0:
            self.last_name = self.last_name[0].upper() + self.last_name[1:]

        super().save(*args, **kwargs)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name="albums")
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name