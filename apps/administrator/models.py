from django.db import models

# Create your models here.
# administrator/models.py
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15)
    validity_date = models.DateField()
    picture = models.ImageField(upload_to='user_pictures/', null=True, blank=True)

    class Meta:
        managed = False
        db_table ='authentication_badgeuser'
        
    def __str__(self):
        return self.name
    

