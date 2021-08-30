from django.db import models


class TimeStampedModel(models.Model):
    
    """Time Stamped Model"""
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    # this indicated this model will not made on database by itself.
    # this model is abstract model
    class Meta:
        abstract = True