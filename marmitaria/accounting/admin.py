# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


class DespesaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'tipo_despesa', 'data')
    list_filter = ('data',)

    def get_actions(self, request):
        actions = super(DespesaAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'tipo_receita', 'data')
    list_filter = ('data',)

    def get_actions(self, request):
        actions = super(ReceitaAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class CentroDeCustoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'total', 'tipo_centro_custo')
    readonly_fields = ('total',)

    def get_actions(self, request):
        actions = super(CentroDeCustoAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class TipoDespesaAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        """
        return {}

    def get_actions(self, request):
        actions = super(TipoDespesaAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class TipoReceitaAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        """
        return {}

    def get_actions(self, request):
        actions = super(TipoReceitaAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class TipoCentroCustoAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        """
        return {}

    def get_actions(self, request):
        actions = super(TipoCentroCustoAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Despesa, DespesaAdmin)
admin.site.register(CentroDeCusto, CentroDeCustoAdmin)
admin.site.register(TipoDespesa, TipoDespesaAdmin)
admin.site.register(TipoReceita, TipoReceitaAdmin)
admin.site.register(TipoCentroCusto, TipoCentroCustoAdmin)
