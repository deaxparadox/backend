from django.db import models
from django.urls import reverse

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CUser(AbstractUser):
    date = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # def get_absolute_url(self):
    #     return reverse("user_profile", kwargs={"pk": self.pk})
    
    