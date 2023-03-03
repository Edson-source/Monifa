from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()
# Create your models here.
class Customer (models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    username = models.CharField(max_length=50, unique=True,
        validators=[username_validator],
        error_messages={
            "unique": ("A user with that username already exists."),
        },)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=SEXO, blank=False, null=False)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username