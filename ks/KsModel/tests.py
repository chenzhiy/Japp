from django.test import TestCase
import json
import hashlib
import datetime

# Create your tests here.
resultData = {'code':0, 'message':'success', 'data': {'userName': 'username', 'balance': 0, 'starLevel': 0}}

print(resultData)

j = json.dumps(resultData)
print(j)

str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
print(str)

pw = "123456"
hl = hashlib.md5()
hl.update(pw.encode('utf-8'))
print(hl.digest())

