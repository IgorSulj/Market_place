from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AccountsUser(AbstractUser):
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=50, db_index=True, blank=True)
