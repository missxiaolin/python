# _*_ coding:utf-8 _*_
__author__ = 'xiaolin'
__data__ = '2018/1/13 下午6:48'

from extra_apps.xadmin import xadmin
from .models import EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin(object):
    # 显示
    list_display = ['email', 'send_type', 'send_time']
    # 搜索
    search_field = ['code', 'email']
    # 过滤
    list_filter = ['code', 'email', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin(object):
    pass


xadmin.site.register(Banner, BannerAdmin)
