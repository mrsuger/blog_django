from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detail/(?P<blog_id>\d+)/$', views.detail, name = 'get_detail'),
    url(r'^home/$', views.home, name = 'get_home'),
    url(r'^aboutme/$', views.about_me, name = 'about_me'),
    # archives页面需要传入两个参数
    url(r'^archives/(?P<year>\d+)/(?P<month>\d+)/$', views.archives, name = 'get_archives'),
    # category页面传入任意字符串
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name = 'get_category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.tags, name='get_tag'),
    url(r'^search/$', views.search, name = 'get_search'),
]