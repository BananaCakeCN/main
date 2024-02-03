import requests, random
print('游戏正在加载')
agelst = requests.get("http://liferestart.syaro.io/data/age.json").json()
eventlst = requests.get("http://liferestart.syaro.io/data/events.json").json()
print('加载完毕')
age = 0
e = []
while True:
    agen = agelst[str(age)]['event']
    r = random.randint(0,len(agen)-1)
    event = str(agen[r]).split('*')[0]
    print(agen)
    print(event)
    e.append(event)
    print(eventlst[event]['event'])
    input('回车继续')
    age += 1
