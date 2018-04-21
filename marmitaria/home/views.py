# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    #print request.user.get_all_permissions()
    return render(request, 'home/index.html')