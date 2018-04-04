# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models


class TipoDespesa(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nome


class TipoReceita(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nome


class TipoCentroCusto(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nome


class CentroDeCusto(models.Model):
    total = models.DecimalField(max_digits=6, decimal_places=2)
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)
    tipo_centro_custo = models.ForeignKey(TipoCentroCusto)

    def __unicode__(self):
        return self.nome


class Despesa(models.Model):
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)
    tipo_despesa = models.ForeignKey(TipoDespesa)
    centro_de_custo = models.ForeignKey(CentroDeCusto)
    data = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return self.nome


class Receita(models.Model):
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)
    tipo_receita = models.ForeignKey(TipoReceita)
    centro_de_custo = models.ForeignKey(CentroDeCusto)
    data = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return self.nome
