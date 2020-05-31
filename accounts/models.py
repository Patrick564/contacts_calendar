# Python imports
from uuid import uuid4
from datetime import date

# Django imports
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Library imports
from phone_field import PhoneField


# Custom create user/superuser funcs
class AccountUserManager(UserManager):
    """
    Class UserManager extended to create users by replacing
    username with email.
    """
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')

        if User.objects.filter(email=email).exists():
            return ValueError('Email is already registered')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(
            email=email,
            password=password,
            is_active=True,
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


# Custom model User
class User(AbstractUser):
    """
    User model with customized fields.
    """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    ]

    user_uuid = models.UUIDField(default=uuid4, editable=False)
    username = models.CharField(
        unique=True,
        max_length=50
    )
    email = models.EmailField(unique=True, max_length=254)
    date_of_birth = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        default=date.today
    )
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=15,
        blank=True,
        default='O'
    )
    phone_number = PhoneField(blank=True, default='00000000')

    objects = AccountUserManager()

    def __str__(self):
        return self.email
