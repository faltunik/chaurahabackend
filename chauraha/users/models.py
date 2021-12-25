from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

BRANCH_CHOICES = [
    ("ARCH", "ARCH"),
    ("BME", "BME"),
    ("BIOTECH", "BIOTECH"),
    ("CHEM", "CHEM"),
    ("CIVIL", "CIVIL"),
    ("CSE", "CSE"),
    ("ECE", "ECE"),
    ("EE", "EE"),
    ("IT", "IT"),
    ("MECH", "MECH"),
    ("META", "META"),
    ("MINING", "MINING"),
    ]

class CustomUser(AbstractUser):
    email = models.EmailField(unique= True)
    branch = models.CharField(
        max_length = 20,
        choices = BRANCH_CHOICES,
        default = 'ARCH',
        unique= False
        )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.username

