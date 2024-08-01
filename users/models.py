from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User Model"""

    class Gender(models.TextChoices):
        MALE = 'm', 'Male'
        FEMALE = 'f', 'Female'
        OTHER = 'o', 'Other'

    class Language(models.TextChoices):
        ENGLISH = 'en', 'English'
        PERSIAN = 'fa', 'Persian'

    class Currency(models.TextChoices):
        USD = 'usd', 'USD'
        IRR = 'irr', 'Iran Rial'

    avatar = models.ImageField(upload_to='avatars', null=True, blank=True, default=None)
    gender = models.CharField(
        max_length=1,
        choices=Gender,
        null=True,
        blank=True,
        default=None,
    )
    bio = models.TextField(null=True, blank=True, default=None)
    birthdate = models.DateField(null=True, blank=True, default=None)
    language = models.CharField(
        max_length=2,
        choices=Language,
        null=True,
        blank=True,
        default=None,
    )
    currency = models.CharField(
        max_length=3,
        choices=Currency,
        null=True,
        blank=True,
        default=None,
    )
    superhost = models.BooleanField(default=False)
