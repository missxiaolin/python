from django.conf.urls import url

from . import view
from apps.message.views import getform

urlpatterns = [
    url(r'^$', view.hello),
    url(r'^form/$', getform)
]
