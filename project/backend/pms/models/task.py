from collections.abc import Iterable
from django.db import models
from django.dispatch import receiver, Signal
from django.db.models.signals import pre_save
from django.urls import reverse

from .heading import Heading

# task_date_exceed_heading = Signal()

class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    note = models.CharField(max_length=120, null=True, blank=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    def end_bound(self):
        """
        This function checks, 
        whether task task end start exceeding headings end date.

        If task date exceeds headings end date, if return True, 
        else return False.
        """
        return self.end > self.heading.end
    
    def get_absolute_url(self):
        return reverse("pms:detail_task_view", kwargs={"id": self.pk})
    
    def get_update_url(self):
        return reverse("pms:update_task_view", kwargs={"id": self.pk})

    @staticmethod
    def get_create_url():
        return reverse("pms:create_task_view")
    
    def save(self, *args, **kwargs) -> None:
        return super().save(*args, **kwargs)
    