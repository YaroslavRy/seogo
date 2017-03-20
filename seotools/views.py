from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import http.client as httplib
from .forms import NameForm


def index(request):
    return render(request, "seotools/index.html")


def get_ip(request):
	def get_client_ip(request):
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			print("returning FORWARDED_FOR")
			ip = x_forwarded_for.split(',')[-1].strip()
		elif request.META.get('HTTP_X_REAL_IP'):
			print("returning REAL_IP")
			ip = request.META.get('HTTP_X_REAL_IP')
		else:
			print("returning REMOTE_ADDR")
			ip = request.META.get('REMOTE_ADDR')
		return ip
	context = {'ip_adress' : str(get_client_ip(request))}	
	return render(request, 'seotools/get_ip.html', context)


def get_headers(request):
	url = 'nasa.gov'
	if url:
		conn = httplib.HTTPConnection(url)
		try:
			conn.request("HEAD", "")
		except Exception as e:
			return HttpResponse("Damn! " + str(e))
		else:
			res = conn.getresponse()
			return HttpResponse("Here are meta of " 
				+ url 
				+ ": <br>" 
				+ str(res.status) 
				+ " "
			+ str(res.getheaders()))
	else:
		return HttpResponse("empty url")


def headers(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether it's valid:
		url = request.POST['headers']
		if form.is_valid():
			if url:
				if url.find("/") > 1:
					urlIndex = url.find("/")
					host = url[:urlIndex]
					uri = url[urlIndex:]
					conn = httplib.HTTPConnection(host)
				else:
					host = url
					uri = "/"
				conn = httplib.HTTPConnection(host)			
				try:
					conn.request("HEAD", uri)
				except Exception as e:
					return HttpResponse("Fuck! " + str(e))
				else:
					res = conn.getresponse()
					# return HttpResponse(# "Here are meta of " 
					# 	"Results for " 
					# 	+ host + uri
					# 	+ ": <br>" 
					# 	+ "Status code: "
					# 	+ str(res.status) 
					# 	+ "<br>" 
					# 	+ str(res.reason)
					# 	+ "<br>" 
					# 	+ str(res.msg)
					# )
					site = host + uri
					status_code = str(res.status) 
					reason = str(res.reason)
					msg = str(res.msg)
					return render(request,'seotools/test.html', {'site' : site, 'status_code' : status_code, 'reason' : reason, 'msg' : msg})
			else:
				return HttpResponse("empty url")
	else:
		form = NameForm()
	return render(request, 'seotools/headers.html', {'form': form})


def about(request):
	return render(request, 'seotools/about.html')


def contact(request):
	return render(request, 'seotools/contact.html')


def robots(request):
	return render(request, 'seotools/robots.txt')

