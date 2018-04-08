# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


@login_required(login_url='/admin/login/')
@permission_required('accounting.add_despesa', raise_exception=True)
def index(request):
    print request.user.get_all_permissions()
    return HttpResponse("Hello, world. You're at the accounting index.")
