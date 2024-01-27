import datetime
from datetime import (
    datetime, time, date
)
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 


class Heading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="heading")
    description = models.TextField(null=True, blank=True)
    note = models.CharField(max_length=120, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    # managers
    objects = models.Manager()


    def __str__(self) -> str:
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse("pms:update_heading_view", kwargs={"id": self.pk})
    
    
    def get_update_url(self):
        return reverse("pms:update_heading_view", kwargs={"id": self.pk})
    
    def get_detail_url(self):
        return reverse("pms:detail_heading_view", kwargs={"id": self.pk})
    
    @staticmethod
    def get_create_url():
        return reverse("pms:create_heading_view")
    
    def add_user(self, user: User | None = None) -> User:
        self.user = user 
        return user