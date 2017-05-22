from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import http.client as httplib
from .forms import NameForm
from seotools.models import Metatags
from django.http import JsonResponse
from scipy.stats import chisquare, chi2_contingency

def index(request):
	content = {'meta_tags' : get_meta_tags(request)}
	return render(request, 'seotools/index.html', content)


def get_meta_tags(request):
	uri = str(request.get_full_path())
	try:
		meta_tags = Metatags.objects.get(page_uri=uri)
	except Exception as e:
		meta_tags = ''
	return meta_tags


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
	context = {'ip_adress' : str(get_client_ip(request)),
		'meta_tags' : get_meta_tags(request)
	}	
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
					site = host + uri
					status_code = str(res.status) 
					reason = str(res.reason)
					msg = str(res.msg)
					return render(
							request, 
							'seotools/test.html', 
							{
								'site' : site, 
								'status_code' : status_code, 
								'reason' : reason, 
								'msg' : msg
							}
						)
			else:
				return HttpResponse("empty url")
	else:
		form = NameForm()
	return render(request, 
		'seotools/headers.html', 
		{
			'form': form,
			'meta_tags' : get_meta_tags(request)
		})


def about(request):
	context = {'meta_tags' : get_meta_tags(request)}
	return render(request, 'seotools/about.html', context)


def contact(request):
	context = {'meta_tags' : get_meta_tags(request)}
	return render(request, 'seotools/contact.html', context)


def ab_test(request):
	context = {'meta_tags' : get_meta_tags(request),}
	return render(request, 'seotools/ab_test.html', context)


def chi_square(request):
	if request.method == "GET":
		a_visits = int(request.GET['aVisits'])
		b_visits = int(request.GET['bVisits'])
		a_goals = int(request.GET['aGoals'])
		b_goals = int(request.GET['bGoals'])
		arr = [[a_visits, b_visits], [a_goals, b_goals]]
		chi_statistic, p_value, ddof, expected = chi2_contingency(arr)
		response = {'chi_statistic' : chi_statistic,
			'p_value' : p_value
		}
		return JsonResponse(response)
	else:
		return HttpResponse('no', content_type='text/html')



def simple(request):
	import random
	import django
	import datetime

	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure
	from matplotlib.dates import DateFormatter

	fig=Figure()
	ax=fig.add_subplot(111)
	x=[]
	y=[]
	now=datetime.datetime.now()
	delta=datetime.timedelta(days=1)
	for i in range(10):
		x.append(now)
		now+=delta
		y.append(random.randint(0, 1000))
	ax.plot_date(x, y, '-')
	ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
	fig.autofmt_xdate()
	canvas=FigureCanvas(fig)
	response=django.http.HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response