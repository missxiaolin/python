# _*_ coding:utf-8 _*_
from django.db import models
from datetime import datetime
from apps.courses.models import Course


# 留言表
class UserMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'用户名')
    email = models.EmailField(verbose_name=u'邮箱')
    address = models.CharField(max_length=100, verbose_name=u'联系地址')
    message = models.CharField(max_length=500, verbose_name=u'留言信息')
    has_read = models.BooleanField(default=False, verbose_name=u'是否已读')

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
    last_login = models.CharField(max_length=12, verbose_name=u'最后登录', default='')
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birday = models.DateField(verbose_name=u'生日', default='')
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='female')
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
    send_type = models.CharField(choices=(('register', u'注册'), ('forget', u'找回密码')), max_length=10,
                                 verbose_name=u'发送类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(upload_to='image/%Y/%m', verbose_name=u'轮播图', default=u'image/default.png',
                              max_length=100)
    url = models.CharField(max_length=200, verbose_name=u'访问地址')
    index = models.ImageField(default=100, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name


# 用户资讯
class UserAsk(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'手机号')
    course_name = models.CharField(max_length=50, verbose_name=u'课程名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户资讯'
        verbose_name_plural = verbose_name


# 用户评论
class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程')
    comment = models.CharField(max_length=200, verbose_name=u'评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name


# 用户收藏
class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户')
    fav_id = models.IntegerField(default=0, verbose_name=u'数据id')
    fav_type = models.IntegerField(choices=((1, u'课程'), (2, u'课程机构'), (3, u'讲师')), default=1, verbose_name=u'收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


# 用户课程
class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name
