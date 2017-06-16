# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'ajax/index.html')

def message(request):
    mess = "Hello from the server!"
    return HttpResponse(mess)
# Create your views here.
