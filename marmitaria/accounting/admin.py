# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


class DespesaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'tipo_despesa', 'data')
    list_filter = ('data',)


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'tipo_receita', 'data')
    list_filter = ('data',)


class CentroDeCustoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'total', 'tipo_centro_custo')
    readonly_fields = ('total',)


class TipoDespesaAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        """
        return {}


class TipoReceitaAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        """
        return {}


class TipoCentroCustoAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        """
        return {}

admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Despesa, DespesaAdmin)
admin.site.register(CentroDeCusto, CentroDeCustoAdmin)
admin.site.register(TipoDespesa, TipoDespesaAdmin)
admin.site.register(TipoReceita, TipoReceitaAdmin)
admin.site.register(TipoCentroCusto, TipoCentroCustoAdmin)
