# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def submit(request):
    if request.method == "POST":
        print request.POST.get('input-textarea')
    return render(request, 'index.html')
