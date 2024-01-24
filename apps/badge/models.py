from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class BadgeUser(AbstractBaseUser):
    name = models.CharField(max_length = 30, blank = False)
    email = models.EmailField(unique = True, blank = False)
    birth_date = models.DateTimeField(blank = False)
    phone = models.CharField(max_length = 15, blank = False)
    validity_date = models.DateTimeField(blank = False)
    is_admin = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email