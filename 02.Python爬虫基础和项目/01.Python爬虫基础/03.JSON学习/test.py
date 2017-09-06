#coding:utf-8
import json

obj = {'one':1,'two':2,'three':[1,2,3]}
#将字典编码
encoded = json.dumps(obj)
print encoded
print type(encoded)
#解码
decoded = json.loads(encoded)
print decoded
print type(decoded)