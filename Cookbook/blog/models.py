from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    objects = models.Manager()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"title": self.slug})
        # return f"/blog/{self.pk}"
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    