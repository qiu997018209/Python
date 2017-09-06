#coding:utf-8
import requests
import html5lib
import re
from bs4 import BeautifulSoup
#本代码使用输入验证码登陆，环境为Python3

#建立一个会话
s = requests.Session()
url_login = 'https://accounts.douban.com/login'

#url_contacts = 'https://www.douban.com/people/****/contacts'

formdata = {
	'redir':'https://www.douban.com',
	'form_email':'13735836970',
	'form_password':'qiu5863370',
	'login':u'登陆'
}

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

r = requests.post(url_login,data = formdata,headers = headers)
content = r.text

soup = BeautifulSoup(content,'html5lib')
#找到验证码
captcha = soup.find('img',id = 'captcha_image')
if captcha:
	captcha_url = captcha['src']
	re_captcha_id = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
	captcha_id = re.findall(re_captcha_id,content)
	print(captcha_url)
	captcha_text = input('Please input the captcha:')
	formdata['captcha-solution'] = captcha_text
	formdata['captcha-id'] = captcha_id
	r = s.post(url_login,data = formdata,headers = headers)
#print (r.text)
#r = s.get(url_contacts)	
with open('content.txt','w+',encoding = 'utf-8') as f:
	f.write(r.text)