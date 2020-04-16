from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=20)
	realName = models.CharField(max_length=20, null=True,verbose_name='realName')
	starLevel = models.IntegerField(0,null=True)
	mobileNo = models.IntegerField(11,null=True)
	customType = models.IntegerField(0,null=True)
	currency = models.IntegerField(0,null=True)
	starName = models.CharField(max_length=30, null=True, verbose_name='starName')
	customId = models.CharField(max_length=50, null=True, verbose_name='customId')

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