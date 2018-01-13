# _*_ coding:utf-8 _*_
__author__ = 'xiaolin'
__data__ = '2018/1/13 下午6:48'

from extra_apps.xadmin import xadmin
from .models import EmailVerifyRecord
from .models import Banner


class EmailVerifyRecordAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

class BannerAdmin(object):
    pass

xadmin.site.register(Banner, BannerAdmin)