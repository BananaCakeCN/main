'''
作者：蕉饼
2021-11-14
用于修改千桔（“橘”的第二次汉字简化）果（网站已关闭）账号的头像，默认头像只能修改为网站预配的。
'''
import requests
from json import dumps
data = {'imageurl': " ../material/2021/11/14/c225d492-1230-4384-b502-bc461f26cb38.png",
'account': '蕉饼',
'sex': '1',
'mysign': '?',
'htmlcode': 'bananacake',
'type': 1}
headers = {'Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'zh-CN,zh;q=0.9','Connection': 'keep-alive','Content-Length': '212','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': {your cookie here},'Host': 'www.qianjugo.com','Origin': 'https://www.qianjugo.com','Referer': 'https://www.qianjugo.com/main/ViewMyInfo?','sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"macOS"','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
print(requests.post('https://www.qianjugo.com/Jason/saveuser1',headers=headers,data=data).text)
