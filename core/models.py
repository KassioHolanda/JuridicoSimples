import re

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models

# Create your models here.
from django.core import validators
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s%s' % (uuid.uuid4(), ext)
    return os.path.join('media', filename)


class News(models.Model):
    date = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    title = models.CharField('Titulo', max_length=40, null=False)
    resume = models.CharField('Resumo', max_length=40, null=True)
    theme = models.ForeignKey('Theme', related_name='news_theme', max_length=255, null=True, on_delete=models.CASCADE)
    body = models.TextField('Corpo da Noticia', null=False)
    image = models.FileField(upload_to=get_file_path, null=True)
    # user_register = models.ForeignKey('User', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('pk',)


class Theme(models.Model):
    description = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

    @property
    def all_news(self):
        return News.objects.filter(theme=self)


class User(AbstractBaseUser):
    username = models.CharField(
        "Nome do Usuário",
        max_length=30,
        unique=True,
        validators=[validators.RegexValidator(re.compile("^[\w.@+-]+$"),
                                              "O nome do user so pode conter letras, digitos ou os""seguintes caracteres @/./+/-/_"
                                              "invalid")])
    email = models.EmailField("E-mail", unique=True)
    nome = models.EmailField("Nome", unique=True)

    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.nome or self.username
