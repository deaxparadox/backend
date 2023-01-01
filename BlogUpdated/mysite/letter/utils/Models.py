from django.db import models

class LetterBase(models.Model):
    title = models.CharField(max_length=30)
    subject = models.CharField(max_length=120, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True     