from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class BadgeUserManager(BaseUserManager):
    def create_user(self, email, name, birth_date, phone, validity_date, password, picture=None):
        if not email:
            raise ValueError('O campo de e-mail deve ser definido')
        if not password:
            raise ValueError('O campo de senha deve ser definido')
        user = self.model(
            email = self.normalize_email(email),
            name=name,
            birth_date=birth_date,
            phone=phone,
            validity_date=validity_date,
            picture=picture,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, birth_date, phone, validity_date, password, picture=None):
        if not email:
            raise ValueError('O campo de e-mail deve ser definido')
        if not password:
            raise ValueError('O campo de senha deve ser definido')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            birth_date=birth_date,
            phone=phone,
            validity_date=validity_date,
            picture=picture,
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

class BadgeUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length = 30, blank = False)
    email = models.EmailField(unique = True, blank = False)
    birth_date = models.DateField(blank = False)
    phone = models.CharField(max_length = 15, blank = False)
    validity_date = models.DateField(blank = False)
    is_admin = models.BooleanField(default = False)
    picture = models.ImageField(upload_to = "users/", blank = True)

    objects = BadgeUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'birth_date', 'phone', 'validity_date']
    DATE_INPUT_FORMATS = ['%d-%m-%Y']

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def __str__(self):
        return self.email
