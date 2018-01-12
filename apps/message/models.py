# _*_ coding:utf-8 _*_
from django.db import models
from datetime import datetime


# 留言表
class UserMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'用户名')
    email = models.EmailField(verbose_name=u'邮箱')
    address = models.CharField(max_length=100, verbose_name=u'联系地址')
    message = models.CharField(max_length=500, verbose_name=u'留言信息')

    class Meta:
        verbose_name = u'用户留言信息'


from django.contrib.auth.models import AbstractUser


# 用户表
class UserProfile(models.Model):
    username = models.CharField(max_length=50, verbose_name=u'账号', default='')
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=100, verbose_name=u'密码', default='')
    last_login = models.CharField(max_length=12,verbose_name=u'最后登录',default='')
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birday = models.DateField(verbose_name=u'生日', default='')
    gender = models.CharField(max_length=5, choices=(('male', u'男'), ('female', u'女')), default='female')
    address = models.CharField(max_length=100, verbose_name=u'地址', default='')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

# 邮箱验证码
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=(('register',u'注册'),('forget',u'找回密码')),max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(upload_to='image/%Y/%m', verbose_name=u'轮播图', default=u'image/default.png', max_length=100)
    url = models.CharField(max_length=200, verbose_name=u'访问地址')
    index = models.ImageField(default=100, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

