from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.utils import timezone
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

import requests
import re

from .models import Log


class LogView(ListView):
    model = Log
    template_name = 'log_list.html'


class LogDetailView(DetailView):
    model = Log


def SendPost(request):
    server = re.search('.+(?=:None)|.+:\d+', request.POST['server']).group(0)
    request = request.POST['request']

    headers = {'Content-Type': 'application/json'}

    response = requests.post(server, data=request, headers=headers)

    return HttpResponse(response.content)