#!/usr/bin/python3
"""
Custom User Model for authentication.

This module defines a custom user model by extending Django's
`AbstractBaseUser` and `BaseUserManager`. It includes custom
methods for creating regular users and superusers.
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class AccountManager(BaseUserManager):
    """
    Custom manager for the `Account` model.

    This manager provides methods for creating both regular users
    and superusers.
    """
    def create_user(
        self, username, first_name, last_name, email,
        phone_number, password=None
    ):
        """
        Creates and returns a new user.

        Args:
            username (str): The user's unique username.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            email (str): The user's email address.
            phone_number (str): The user's phone number.
            password (str, optional): The user's password. Defaults to None.

        Returns:
            Account: The created user instance.

        Raises:
            ValueError: If email or phone number is missing.
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not phone_number:
            raise ValueError("User must have a phone number")

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, first_name, last_name, email,
        phone_number, password=None
    ):
        """
        Custom user model extending `AbstractBaseUser`.

        This model replaces Django's default User model, adding fields for
        first name, last name, phone number, and user roles.

        Attributes:
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            username (str): Unique username for the user.
            email (str): The user's email (used for login).
            phone_number (str): The user's phone number.
            date_joined (datetime): The date the user registered.
            last_login (datetime): The date of the user's last login.
            is_active (bool): Whether the account is active.
            is_admin (bool): Whether the user has admin privileges.
            is_staff (bool): Whether the user is staff.
            is_superadmin (bool): Whether the user is a superadmin.
        """
        user = self.create_user(
            username, first_name, last_name, email, phone_number, password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    """
    Custom User extending AbstractBaseUser.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    # Permissions and role-related fields
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']

    def __str__(self):
        """
        Returns a string representation of the user.

        Returns:
            str: The user's email address.
        """
        return self.email

    def has_perm(self, perm, obj=None):
        """
        Returns a string representation of the user.

        Returns:
            str: The user's email address.
        """
        return self.is_admin

    def has_module_perms(self, app_label):
        """
        Checks if the user has permissions to view an app.

        Args:
            app_label (str): The app label to check.

        Returns:
            bool: Always True (superusers have all permissions).
        """
        return True
