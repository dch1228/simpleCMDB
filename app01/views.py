from django.shortcuts import render_to_response, HttpResponseRedirect
from django.contrib import auth
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from models import UserInfo

# Create your views here.


def login(request):
	data = {'loginStatus': ''}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/')
		data['loginStatus'] = 'Wrong username or password!'
	return render_to_response('login.html', data, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def index(request):
	return render_to_response('index.html')


@login_required(login_url='/login/')
def userlist(request):
	model = UserInfo.objects.all()
	return render_to_response('userlist.html', {'model': model}, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def adduser(request):
	posData = request.POST
	uid = posData.get('uid')
	username = posData.get('username')
	name = posData.get('name')
	gender = posData.get('gender')
	email = posData.get('email')
	if gender == 'null':
		gender = None
	elif int(gender) == 0:
		gender = 0
	else:
		gender = 1
	if username and name and email:
		if uid:
			UserInfo.objects.filter(uid=int(uid)).update(username=username, realName=name, gender=gender, email=email)
		else:
			userInfo = UserInfo(username=username, realName=name, gender=gender, email=email)
			userInfo.save()
	return HttpResponseRedirect('/userlist/')


@login_required(login_url='/login/')
def deluser(request):
	posData = request.POST
	uid = posData.get('deluid')
	if uid:
		uid = int(uid)
		UserInfo.objects.filter(uid=uid).delete()
	return HttpResponseRedirect('/userlist/')


@login_required(login_url='/login/')
def userdetail(request, uid):
	result = UserInfo.objects.get(uid=int(uid))
	return render_to_response('userdetail.html', {'key1': result})