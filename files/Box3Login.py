'''
作者：蕉饼
2021-06-13
'''
import requests
from json import dumps
boxID = input('手机号/邮箱/Box ID')
password = input('密码')
headers = {'accept-encoding': 'gzip, deflate, br','accept-language': 'zh-CN,zh;q=0.9','content-type': 'text/plain;charset=UTF-8','origin': 'https://box3.codemao.cn','referer': 'https://box3.codemao.cn/notification?type=1','sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"','user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
requests.post('https://box3.codemao.cn/api/api/auth-server-rpc',data = dumps({"type":"login","data":{"password":password,"target":boxID}}))
print(requests.post('https://box3.codemao.cn/api/api/notify-server-rpc',headers = headers,data = {"type":"list","data":{"limit":10,"offset":0,"type":1}}).text)
