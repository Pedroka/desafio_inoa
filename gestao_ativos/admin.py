from django.contrib import admin
from django import forms
from .models import Ativo, AtivosMonitorado, ClassificacaoTunel, TipoTunel, TipoProtecao

@admin.register(Ativo)
class AtivoAdmin(admin.ModelAdmin):
    list_display = ['nome_ativo', 'data_criacao', 'is_active']

@admin.register(AtivosMonitorado)
class AtivosMonitoradosAdmin(admin.ModelAdmin):
    pass

@admin.register(ClassificacaoTunel)
class ClassTunelAdmin(admin.ModelAdmin):
    list_display = ['classificacao']

@admin.register(TipoTunel)
class TipoTunelAdmin(admin.ModelAdmin):
    list_display = ['tipo_tunel']
    
@admin.register(TipoProtecao)
class TipoProtecaoAdmin(admin.ModelAdmin):
    list_display = ['tipo_protecao']