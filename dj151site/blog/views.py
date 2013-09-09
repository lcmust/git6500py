#!/usr/bin/python
#coding=utf-8
# -*- coding: utf-8 -*-
# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, Template
from django.template.loader import get_template
from blog.models import Blog, Author, AuthorForm, BlogForm
from blog.forms import AuthorForm2, BlogForm2
import datetime,sys
import cStringIO as StringIO
from py_pil_validate2 import CreateValidateCode
###learn_test
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
####

###learn_test
@receiver(request_finished)
def my_callback(sender, **kwargs):
    #print("Request finished! %s" % datetime.datetime.ctime(datetime.datetime.now()))
    pass


def get_client_info(request):
    client_info = {}
    client_info['client_ip'] = request.META.get('REMOTE_ADDR', 'protect')
    client_info['client_user_agent'] = request.META.get('HTTP_USER_AGENT', 'no name')

    try:
        client_info['csrftoken'] = request.COOKIES.get('csrftoken', "unknown")
    except:
        client_info['csrftoken'] = 'Unknown'
    try:
        client_info['sessionid'] = request.COOKIES.get('sessionid', 'unknown')
    except:
        client_info['sessionid'] = 'Unknown'

    return client_info

def welcome(request):
    login_required_(request)
    template = get_template("blog_welcome.html")
    content = RequestContext(request, {
            'title': 'welcome',
            'menus': ('index', 'login', 'list', 'add', 'authoradd', 'del', 'update', 'admin',),
            'body': 'welcome_body',
            'client_info': get_client_info(request),
            })
    output = template.render(content)
    return HttpResponse(output)

def login(request):
    if request.method == "POST":
        if request.POST['Username'] and request.POST['Password']\
                and request.POST['Validate']:
            if request.POST['Username'] == "admin" and\
                    request.POST['Password'] == "admin":
                resp_out = HttpResponse("login susscued!")
                resp_out.set_cookie('hello', 'world')
                resp_out.flush()
                #return resp_out
                return HttpResponseRedirect("/blog/")
            else:
                return HttpResponseRedirect("#")
        else:
            return HttpResponseRedirect("/blog/login/")
    else:
        template = get_template("blog_login.html")
        content = RequestContext(request, {
                'title': 'login',
                'menus': ('index',),
                'clent_info': get_client_info(request),
                })
        output = template.render(content)
        return HttpResponse(output)

def logout(request):
    is_admin = request.COOKIES.get('hello', "")
    if is_admin:
        print is_admin
        html = HttpResponse()
        html.delete_cookie('hello')
        del html['hello']
        html.close()
        return html
    return HttpResponseRedirect("/blog/")

def login_required_(request, function=None, redirect_field_name=None, login_url=None):
    if request.COOKIES.get('hello', ''):
        print "request.COOKIES['hello']:", request.COOKIES['hello']
        return
    else:
        return HttpResponseRedirect('/blog/login/')


def index(request):
    login_required_(request)
    template = get_template("blog_list.html")
    latest_blog_list = Blog.objects.order_by('-publish_time')[:3]
    content = RequestContext(request, {
            'title': 'index_list',
            'menus': ('index', 'login', 'list', 'add', 'authoradd', 'del', 'update', 'admin',),
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

#@login_required
def blog_add(request):
    template = get_template("blog_add.html")

    if request.method == "POST":
        if request.POST['caption'] and request.POST['author'] \
                and request.POST['content']:
            cont = {'title': 'add',
                    'menus': ('index', 'list', 'add', 'del', 'update', 'admin', ),
                    'msg': ("add succsed!",),
                    'body': ''}
            """如果是由新的作者提交:该新作者名在数据库表author中不存在时，提示用户：该作者尚不存在"""
            """20130720-1220 在blog_add提交页面中使用了BlogForm后，author是用下拦框进行选择，不再是自己输入任意的AUTHOR，所以不会出现在数据库中不存在的用户了。
            实际使用中，用户首先登录到平台中，由该登录用户发表的BLOG，作者一栏自然就是该登录用户名了，不允许由A登录后以B的身份发布BLOG。"""
            try:
                print request.POST['author']
                author1 = Author.objects.get(pk=request.POST['author'])
            except:
                cont = {'title': 'add',
                        'errors': ("author name is not exist",),
                        'menus': ('index', 'list', 'add', 'del', 'update', 'admin',),
                        'body': '',
                        'blog_form': BlogForm(),
                        }
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
                    'body': '',
                    'blog_form': BlogForm(),
                    }
            content = RequestContext(request, cont)
            return HttpResponse(template.render(content))
    else:
        content = RequestContext(request, {
                'title': 'add',
                'menus':('index', 'list', 'del', 'update', 'admin',),
                'body':'',
                'blog_form': BlogForm(),
                #'blog_form2': BlogForm2(),
                })
    return HttpResponse(template.render(content))

def author_add(request):
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

def blog_detail(request, id=1):
    try:
        blog_choice = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    template = get_template("blog_detail.html")
    content = RequestContext(request, {
            'title': 'blog_detail',
            'menus': ('index', 'list', 'add', 'admin'),
            'blog': blog_choice,
            'blog_form': BlogForm(),
            'client_info': get_client_info(request),
            })
    return HttpResponse(template.render(content))


def blog_update(request):
    return HttpResponse("blog_update")

def admin(request):
    return HttpResponseRedirect("/admin")

def validate(request):
    mstream = StringIO.StringIO()
    validate1 = CreateValidateCode(fg_color_random=1)
    validate2 = validate1.create_all()
    validate2[0].save(mstream, "GIF")
    request.session['validate'] = validate2[1]

    respon_out =  HttpResponse(mstream.getvalue(), "image/gif")
    respon_out['Cache-Control'] = "no-cache"
    return respon_out
    #return HttpResponse("<html><title>validate</title><body><table><tr><th>title1><title2></tr><tr><td>" + <img validate2[0].show() + "<td><td>here is validate code img</td></tr></table></body></html>")

def current_now(request):
    now = datetime.datetime.ctime(datetime.datetime.now())
    return HttpResponse(now)

def test(request):
    return HttpResponse("<html><title>test</title><body><h2>we will come soon!</h2></body></html>")

def test_css(request):
    return render_to_response("blog/test_css.html", {'body': ""})
