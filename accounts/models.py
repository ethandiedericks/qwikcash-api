import uuid
from io import BytesIO
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import validate_email
from django.db import models
from django.core.files.base import ContentFile

from phonenumbers import parse, is_valid_number
from phonenumbers.phonenumberutil import NumberParseException
from PIL import Image


class MarketplaceUserManager(BaseUserManager):
    def create_user(self, email, phone_number, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not phone_number:
            raise ValueError("Users must have a phone number")
        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, phone_number, first_name, last_name, password=None
    ):
        user = self.create_user(
            email=self.normalize_email(email),
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MarketplaceUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, validators=[validate_email])
    phone_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MarketplaceUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number", "first_name", "last_name"]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.profile_picture:
            img = Image.open(self.profile_picture)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)

                # Save the resized image back to the profile_picture field
                img_io = BytesIO()
                img.save(img_io, format="JPEG")
                self.profile_picture.save(
                    self.profile_picture.name,
                    ContentFile(img_io.getvalue()),
                    save=False,
                )

        super().save(*args, **kwargs)

    def clean(self):
        try:
            parsed_number = parse(self.phone_number, "ZA")
            if not is_valid_number(parsed_number):
                raise ValueError("Invalid phone number")
        except NumberParseException:
            raise ValueError("Invalid phone number")

        try:
            parsed_number = parse(self.whatsapp_number, "ZA")
            if not is_valid_number(parsed_number):
                raise ValueError("Invalid WhatApp number")
        except NumberParseException:
            raise ValueError("Invalid WhatsApp number")
