import requests
#使用cookie较为方便,不用输入验证码
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
cookies = {'cookie':'bid=0rMBylP5h7M; __yadk_uid=20aDycjsAaAi5qmWqbMuQAbTXDFWGVao; ll="108296"; ps=y; _ga=GA1.2.961478068.1503283417; _gid=GA1.2.1490945184.1504763157; dbcl2="65537734:lfgoWNwf9DE"; ck=M60s; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1504766315%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Falias%3D13735836970%26redir%3Dhttps%253A%252F%252Fwww.douban.com%252F%26source%3Dindex_nav%26error%3D1013%22%5D; ap=1; _pk_id.100001.8cb4=2b2d25c87bf276bb.1503283417.4.1504767093.1504763286.; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utmt=1; __utma=30149280.961478068.1503283417.1504766316.1504767093.5; __utmb=30149280.2.10.1504767093; __utmc=30149280; __utmz=30149280.1504767093.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.6553; ct=y'}
url = 'http://www.douban.com'
r = requests.get(url,cookies = cookies,headers = headers)
with open('douban_2.txt','wb+') as f:
	f.write(r.content)