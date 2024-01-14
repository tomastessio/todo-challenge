from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, last_name, password,  is_staff, is_superuser, **extrafields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            password = password,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extrafields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, username, email, name, last_name, password=None, **extrafields):
        return self._create_user(username, email, name, last_name, password, False, False, **extrafields)
    
    def create_superuser(self, username, email, name, last_name, password=None, **extrafields):
        return self._create_user(username, email, name, last_name, password, True, True, **extrafields)
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField('Correo electrónico', max_length=100, unique=True)
    name = models.CharField('Nombre', max_length=255, blank=True, null=True)
    last_name = models.CharField('Apellido', max_length=255, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name', 'last_name']
    
    def __str__(self):
        return f'{self.name}{self.last_name}'
