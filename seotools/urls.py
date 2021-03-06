from django.conf.urls import url
from django.http import HttpResponse
from .import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^get_ip', views.get_ip, name='get_ip'),
	url(r'^get_headers$', views.get_headers, name='get_headers'),
	url(r'^headers$', views.headers, name='headers'),
	url(r'^about$', views.about, name='about'),
	url(r'^contact$', views.contact, name='contact'),
	url(r'^ab_test$', views.ab_test, name='ab_test'),
	url(r'^chi_square$', views.chi_square, name='chi_square'),
	url(r'^simple.png$', views.simple, name='simple'),
	url(r'^robots.txt$', 
		lambda r: HttpResponse("User-agent: *\nAllow: * \nDisallow: /admin/*", content_type="text/plain")),
]