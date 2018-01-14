# _*_ coding:utf-8 _*_
__author__ = 'xiaolin'
__data__ = '2018/1/14 上午11:15'

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    url('^list/$', TemplateView.as_view(template_name="org_list.html"), name="org_list"),
]

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)