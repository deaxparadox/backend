import datetime
from datetime import (
    datetime, time, date
)
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 


class Heading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="heading")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)


    def __str__(self) -> str:
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse("app:edit_", kwargs={"pk": self.pk})
    
    def add_user(self, user: User | None = None) -> User:
        self.user = user 
        return user