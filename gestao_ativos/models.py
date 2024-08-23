from django.db import models
from users.models import User

class Ativo(models.Model):
    id_ativo = models.AutoField(primary_key=True)
    nome_ativo = models.CharField(max_length=20, unique=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome_ativo


class ClassificacaoTunel(models.Model):
    id_class_tunel = models.AutoField(primary_key=True)
    classificacao = models.CharField(unique=True, max_length=50)
    
    
    def __str__(self):
        return self.classificacao

class TipoTunel(models.Model):
    id_tipo_tunel = models.AutoField(primary_key=True)
    tipo_tunel = models.CharField(max_length=15)
    
    def __str__(self):
        return self.tipo_tunel

class TipoProtecao(models.Model):
    id_tipo_protecao = models.AutoField(primary_key=True)
    tipo_protecao = models.CharField(max_length=15)
    
    def __str__(self):
        return self.tipo_protecao

class AtivosMonitorado(models.Model):
    id_ativo_monitorado = models.AutoField(primary_key=True)
    ativo = models.ManyToManyField(Ativo)
    usuario = models.ManyToManyField(User)
    class_tunel = models.ManyToManyField(ClassificacaoTunel)
    tipo_tunel = models.ManyToManyField(TipoTunel)
    tipo_protecao = models.ManyToManyField(TipoProtecao)
    preco_base = models.CharField(max_length=20)
    peridiocidade = models.IntegerField()
    is_active = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)