'''
作者：蕉饼
2021-05-23
'''
import requests
from json import dumps
class Box3Search():
    def __init__(self,data):
        self.data = data
        self.map = requests.post('https://box3.codemao.cn/api/api/content-server-rpc',data = dumps({"type":"search","data":{"limit":24,"offset":0,"type":1,"isPublic":True,"keyword":data}})).json()['data']['data']['rows']
        self.asset = requests.post('https://box3.codemao.cn/api/api/content-server-rpc',data = dumps({"type":"search","data":{"limit":24,"offset":0,"type":2,"isPublic":True,"keyword":data}})).json()['data']['data']['rows']
        self.music = requests.post('https://box3.codemao.cn/api/api/content-server-rpc',data = dumps({"type":"search","data":{"limit":24,"offset":0,"type":3,"isPublic":True,"keyword":data}})).json()['data']['data']['rows']
        self.user = requests.post('https://box3.codemao.cn/api/api/content-server-rpc',data = dumps({"type":"search","data":{"limit":10,"offset":0,"targetName":data}})).json()
    def returnResult(self,index,type):
        if type == 1:
            if len(self.map) == 0:
                return '抱歉! 没有找到 ' + self.data + ' 的结果'
            else:
                return self.map[index]
        if type == 2:
            if len(self.asset) == 0:
                return '抱歉! 没有找到 ' + self.data + ' 的结果'
            else:
                return self.asset[index]
        if type == 3:
            if len(self.music) == 0:
                return '抱歉! 没有找到 ' + self.data + ' 的结果'
            else:
                return self.music[index]
        if type == 4:
            if len(self.user) == 0:
                return '抱歉! 没有找到 ' + self.data + ' 的结果'
            else:
                return self.user#[index]
print(Box3Search('吉吉喵').returnResult(0,4))
#Box3Search(名称).returnResult(查询到作品的下标,种类(1：地图，2:模型，3:音乐，4:用户)
