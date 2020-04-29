from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=20)
	realName = models.CharField(max_length=20)
	starLevel = models.IntegerField(1,default=0)
	mobileNo = models.IntegerField(11,default=0)
	customType = models.IntegerField(1,default=0)
	currency = models.IntegerField(1,default=0)
	starName = models.CharField(max_length=30)
	customId = models.CharField(max_length=50)
	token = models.CharField(max_length=255)

	def userToJson(self):
		return{
			"username": self.username,
			# "password": self.password,
			"realName": self.realName,
			"starLevel": self.starLevel,
			"mobileNo": self.mobileNo,
			"customType": self.customType,
			"currency": self.currency,
			"starName": self.starName,
			"customId": self.customId,
			"token": self.token,
		}

class Test(models.Model):
	objects = None
	name = models.CharField(max_length=20)

class Contact(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField(default=0)
	email = models.EmailField()
	def __unicode__(self):
		return self.name

class Tag(models.Model):
	contact = models.ForeignKey(Contact,on_delete=models.CASCADE,)
	name = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name

class TopBanner(models.Model):
	image = models.CharField(max_length=100)
	imageTitle = models.CharField(max_length=100)
	imageType = models.CharField(max_length=100)
	game = models.CharField(max_length=255)
	link = models.CharField(max_length=255)

class Balance(models.Model):
	balance = models.FloatField(11,default=0.0)
	localBalance = models.FloatField(11,default=0.0)
	minWithdrawAmount = models.IntegerField(11,default=20)
	platformTotalBalance = models.FloatField(11,default=0.0)
	withdrawBal = models.FloatField(11,default=0.0)

class GameList(models.Model):
	pageNo = models.IntegerField(1,default=0)
	pageSize = models.IntegerField(1000,default=20)
	totalPage = models.IntegerField(100000,default=0)
	totalRow = models.IntegerField(10000,default=0)