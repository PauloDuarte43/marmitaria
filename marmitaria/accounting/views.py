# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import decimal
import calendar
import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from accounting.models import ProdutoDespesa
from accounting.models import ProdutoReceita
from accounting.models import Receita
from accounting.models import Despesa


def range_date(request):
    if (request.method == 'POST' and request.POST.get('data-inicial') and request.POST.get('data-final')):
        start_d = datetime.datetime.strptime(request.POST.get('data-inicial'), '%Y-%m-%d')
        end_d = datetime.datetime.strptime(request.POST.get('data-final'), '%Y-%m-%d')
        start_day = start_d.day
        end_day = end_d.day
        start_month = start_d.month
        end_month = end_d.month
        start_year = start_d.year
        end_year = end_d.year
    else:
        now = datetime.datetime.now()
        _, last_day = calendar.monthrange(now.year, now.month)
        start_day = 1
        end_day = last_day
        start_month = end_month = now.month
        start_year = end_year = now.year

    data_inicial = datetime.datetime(year=start_year,
                                     month=start_month,
                                     day=start_day,
                                     hour=0,
                                     minute=0,
                                     second=0)
    data_final = datetime.datetime(year=end_year,
                                   month=end_month,
                                   day=end_day,
                                   hour=23,
                                   minute=59,
                                   second=59)
    return data_inicial, data_final


@login_required(login_url='/admin/login/')
@permission_required('accounting.add_despesa', raise_exception=True)
def index(request):
    return render(request, 'accounting/index.html')


@login_required(login_url='/admin/login/')
@permission_required('accounting.add_despesa', raise_exception=True)
def despesa(request):
    data_inicial, data_final = range_date(request)
    despesa = Despesa.objects.filter(data__range=(data_inicial, data_final))
    queryset = ProdutoDespesa.objects.filter(despesa__in=despesa)
    products = {}
    for obj in queryset:
        if not products.get(obj.produto.nome):
            products[obj.produto.nome] = {
                'quantidade': decimal.Decimal(0),
                'total': decimal.Decimal(0),
                'data': None
            }
        products[obj.produto.nome]['quantidade'] += obj.quantidade
        products[obj.produto.nome]['total'] += (obj.valor * obj.quantidade)

    context = {
        'products': products,
        'data_inicial': data_inicial,
        'data_final': data_final
    }
    return render(request, 'accounting/despesa.html', context)


@login_required(login_url='/admin/login/')
@permission_required('accounting.add_despesa', raise_exception=True)
def receita(request):
    data_inicial, data_final = range_date(request)
    receita = Receita.objects.filter(data__range=(data_inicial, data_final))
    queryset = ProdutoReceita.objects.filter(receita__in=receita)
    products = {}
    for obj in queryset:
        if not products.get(obj.produto.nome):
            products[obj.produto.nome] = {
                'quantidade': decimal.Decimal(0),
                'total': decimal.Decimal(0),
                'data': None
            }
        products[obj.produto.nome]['quantidade'] += obj.quantidade
        products[obj.produto.nome]['total'] += (obj.valor * obj.quantidade)

    context = {
        'products': products,
        'data_inicial': data_inicial,
        'data_final': data_final
    }

    return render(request, 'accounting/receita.html', context)
