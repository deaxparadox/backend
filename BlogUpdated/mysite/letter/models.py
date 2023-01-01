from django.db import models
from django.urls import reverse

from .utils.Models import LetterBase



class SentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Letter.Status.SENT)

class PendingManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Letter.Status.PENDING)

class TravelingManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Letter.Status.TRAVELING)

class DeliveredManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Letter.Status.DELIVERED)

class Letter(LetterBase):
    class Status(models.TextChoices):
        PENDING = "PND", "Pending"
        SENT = "SNT", "Sent"
        TRAVELING = "TRV", "Traveling"
        DELIVERED = "DLV", "Deliered"

    slug = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.PENDING)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    pending = PendingManger()
    sent = SentManager()    
    traveling = TravelingManger()
    delivered = DeliveredManger()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        print(self.slug)
        return reverse("letter:letter_detail", kwargs={"slug": self.slug})
    