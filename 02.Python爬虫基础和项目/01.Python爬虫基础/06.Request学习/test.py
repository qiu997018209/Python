#coding:utf-8
import requests


#print (dir(requests))
url = 'http://www.baidu.com'
#r = requests.get(url)
'''
print (r.status_code)
print (r.text)
print (r.encoding)
'''
'''
#二进制数据
from PIL import Image
from io import BytesIO
r = requests.get('https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&hs=2&pn=0&spn=0&di=92576665720&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cl=2&lm=-1&cs=1380084653%2C2448555822&os=2973510374%2C1623682744&simid=4142519358%2C676911946&adpicid=0&lpn=0&ln=30&fr=ala&fm=&sme=&cg=girl&bdtype=0&oriquery=&objurl=http%3A%2F%2Fwww.zhlzw.com%2FUploadFiles%2FArticle_UploadFiles%2F201204%2F20120412123914329.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bziszo_z%26e3Bv54AzdH3Ff3AzdH3F5s44AzdH3F0088d0_z%26e3Bip4s&gsm=0')
image = Image.open(BytesIO(r.content))
image.save('meinv.jpg')
'''
'''
#json处理
r = requests.get('https://github.com/timeline.json')
print(r.json)
print(r.text)
'''
'''
#原始数据处理
r = requests.get('https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&hs=2&pn=0&spn=0&di=92576665720&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cl=2&lm=-1&cs=1380084653%2C2448555822&os=2973510374%2C1623682744&simid=4142519358%2C676911946&adpicid=0&lpn=0&ln=30&fr=ala&fm=&sme=&cg=girl&bdtype=0&oriquery=&objurl=http%3A%2F%2Fwww.zhlzw.com%2FUploadFiles%2FArticle_UploadFiles%2F201204%2F20120412123914329.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bziszo_z%26e3Bv54AzdH3Ff3AzdH3F5s44AzdH3F0088d0_z%26e3Bip4s&gsm=0')
with open('2.jpg','wb+') as f:
	for chunk in r.iter_content(1024):
		f.write(chunk)
'''
#提交表单
params = {'jsonrpc':'2.0','id':1,'method':'list'}
r = requests.post(url='http://127.1.1.1:1234/run', data=params)
print (r.url)
print (r.text)