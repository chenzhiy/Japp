# -*- utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import redirect, render

import datetime
import base64

from KsModel.models import Test, User, TopBanner
import json


# 首页
def home(request):
	ctx = {}
	if request.method == "POST":
		# 获取账号和密码
		ctx['username'] = request.POST.get('username')
		# 返回首页信息
		head = {'code': 0, 'errCode': '0000', 'message': 'success'}
		body = {"onlineNum": 2411, "topBanners": [
			{"image": "/cdn/A06FM/externals/img/_wms/banner/H5bifubaoqukfl484x238.jpg",
			 "link": "http://bbs.kb16888.com/forum.php?mod=viewthread&tid=84291&mobile=2", "imgTitle": "币付宝取款双重好礼",
			 "linkType": "6", "game": []},
			{"image": "/cdn/A06FM/externals/img/_wms/banner/banner_a06_h5_kakawangtiing-484x238-1.jpg",
			 "link": "http://bbs.kb16888.com/forum.php?mod=viewthread&tid=84330&mobile=2", "imgTitle": "AG卡卡湾厅见面有礼",
			 "linkType": "6", "game": []},
			{"image": "/cdn/A06FM/externals/img/_wms/banner/banner_a06_h5_shrangzidanfei-484x238-1.jpg",
			 "link": "/event/promoCode/RZDF", "imgTitle": "捕鱼季-让子弹飞", "linkType": "1", "game": []},
			{"image": "/cdn/A06FM/externals/img/_wms/banner/banner_a06_h5_sycaipioajiams-484x238-1.jpg",
			 "link": "http://bbs.kb16888.com/forum.php?mod=viewthread&tid=84327&mobile=2",
			 "imgTitle": "彩票加码送，投注送iphone天天领9999元", "linkType": "6", "game": []},
			{"image": "/cdn/A06FM/externals/img/_wms/banner/banner_a06_h5_SYXY6-484x238-2.jpg",
			 "link": "http://bbs.kb16888.com/forum.php?mod=viewthread&tid=84284&mobile=2", "imgTitle": "捕“6”行动领赏金",
			 "linkType": "6", "game": []}]}
		return HttpResponse(json.dumps(response_res(head,body)))
	else:
		return HttpResponse("404")


# 注册用户
def register(request):
	ctx = {}
	if request.method == "POST":
		# 获取账号和密码
		ctx['username'] = request.POST.get('username')
		ctx['password'] = request.POST.get('password')
		if len(ctx['username']) > 10:
			head = {'code': 0, 'errCode': '0000', 'message': u'请输入长度为3-10位的字符或数字组合'}
			body = {}
			return HttpResponse(json.dumps(response_res(head,body)))
		# 查询该账号是否存在
		user = User.objects.filter(username=ctx['username'])

		if user:
			head = {'code': 0, 'errCode': '0000', 'message': u'该账号已存在，请更换其他账号'}
			body = {}
			return HttpResponse(json.dumps(response_res(head,body)))
		else:
			# 生成token，然后将该用户的信息返回给前端
			token = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ctx['username'] + ctx['password']
			token = str(base64.b64encode(token.encode('utf-8')), 'utf-8')
			user = User(username=ctx['username'], password=ctx['password'], token=token)
			user.save()
			head = {'code': 0, 'errCode': '0000', 'message': '注册成功'}
			body = user.userToJson()
			return HttpResponse(json.dumps(response_res(head,body)))
	else:
		return HttpResponse("404！")


def checkAccountExist(uname):
	if uname:
		user = User.objects.filter(username=uname)
		if user:
			return True
	return False


# 检查账号密码正确性
def checkAccount(ctx):
	uname = ctx['username']
	passwd = ctx['password']
	if ctx:
		# 检查账号是否存在
		if checkAccountExist(uname):
			# 判断密码是否正确
			if User.objects.filter(username=uname, password=passwd):
				return True
	return False


# 将类转换成json返回
def userToJson(user):
	data = {}
	data["username"] = user.username
	data["password"] = user.password
	data["realName"] = user.realName
	data["starLevel"] = user.starLevel
	data["mobileNo"] = user.mobileNo
	data["customType"] = user.customType
	data["currency"] = user.currency
	data["starName"] = user.starName
	data["customId"] = user.customId
	data["token"] = user.token
	return data


