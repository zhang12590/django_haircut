from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views, kwargs=None, name='index'),
    url(r'^login/$', login_views, kwargs=None, name='login'),
    url(r'^regist/$', regist_views, kwargs=None, name='regist'),
]