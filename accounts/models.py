from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django_jalali.db import models as jmodels
from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=200, unique=True, verbose_name="ایمیل")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_admin = models.BooleanField(default=False, verbose_name="مدیر")
    last_login = jmodels.jDateTimeField(blank=True, null=True, verbose_name='آخرین بازدید')
    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}--{self.name}"
