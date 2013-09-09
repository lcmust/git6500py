#!/usr/bin/env python
#coding=utf-8
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, Template
from django.template.loader import get_template
from logs.models import Ipaddres
import datetime, sys

def welcome(request):
    template = get_template("logs_welcome.html")
    content = RequestContext(request, {
            'title': 'logs_welcome',
            'menus': ('welcome', 'admin'),
            'body': 'welcome_body',
            'body2': 'welcome_body2',
            'client_info': '',
            })
    output = template.render(content)
    return HttpResponse(output)

def index(request):
    template = get_template("logs_index.html")
    content = RequestContext(request, {
            'title': 'logs_index',
            'menus': ('welcome', 'admin'),
            'body': 'index_body',
            })
    output = template.render(content)
    return HttpResponse(output)
