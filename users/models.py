from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    """Custom user model"""
   

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean")
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    
    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW")
    )
    
    
    # default="" or null=True is required for adding some new field to existing model.     # null is for database, blank is for form
    
    avatar = models.ImageField(null=True, blank=True)
    # choices only effect to form so doesn't need to migrage
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio =  models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2,null=True, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3,null=True, blank=True)
    
    superhost = models.BooleanField(default=False)
