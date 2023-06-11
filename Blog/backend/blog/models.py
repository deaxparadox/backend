from django.db import models
from django.urls import reverse
from django.utils import timezone


class Status(models.TextChoices):
    DRAFT = "DF", "Draft"
    PUBLISHED = "PB", "Published"

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    status = models.TextField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["-published"]

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"id": self.id, "slug": self.slug})
    