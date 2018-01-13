# _*_ coding:utf-8 _*_
__author__ = 'xiaolin'
__data__ = '2018/1/13 下午6:48'

from extra_apps.xadmin import xadmin
from .models import EmailVerifyRecord, Banner

# 主题
class BaseSetting(object):
    enable_themes = True
    use_booswatch = True

class GlobalSetting(object):
    site_title = '小林'
    site_bootswatch = True

# xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)
# xadmin.site.register(xadmin.views.CommAdminView, GlobalSetting)


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
