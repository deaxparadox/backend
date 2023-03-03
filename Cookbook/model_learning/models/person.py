from django.db import models

class BasePerson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        abstract = True 

# class Person(BasePerson):
#     SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )
#     name = models.CharField(max_length=60)
#     shirt_size = models.CharField(
#         max_length=1,
#         choices=SHIRT_SIZES
#     )

#     def __str__(self):
#         return self.first_name

class Musician(BasePerson):
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Album(models.Model):
    artist = models.ForeignKey(
        Musician,
        related_name='albums',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=100
    )
    release_date = models.DateField(auto_now_add=True)
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name
    