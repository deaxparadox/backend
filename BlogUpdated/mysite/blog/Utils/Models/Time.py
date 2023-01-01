from django.db import models 

class Created(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True 

class Updated(Created):
    updated = models.DateTimeField(auto_now=True)
    