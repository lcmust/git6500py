#!/usr/bin/python
#coding=utf-8
# -*- coding: utf-8 -*-
# Create your views here.
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context,RequestContext,Template
from django.template.loader import get_template
from blog.models import Blog,Author
from blog.forms import AuthorForm
import datetime,sys

def get_client_info(request):
    client_info = {}
    client_info['client_ip'] = request.META.get('REMOTE_ADDR', 'protect')
    client_info['client_user_agent'] = request.META.get('HTTP_USER_AGENT', 'no name')
    return client_info

def welcome(request):
    template = get_template("blog_welcome.html")
    content = RequestContext(request, {
            'title': 'welcome',
            'menus': ('index', 'list', 'add', 'authoradd', 'del', 'update', 'admin',),
            'body': 'welcome_body',
            'client_info': get_client_info(request),
            })
    output = template.render(content)
    return HttpResponse(output)

def index(request):
    template = get_template("blog_list.html")
    latest_blog_list = Blog.objects.order_by('-publish_time')[:3]
    content = RequestContext(request, {
            'title': 'index_list',
            'menus': ('index', 'list', 'add', 'authoradd', 'del', 'update', 'admin',),
            'blogs': latest_blog_list,
            'client_info': get_client_info(request),
            })
    return HttpResponse(template.render(content))

def blog_list(request):
    template = get_template("blog_list.html")
    blogs = Blog.objects.all()
    authors = Author.objects.all()
    content = RequestContext(request, {
            'title': 'list',
            'menus': ('index', 'list', 'add', 'del', 'update', 'admin',),
            'body': 'blog_list',
            'blogs': blogs,
            'authors': authors,
            'client_info': get_client_info(request),
            })
    output = template.render(content)
    return HttpResponse(output)

def blog_add(request):
    template = get_template("blog_add.html")

    if request.method == "POST":
        if request.POST['caption'] and request.POST['author'] \
                and request.POST['content']:
            cont = {'title': 'add',
                    'menus': ('index', 'list', 'add', 'del', 'update', 'admin', ),
                    'msg': ("add succsed!",),
                    'body': ''}
            """如果是由新的作者提交，首先将该新作者名增加到数据库表author中"""
            """
            try:
                author1 = Author.objects.get(name=request.POST['author'])
            except:
                print request.POST['author']
                print u'%s' % request.POST['author']
                author_new = Author(name=request.POST['author'])
                author_new.save()"""
            """如果不直接增加新的作者，就提示用户，该作者尚不存在"""
            try:
                author1 = Author.objects.get(name=request.POST['author'])
            except:
                cont = {'title': 'add',
                        'errors': ("author name is not exist",),
                        'menus': ('index', 'list', 'add', 'del', 'update', 'admin',),
                        'body': '',}
                content = RequestContext(request, cont)
                return HttpResponse(template.render(content))

            tmp = Blog(caption=request.POST['caption'],
                       author=author1,
                       content=request.POST['content'],
                       publish_time=datetime.datetime.now())
            tmp.save()
            content = RequestContext(request, cont)
            return HttpResponseRedirect('/blog/list')
        #(template.render(content))
        else:
            cont = {'title': 'add',
                    'errors': ["your input is empty",],
                    'menus': ('index', 'list', 'add', 'del', 'update', 'admin',),
                    'body': '',}
            content = RequestContext(request, cont)
            return HttpResponse(template.render(content))
    else:
        content = RequestContext(request, {
                'title': 'add',
                'menus':('index', 'list', 'del', 'update', 'admin',),
                'body':'',
                })
    return HttpResponse(template.render(content))

def author_add_validate(request):
    template = get_template("author_add.html")
    form = None
    if request.method == "POST":
        if request.POST['name'] and request.POST['email'] and request.POST['website']:
            
            form = AuthorForm(request.POST)
            if form.is_valid():
                form_data = form.cleaned_data
                tmp = Author(name = form_data['name'],
                             email = form_data['email'],
                             website =  form_data['website']
                             )
                tmp.save()
                return HttpResponseRedirect('/blog/list')
            else:  ###form of some <input> is error
                content = RequestContext(request, {
                        'title': 'author_add',
                        'errors': ("your input have some *error(s)*",),
                        'menus': ('index', 'list', 'add', 'authoradd', 'del', 'update', 'admin',),
                        'body': '',
                        'author_form': AuthorForm(),
                        })
                return HttpResponse(template.render(content))
        else: ###some is empty
            content = RequestContext(request, {
                    'title': 'author_add',
                    'errors': ("your input have some *empty(s)*",),
                    'menus': ('index', 'list', 'add', 'authoradd', 'del', 'update', 'admin',),
                    'body': '',
                    'author_form': AuthorForm(),
                    })
            return HttpResponse(template.render(content))            
    else:  ###method is get
        content = RequestContext(request, {
                'title': 'author_add',
                'menus': ('index', 'list', 'add', 'authoradd', 'del', 'update', 'admin',),
                'author_form': AuthorForm(),
                })
        return HttpResponse(template.render(content))

###can delete author_add()
def author_add(request):
    """
    template = get_template("author_add.html")

    content = RequestContext(request, {
            'title': 'author_add',
            'menus': ('index', 'list', 'add', 'authoradd', 'del', 'update', 'admin',),
            })
    return HttpResponse(template.render(content))"""

def blog_del(request):
    template = get_template("blog_del.html")
    latest_blog_list = Blog.objects.all()
    content = RequestContext(request, {
            'title': 'blog_del',
            'menus': ('index', 'list', 'add', 'authoradd', 'del', 'update', 'admin',),
            'blogs': latest_blog_list,
            'client_info': get_client_info(request),
            })
    return HttpResponse(template.render(content))

def blog_update(request):
    return HttpResponse("blog_update")

def admin(request):
    return HttpResponseRedirect("/admin")

def test(request):
    return HttpResponse("<html><title>test</title><body><h2>we will come soon!</h2></body></html>")

