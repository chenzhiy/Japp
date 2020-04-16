from django.http import HttpResponse
from django.shortcuts import render_to_response

#表单
def search_form(request):
	return render_to_response("search_form.html")

#登录表单
def login_form(request):
	return render_to_response("login.html")

#注册表单
def register_form(request):
	return render_to_response("register.html")

#接收请求数据
def search(request):
	request.encoding='utf-8'
	if 'q' in request.GET and request.GET['q']:
		message = '你搜素的内容为：' + request.GET['q']
	else:
		message = '你提交了空表单'
	return HttpResponse(message)
