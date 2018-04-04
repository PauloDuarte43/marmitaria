# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(TipoDespesa)
admin.site.register(TipoReceita)
admin.site.register(CentroDeCusto)
admin.site.register(TipoCentroCusto)