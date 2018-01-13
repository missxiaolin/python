# _*_ coding:utf-8 _*_
__author__ = 'xiaolin'
__data__ = '2018/1/14 上午12:04'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
