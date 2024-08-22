from django.db import models
from users.models import User

class Ativos(models.Model):
    id_ativo = models.IntegerField(primary_key=True)
    nome_ativo = models.CharField(max_length=20, unique=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class AtivosMonitorados(models.Model):
    id_ativo_monitorado = models.IntegerField(primary_key=True)
    id_ativos = models.ManyToManyField(Ativos)
    id_usuario = models.ManyToManyField(User)
    class_tunel = models.CharField(max_length=10)
    tipo_tunel = models.CharField(max_length=15)
    tipo_protecao = models.CharField(max_length=15)
    preco_base = models.CharField(max_length=20)
    peridiocidade = models.IntegerField()