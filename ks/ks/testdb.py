# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import redirect, render

from KsModel.models import Test,User

#注册用户
def register(request):
	ctx = {}
	if request.method == "POST":
		#获取账号和密码
		username1 = request.POST.get('username')
		password1 = request.POST.get('password')
		print(username1)
		print(password1)
		ctx['username'] = username1
		ctx['password'] = password1
		#查询该账号是否存在
		# list = User.objects.filter(username=username)
		# print(list)
	# if len(list) == 0:
		user = User(username=username1, password=password1)
		user.save()
		return render(request, "Success.html", ctx)
	# else:
	# 	print('该用户已存在')
	# 	return HttpResponse("注册失败！账号已存在！")
	else:
		return HttpResponse("注册失败！")


#登录
# @app.route('/api/login',methods=['POST'])
def login(request):
	ctx = {}
	if request.method == "POST":
		ctx['username'] = request.POST.get('username')
		ctx['password'] = request.POST.get('password')
		print(ctx['username'])
		print(ctx['password'])
		return HttpResponse("200")
		# return render(request, "Success.html", ctx)

	return HttpResponse("404")

#操作数据库
def testdb(request):
	#version 1
	test1 = Test(name='windwins')
	test1.save()
	return HttpResponse("<p>数据添加成功！</p>")

	#versein 2
	# #初始化
	# response = ""
	# response1 = ""
	#
	# #通过object这个模型管理器的all（）获得所有数据行，相当于sql中的select * from
	# list = Test.objects.all()
	#
	# #filter相当于sql中的where，可设置条件过滤结果
	# response1 = Test.objects.filter(id=1)
	# #限制返回的数据，相当于sql中的offset 0 limit 2；
	# Test.objects.order_by('name')[0:2]
	#
	# #数据排序
	# Test.objects.order_by('id')
	#
	# #上面的方法可以连锁使用
	# Test.objects.filter(name='runoob').order_by('id')
	#
	# #输出所有数据
	# for var in list:
	# 	response1 += var.name
	# response = response1
	# # return HttpResponse("<p>"+ list + "</p>")
	# return HttpResponse(list)

	#version 3
	# test1 = Test.objects.get(id=1)
	# test1.name = 'Google'
	# test1.save()

	#version 4
	# Test.objects.filter(id=1).update(name='alibaba')
	#
	# Test.objects.all().update(name='Google')
	# return HttpResponse("<p>修改成功！</p>")

	#version 5
	#删除id=1d 的数据
	# test1 = Test.objects.get(id=1)
	# test1.delete()
	#
	# return HttpResponse("删除成功")