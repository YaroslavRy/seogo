from django.conf.urls import url
from .import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^get_ip', views.get_ip, name='get_ip'),
	url(r'^get_headers$', views.get_headers, name='get_headers'),
	url(r'^headers$', views.headers, name='headers'),
	url(r'^about$', views.about, name='about'),
	url(r'^contact$', views.contact, name='contact'),
	url(r'^robots.txt$', views.robots, name='robots'),
]