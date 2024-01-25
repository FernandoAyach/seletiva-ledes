from django.db import models

# Create your models here.
# administrator/models.py
from django.db import models


class UserEditRequest(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    novoNome = models.CharField(max_length=30)
    is_approved = models.BooleanField(default=False)

    def approve(self):
        self.user.name=self.novoNome
        self.user.save()
   

