# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import decimal
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from accounting.models import ProdutoDespesa
from accounting.models import ProdutoReceita


@login_required(login_url='/admin/login/')
@permission_required('accounting.add_despesa', raise_exception=True)
def index(request):
    return render(request, 'accounting/index.html')


@login_required(login_url='/admin/login/')
@permission_required('accounting.add_despesa', raise_exception=True)
def despesa(request):
    queryset = ProdutoDespesa.objects.all()
    products = {}
    for obj in queryset:
        if not products.get(obj.produto.nome):
            products[obj.produto.nome] = {
                'quantidade': decimal.Decimal(0),
                'total': decimal.Decimal(0)
            }
        products[obj.produto.nome]['quantidade'] += obj.quantidade
        products[obj.produto.nome]['total'] += (obj.valor * obj.quantidade)

    context = {
        'products': products
    }
    return render(request, 'accounting/despesa.html', context)


@login_required(login_url='/admin/login/')
@permission_required('accounting.add_despesa', raise_exception=True)
def receita(request):
    queryset = ProdutoReceita.objects.all()
    products = {}
    for obj in queryset:
        if not products.get(obj.produto.nome):
            products[obj.produto.nome] = {
                'quantidade': decimal.Decimal(0),
                'total': decimal.Decimal(0)
            }
        products[obj.produto.nome]['quantidade'] += obj.quantidade
        products[obj.produto.nome]['total'] += (obj.valor * obj.quantidade)

    context = {
        'products': products
    }

    return render(request, 'accounting/receita.html', context)