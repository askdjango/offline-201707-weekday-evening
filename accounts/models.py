from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)  # 'auth.User'
    phone = models.CharField(max_length=11)
    addr = models.CharField(max_length=50)

