from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class AccountUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(
            email=email,
            password=password,
            **extra_fields
        )

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(
            email=email,
            password=password,
            **extra_fields
        )


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]

    # user_uuid = models.UUIDField(default=uuid4, editable=False)
    username = models.CharField(blank=True, unique=False, max_length=50)
    email = models.EmailField(unique=True, max_length=254)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=15)
    phone_number = models.IntegerField()

    objects = AccountUserManager()

    def __str__(self):
        return self.email


class ContactsFields(models.Model):
    # user_uuid = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE
    # )
    email = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    contact_email = models.EmailField(max_length=254)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