# 登录
def login(request):
	ctx = {}
	# 判断请求方式是否为POST，如果是post，获取用户名和密码
	if request.method == "POST":
		ctx['username'] = request.POST.get('username')
		ctx['password'] = request.POST.get('password')

		# 在检查账号密码是否正确
		if checkAccount(ctx):
			# 生成token，然后将该用户的信息返回给前端
			token = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ctx['username'] + ctx['password']
			token = base64.b64encode(token.encode('utf-8'))
			# 将token存放到对应的用户表中
			user = User.objects.get(username=ctx['username'])
			# User.objects.filter(username=ctx['username']).update(token=token) #更新token
			user.token = str(token, 'utf-8')  # 将token的字节码转成字符串放到数据库中
			user.save()  # 保存登录的token

			# 返回用户信息给前端
			head = {'code': 0, 'errCode': '0000', 'message': 'success'}
			res = response_res(head, user.userToJson())  # 返回字典格式数据
			jVar = json.dumps(res)  # 将字典转成json数据
			return HttpResponse(jVar)
		else:
			head = {'code': 0, 'errCode': '0000', 'message': u'账号或密码不正确'}
			body = {}
			res = response_res(head, body)
			jVar = json.dumps(res)
			return HttpResponse(jVar)
	else:
		return HttpResponse("404")


# 返回消息体类型组装
def response_res(head, body):
	response_result = {}
	response_result['head'] = head
	response_result['body'] = body
	return response_result


# 测试网络请求
def test_network(request):
	if request.method == "GET":
		resultData = {'code': 0, 'message': 'success', 'data': {'userName': 'jacker', 'balance': 0, 'starLevel': 0}}
		jVar = json.dumps(resultData)
		return HttpResponse(jVar)
	return HttpResponse("404")


# 操作数据库
def testdb(request):
	# version 1
	# test1 = User.objects.get(id=5)
	ah1 = TopBanner(
		image="/cdn/A06FM/externals/img/_wms/banner/H5bifubaoqukfl484x238.jpg",
		link="http://bbs.kb16888.com/forum.php?mod=viewthread&tid=84291&mobile=2",
		imageTitle="币付宝取款双重好礼",
		imageType="6",
		game=[])
	ah1.save()

	ah2 = TopBanner(
		image="/cdn/A06FM/externals/img/_wms/banner/banner_a06_h5_kakawangtiing-484x238-1.jpg",
		link="http://bbs.kb16888.com/forum.php?mod=viewthread&tid=84330&mobile=2",
		imageTitle="AG卡卡湾厅见面有礼",
		imageType="6",
		game=[])
	ah2.save()

	ah3 = TopBanner(
		image="/cdn/A06FM/externals/img/_wms/banner/banner_a06_h5_shrangzidanfei-484x238-1.jpg",
		link="/event/promoCode/RZDF",
		imageTitle="捕鱼季-让子弹飞",
		imageType="1",
		game=[])
	ah3.save()

	ah4 = TopBanner(
		image="/cdn/A06FM/externals/img/_wms/banner/banner_a06_h5_sycaipioajiams-484x238-1.jpg",
		link="http://bbs.kb16888.com/forum.php?mod=viewthread&tid=84327&mobile=2",
		imageTitle="彩票加码送，投注送iphone天天领9999元",
		imageType="6",
		game=[])
	ah4.save()

	ah5 = TopBanner(
		image="/cdn/A06FM/externals/img/_wms/banner/banner_a06_h5_SYXY6-484x238-2.jpg",
		link="http://bbs.kb16888.com/forum.php?mod=viewthread&tid=84284&mobile=2",
		imageTitle="捕“6”行动领赏金",
		imageType="6",
		game= [])
	ah5.save()
	return HttpResponse("<p>数据添加成功！</p>")

# versein 2
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

# version 3
# test1 = Test.objects.get(id=1)
# test1.name = 'Google'
# test1.save()

# version 4
# Test.objects.filter(id=1).update(name='alibaba')
#
# Test.objects.all().update(name='Google')
# return HttpResponse("<p>修改成功！</p>")

# version 5
# 删除id=1d 的数据
# test1 = Test.objects.get(id=1)
# test1.delete()
#
# return HttpResponse("删除成功")
