# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import decimal
from django.db import models
from django.core.exceptions import ValidationError
from django.template.defaultfilters import floatformat


class BaseModel(object):
    @classmethod
    def from_db(cls, db, field_names, values):
        # Default implementation of from_db() (subject to change and could
        # be replaced with super()).
        if len(values) != len(cls._meta.concrete_fields):
            values = list(values)
            values.reverse()
            values = [
                values.pop() if f.attname in field_names else DEFERRED
                for f in cls._meta.concrete_fields
            ]
        instance = cls(*values)
        instance._state.adding = False
        instance._state.db = db
        # customization to store the original field values on the instance
        instance._loaded_values = dict(zip(field_names, values))
        return instance


class Produto(models.Model):
    nome = models.CharField(max_length=40)

    def __unicode__(self):
        return self.nome


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
    total = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)
    tipo_centro_custo = models.ForeignKey(TipoCentroCusto)

    def __unicode__(self):
        return self.nome


class Despesa(BaseModel, models.Model):
    valor = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)
    tipo_despesa = models.ForeignKey(TipoDespesa)
    centro_de_custo = models.ForeignKey(CentroDeCusto)
    data = models.DateField(default=datetime.date.today)
    produtos = models.ManyToManyField(Produto, through='ProdutoDespesa')

    @property
    def valor_total(self):
        val_tmp = decimal.Decimal()
        prod_despesa = ProdutoDespesa.objects.filter(despesa=self)
        for prod in prod_despesa:
            for i in range(prod.quantidade):
                val_tmp += prod.valor
        return floatformat(val_tmp, 2)

    def clean(self):
        #tmp = self.centro_de_custo.total - self.valor
        #if tmp < 0:
        #    raise ValidationError({'centro_de_custo':'Centro de custo sem fundos, selecione outro centro ou adicione nova receita'})
        super(Despesa, self).clean()

    def save(self, *args, **kwargs):
        super(Despesa, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Despesa, self).delete(*args, **kwargs)

    def __unicode__(self):
        return self.nome


class Receita(BaseModel, models.Model):
    valor = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)
    tipo_receita = models.ForeignKey(TipoReceita)
    centro_de_custo = models.ForeignKey(CentroDeCusto)
    data = models.DateField(default=datetime.date.today)
    produtos = models.ManyToManyField(Produto, through='ProdutoReceita')

    @property
    def valor_total(self):
        val_tmp = decimal.Decimal()
        prod_receita = ProdutoReceita.objects.filter(receita=self)
        for prod in prod_receita:
            for i in range(prod.quantidade):
                val_tmp += prod.valor
        return floatformat(val_tmp, 2)

    def save(self, *args, **kwargs):
        super(Receita, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Receita, self).delete(*args, **kwargs)

    def __unicode__(self):
        return self.nome


class ProdutoDespesa(BaseModel, models.Model):
    produto = models.ForeignKey(Produto)
    despesa = models.ForeignKey(Despesa)
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    quantidade = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if self._state.adding:
            centro = CentroDeCusto.objects.get(id=self.despesa.centro_de_custo.id)

            if self.despesa.valor != 0:
                self.despesa.descricao += " valor antigo: [%s]" % self.despesa.valor
                centro.total += self.despesa.valor
                self.despesa.valor = 0
                self.despesa.save()

            for i in range(self.quantidade):
                centro.total -= self.valor
                centro.save()
        else:
            if self.valor != self._loaded_values['valor']:
                centro = CentroDeCusto.objects.get(id=self.despesa.centro_de_custo.id)
                for i in range(self.quantidade):
                    centro.total -= (self.valor - self._loaded_values['valor'])
                    centro.save()
        super(ProdutoDespesa, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        centro = CentroDeCusto.objects.get(id=self.despesa.centro_de_custo.id)
        for i in range(self.quantidade):
            centro.total += self.valor
        centro.save()
        super(ProdutoDespesa, self).delete(*args, **kwargs)


class ProdutoReceita(BaseModel, models.Model):
    produto = models.ForeignKey(Produto)
    receita = models.ForeignKey(Receita)
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    quantidade = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if self._state.adding:
            centro = CentroDeCusto.objects.get(id=self.receita.centro_de_custo.id)

            if self.receita.valor != 0:
                self.receita.descricao += " valor antigo: [%s]" % self.receita.valor
                centro.total -= self.receita.valor
                self.receita.valor = 0
                self.receita.save()

            for i in range(self.quantidade):
                centro.total += self.valor
                centro.save()
        else:
            if self.valor != self._loaded_values['valor']:
                centro = CentroDeCusto.objects.get(id=self.receita.centro_de_custo.id)
                for i in range(self.quantidade):
                    centro.total += (self.valor - self._loaded_values['valor'])
                    centro.save()
        super(ProdutoReceita, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        centro = CentroDeCusto.objects.get(id=self.receita.centro_de_custo.id)
        for i in range(self.quantidade):
            centro.total -= self.valor
        centro.save()
        super(ProdutoReceita, self).delete(*args, **kwargs)
