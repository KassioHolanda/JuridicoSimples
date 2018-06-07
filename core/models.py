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


class Postagem(models.Model):
    data_postagem = models.DateTimeField('Data de Postagem', auto_now_add=True)
    titulo = models.CharField('Titulo', max_length=40, null=False)
    resumo = models.CharField('Resumo', max_length=40, null=True)
    tema = models.ForeignKey('Theme', related_name='news_theme', max_length=255, null=True, on_delete=models.CASCADE)
    corpo = models.TextField('Corpo da Noticia', null=False, max_length=60000)
    imagem = models.FileField(upload_to=get_file_path, null=True)
    postagem_principal = models.BooleanField('Postagem Principal', default=False, null=False)

    # user_register = models.ForeignKey('User', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('-data_postagem',)


class Theme(models.Model):
    descricao = models.CharField('Descrição Tema', max_length=255, null=False)
    nome = models.CharField('Nome', max_length=255, null=False, unique=True)

    def __str__(self):
        return self.nome

    @property
    def todas_as_postagens(self):
        return Postagem.objects.filter(theme=self)


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
