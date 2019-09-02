from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models

User = settings.AUTH_USER_MODEL


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField()
    email_confirmation = models.EmailField()
    bio = models.TextField(validators=[MinLengthValidator(limit_value=10)])
    avatar = models.ImageField()

    def __str__(self):
        return self.first_name
