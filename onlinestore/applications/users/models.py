from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
import uuid
#
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField('ID usuario', default=uuid.uuid4, editable=False)
    email = models.EmailField('Correo Electronico', max_length=254, unique=True)
    full_name = models.CharField('Nombre Completo', max_length=200)
    date_birth = models.DateField('Fecha Nacimiento', null=True, blank=True)
    address = models.CharField('Direccion', max_length=50, null=True, blank=True)  
    phone = models.CharField('Telefono', max_length=12, null=True, blank=True)
    photo = models.ImageField('Foto Perfil', upload_to='perfil', null=True, blank=True)
    cod_activated = models.CharField('Codigo Activacion', max_length=6)
    marketingaccept = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    #
    otp_base32 = models.CharField(max_length=255, blank=True, null=True)
    login_otp = models.CharField(max_length=255, blank=True, null=True)
    use_login_otp = models.BooleanField(default=False)
    created_at = models.DateField('OTP creado', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name',]

    

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.email