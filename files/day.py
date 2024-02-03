import requests, time
from json import dumps
earlyTime = int(input('输入当天最早的Unix时间戳'))
lastTime = int(input('输入当天最晚的Unix时间戳'))
lastCodemaoID = int(input('输入最新的Codemao作品ID'))
interval = 0
dayLatest = 0
dayEarliest = 0
CanOver = True
print('正在进行最初测试....\n')
if requests.get('https://api.codemao.cn/api/work/info/' + str(lastCodemaoID - interval)).json()['msg'] == '成功':
    workTime = requests.get('https://api.codemao.cn/api/work/info/' + str(lastCodemaoID - interval)).json()['data']['workDetail']['workInfo']['create_time']
    print('正在进行下一步...\n')
    startTime = time.time()
    print('开始计时！\n\n')
    while True:
        interval += 800
        try:
            workTime = int(requests.get('https://api.codemao.cn/api/work/info/' + str(lastCodemaoID - interval)).json()['data']['workDetail']['workInfo']['create_time'])
        except :
            print('出现错误，作品可能被删除')
        if workTime < lastTime and CanOver:
            print('当天最晚的作品ID在' + str(lastCodemaoID - interval) + '-' + str(lastCodemaoID - interval + 800) + '范围内。')
            dayLatest = lastCodemaoID - interval + 800
            CanOver = False
        if workTime < earlyTime:
            print('当天最早的作品ID在' + str(lastCodemaoID - interval) + '-' + str(lastCodemaoID - interval + 800) + '范围内。')
            dayEarliest = lastCodemaoID - interval + 800
            print('当日新建作品约有' + str(dayLatest - dayEarliest) + '个')
            break
        print('已用时' + str((time.time() - startTime)/60) + '分钟。' + '\n')
else:
    print('请重试')
