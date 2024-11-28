import uuid

from base.base_models import BaseModel
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import Q, UniqueConstraint
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        create and save a user with given username, email and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser, BaseModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("ID"),
        help_text="A unique identifier for each user, generated automatically.",
    )
    username = None
    first_name = models.CharField(
        max_length=150, blank=True, null=True, verbose_name=_("first_name")
    )
    last_name = models.CharField(
        max_length=150, blank=True, null=True, verbose_name=_("last_name")
    )
    email = models.EmailField(
        null=False,
        unique=True,
        blank=False,
        db_index=True,
        verbose_name=_("user_email"),
    )
    birth_date = models.DateTimeField(
        blank=True, null=True, verbose_name=_("date_of_birth")
    )
    profile_picture = models.ImageField(
        upload_to="media/profile_pictures",
        blank=True,
        null=True,
        verbose_name=_("user_profile_picture"),
    )
    mobile_number = models.CharField(  # TODO validation
        max_length=50,
        null=True,
        blank=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"{self.id}"

    class Meta:
        verbose_name_plural = "Users"
        verbose_name = "User"
