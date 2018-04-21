# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


class BaseAdmin(object):
    def get_actions(self, request):
        actions = super(BaseAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class ProdutoDespesaInline(admin.TabularInline):
    model = ProdutoDespesa
    extra = 1


class ProdutoReceitaInline(admin.TabularInline):
    model = ProdutoReceita
    extra = 1


class ProdutoAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = ('nome',)


class ProdutoDespesaAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = ('produto', 'valor', 'quantidade')

    def get_model_perms(self, request):
        """
        """
        return {}


class ProdutoReceitaAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = ('produto', 'valor', 'quantidade')

    def get_model_perms(self, request):
        """
        """
        return {}


class DespesaAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = ('nome', 'valor_total', 'tipo_despesa', 'data')
    list_filter = ('data',)
    inlines = (ProdutoDespesaInline,)
    readonly_fields = ('valor', 'valor_total')
    exclude = ('produtos',)
    fieldsets = (
        (None, {
            'fields': ('valor',
                       'valor_total',
                       'nome',
                       'descricao',
                       'tipo_despesa',
                       'centro_de_custo',
                       'data')
        }),
    )


class ReceitaAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = ('nome', 'valor_total', 'tipo_receita', 'data')
    list_filter = ('data',)
    inlines = (ProdutoReceitaInline,)
    readonly_fields = ('valor', 'valor_total')
    exclude = ('produtos',)
    fieldsets = (
        (None, {
            'fields': ('valor',
                       'valor_total',
                       'nome',
                       'descricao',
                       'tipo_receita',
                       'centro_de_custo',
                       'data')
        }),
    )


class CentroDeCustoAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = ('nome', 'total', 'tipo_centro_custo')
    readonly_fields = ('total',)


class TipoDespesaAdmin(BaseAdmin, admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        """
        return {}


class TipoReceitaAdmin(BaseAdmin, admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        """
        return {}


class TipoCentroCustoAdmin(BaseAdmin, admin.ModelAdmin):
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
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(ProdutoDespesa, ProdutoDespesaAdmin)
admin.site.register(ProdutoReceita, ProdutoReceitaAdmin)
