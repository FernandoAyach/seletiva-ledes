from django.db import models


from django.db import models
from django.contrib.auth import get_user_model

class UserEditRequest(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    birth_date = models.DateField(default='2001-01-01')
    phone = models.CharField(max_length=15, blank=True)
    picture = models.ImageField(upload_to="users/", blank=True)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    def approve(self):
        if self.name: self.user.name = self.name
        if self.email: self.user.email = self.email
        if self.birth_date: self.user.birth_date = self.birth_date
        if self.phone: self.user.phone = self.phone
        if self.picture: self.user.picture = self.picture

        self.is_approved = True
        self.is_rejected = False
        
        self.user.save()
        self.save
        
    def reject(self):
        self.is_approved = False
        self.is_rejected = True
        
        self.save()