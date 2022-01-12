from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default="default_pic.png", upload_to='users/')