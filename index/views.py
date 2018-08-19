from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
def index_views(request):
    name = 'zhang'
    age = 26
    address = 'chengdu'
    return render(request, 'index.html', locals())

def login_views(request):
    if request.method == 'GET':
        print('session', request.session.items())
        print('cookie', request.COOKIES)
        if request.session.get('id',''):
            return HttpResponseRedirect('/')
        elif 'id' in request.COOKIES and 'uphone' in request.COOKIES:
            request.session['id'] = request.COOKIES['id']
            request.session['uphone'] = request.COOKIES['uphone']
            return HttpResponseRedirect('/')
        return render(request, 'login.html')
    else:
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        users = User.objects.filter(uphone=uphone, upwd=upwd)
        if users:
            request.session['id'] = users[0].id
            request.session['uphone'] = uphone
            resp = HttpResponseRedirect('/')
            if 'isSaved' in request.POST:
                MAX_AGE = 60*60*24
                resp.set_cookie('id', users[0].id, MAX_AGE)
                resp.set_cookie('uphone', uphone, MAX_AGE)
            return resp
        else:
            return render(request, 'login.html')

def regist_views(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    else:
        uphone = request.POST['uphone']
        users = User.objects.filter(uphone=uphone)
        if users:
            errMsg = '手机号已经注册'
            return render(request, 'regist.html', locals())
        else:
            upwd = request.POST['upwd']
            uname = request.POST['uname']
            uemail = request.POST['uemail']
            User.objects.create(uphone=uphone, upwd=upwd, uname=uname, uemail=uemail)
            users = User.objects.filter(uphone=uphone, upwd=upwd)
            request.session['id'] = users[0].id
            request.session['uphone'] = uphone
            resp = HttpResponseRedirect('/')
            resp.set_cookie('name', 'zhang', 60)
            return resp