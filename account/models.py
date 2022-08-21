from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    class UserType(models.TextChoices):
        TYPE_EDUCATOR = 'Educator', _('Eduactor')
        TYPE_STUDENT = 'Student', _('Student')
    email = models.EmailField(unique=True,null=False)
    type = models.CharField(choices=UserType.choices,default='Student',max_length=20)