# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-04 17:24
from __future__ import unicode_literals

import accounting.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CentroDeCusto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19)),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=200)),
                ('data', models.DateField(default=datetime.date.today)),
                ('centro_de_custo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.CentroDeCusto')),
            ],
            bases=(accounting.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19)),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=200)),
                ('data', models.DateField(default=datetime.date.today)),
                ('centro_de_custo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.CentroDeCusto')),
            ],
            bases=(accounting.models.BaseModel, models.Model),
        ),
        migrations.CreateModel(
            name='TipoCentroCusto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDespesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoReceita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='receita',
            name='tipo_receita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.TipoReceita'),
        ),
        migrations.AddField(
            model_name='despesa',
            name='tipo_despesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.TipoDespesa'),
        ),
        migrations.AddField(
            model_name='centrodecusto',
            name='tipo_centro_custo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.TipoCentroCusto'),
        ),
    ]
