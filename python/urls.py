from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import view
from apps.message.views import getform

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', view.hello),
    url(r'^form/$', getform)
]
