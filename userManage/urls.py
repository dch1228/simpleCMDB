from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views

urlpatterns = patterns(
	'',  # Examples:  # url(r'^$', 'userManage.views.home', name='home'),  # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', views.login),
	url(r'^logout/$', views.logout),
	url(r'^$', views.index),
	url(r'^userlist/$', views.userlist),
	url(r'^adduser/$', views.adduser),
	url(r'^deluser/$', views.deluser),
	url(r'^userdetail/(?P<uid>\d*)/$', views.userdetail),
)
