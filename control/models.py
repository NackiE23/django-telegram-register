from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True):
        custom_user = self.model(email=self.normalize_email(email))
        custom_user.set_password(password)
        custom_user.is_staff = is_staff
        custom_user.is_admin = is_admin
        custom_user.is_active = is_active
        custom_user.save()
        return custom_user

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class CustomUser(AbstractBaseUser):
    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
        ordering = ['name']

    user_id = models.CharField(max_length=45, null=True, verbose_name="User id")
    username = models.CharField(max_length=45, null=True, verbose_name='Username')
    name = models.CharField(max_length=45, null=True, verbose_name="Name")

    email = models.EmailField(unique=True)  # require

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_telegram_url(self):
        return f"https://t.me/{self.username}"
