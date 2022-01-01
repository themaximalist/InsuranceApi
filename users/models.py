from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    """
        this model inherit from "AbstractUser" and adds "phonNumber" field to default user object

    """
    phoneNumberRegex = RegexValidator(regex=r"(^\+98|0098|98|0)?9\d{9}$") # for validation of phoneNumber
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=14, unique=True)
