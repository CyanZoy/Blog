from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import (login, logout, authenticate,)
from django import forms
from django.contrib.auth.decorators import login_required
import json
from collections import defaultdict


class UserRegisterFrom(forms.Form):
    username = forms.CharField(label="用户名", max_length=100, min_length=3,
                               widget=forms.TextInput(attrs={'autofocus': 'autofocus', 'placeholder': '请输入用户名',
                                                             'name': 'form_username',
                                                             'class': 'form-first-name form-control'}))
    password = forms.CharField(label='密码', min_length=6,
                               widget=forms.TextInput(attrs={'placeholder': '请输入密码', 'name': 'form_password',
                                                             'class': 'form-first-name form-control',
                                                             'type': 'password'}))

    password_again = forms.CharField(label='密码', min_length=6,
                               widget=forms.TextInput(attrs={'placeholder': '请再次输入密码', 'name': 'form_password_again',
                                                             'class': 'form-first-name form-control',
                                                             'type': 'password'}))


class UserLoginFrom(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class roo(forms.Form):
    msg = forms.CharField(
        label='wrong',
    )


def index(request):
    return render(request, 'htmls/index.html')


def login_process(request):
    __next_web = request.GET.get('next') if request.GET.get('next') else '/note'
    print(__next_web)
    if request.method == "POST":
        uf_login = UserLoginFrom(request.POST)
        if uf_login.is_valid():
            username = uf_login.cleaned_data['username']
            password = uf_login.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                request.session['username'] = username
                response = HttpResponseRedirect(__next_web)
                request.session.set_expiry(60*15)
                return response
            else:
                return HttpResponseRedirect('/login')
    elif request.user.is_authenticated:
        return HttpResponseRedirect('/note')
    else:
        uf = UserRegisterFrom()
        return render(request, 'htmls/login.html', {'uf': uf, 'next': __next_web})


def logout_process(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST' and not request.is_ajax():
        newUser = UserRegisterFrom(request.POST)
        if newUser.is_valid():
            username = newUser.cleaned_data['username']
            password = newUser.cleaned_data['password']
            password_again = newUser.cleaned_data['password_again']
            return HttpResponseRedirect('/')
        else:
            g = newUser.errors.as_json()
            print(g)
            msg = []
            for _ in newUser.errors:
                print(newUser.errors[_].data[0])
                msg.append(newUser.errors[_].data[0])
            uf = UserRegisterFrom()
            return render(request, 'htmls/register.html', {'msg': msg, 'uf': uf})
    elif request.method == 'POST' and request.is_ajax():
        username = request.POST.get('username')
        print(username)
        return HttpResponse("yes")
    else:
        uf = UserRegisterFrom()
        context = {'uf': uf}
        return render(request, 'htmls/register.html', context)


from BlogFront.interface.note_model import *
@login_required
def note(request):
    if not request.is_ajax():
        notename = request.GET.get('spm').lower()
        allname = ModelGet.note_get_name()
        # 如果没有笔记名参数则默认查询全部
        if not notename:
            allnote = ModelGet.note_get_t()
            context = Change.queryset_to_dic((allnote, allname), one='note', two='name')
            return render(request, 'htmls/note.html', context=context)
        result = ModelGet.note_get_t(notename)
        # 查询没结果则重定向至note
        if not result:
            return HttpResponseRedirect('/note')
        # 查询对应笔记
        context = Change.queryset_to_dic((result, allname), one='note', two='name')
        return render(request, 'htmls/note.html', context=context)
    else:
        # spm = notename = request.GET.get('spm').lower()
        note_num = request.GET.get('id')
        print(note_num)
        return HttpResponse('success')