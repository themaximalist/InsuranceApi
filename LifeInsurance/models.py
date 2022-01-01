from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
# Create your models here.


class Branch(models.Model):
    branch_name = models.CharField(max_length=64)


class LifeInsurnaceModel(models.Model):

    name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    email = models.EmailField(null=False)
    phoneNumberRegex = RegexValidator(regex=r"(^\+98|0098|98|0)?9\d{9}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=14, unique=True)
    age = models.PositiveSmallIntegerField()
    BMI = models.PositiveSmallIntegerField()
    smoker = models.BooleanField(default=False)
    cigarette_count = models.PositiveIntegerField(default=0)
    hookah_count = models.PositiveIntegerField(default=0)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
