# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.core.exceptions import ValidationError


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
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)
    tipo_despesa = models.ForeignKey(TipoDespesa)
    centro_de_custo = models.ForeignKey(CentroDeCusto)
    data = models.DateField(default=datetime.date.today)

    def clean(self):
        #tmp = self.centro_de_custo.total - self.valor
        #if tmp < 0:
        #    raise ValidationError({'centro_de_custo':'Centro de custo sem fundos, selecione outro centro ou adicione nova receita'})
        super(Despesa, self).clean()

    def save(self, *args, **kwargs):
        if self._state.adding:
            centro = CentroDeCusto.objects.get(id=self.centro_de_custo.id)
            centro.total -= self.valor
            centro.save()
        else:
            if self.valor != self._loaded_values['valor']:
                centro = CentroDeCusto.objects.get(id=self.centro_de_custo.id)
                centro.total -= (self.valor - self._loaded_values['valor'])
                centro.save()

        super(Despesa, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nome


class Receita(BaseModel, models.Model):
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)
    tipo_receita = models.ForeignKey(TipoReceita)
    centro_de_custo = models.ForeignKey(CentroDeCusto)
    data = models.DateField(default=datetime.date.today)
    
    def save(self, *args, **kwargs):
        if self._state.adding:
            centro = CentroDeCusto.objects.get(id=self.centro_de_custo.id)
            centro.total += self.valor
            centro.save()
        else:
            if self.valor != self._loaded_values['valor']:
                centro = CentroDeCusto.objects.get(id=self.centro_de_custo.id)
                centro.total += (self._loaded_values['valor'] - self.valor)
                centro.save()

        super(Receita, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nome

