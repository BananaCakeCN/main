import pygame, PyTouchBar, os, base64, random, requests, time, subprocess
from io import BytesIO
if os.uname().sysname != 'Darwin':
    os._exit(0)
pygame.init()
pygame.mixer.pre_init()
pygame.mixer.init()
window = pygame.display.set_mode((550,600))
PyTouchBar.prepare_pygame()
pygame.display.set_caption('DevTools - eat_fish_together()')
colors = [(1,0,0,1),(1,1,0,1),(0,1,0,1),(0,1,1,1),(0,0,1,1),(1,0,1,1)]
pg = 0
fish_pos = []
fish = []
score = 0
wrong_time = 10#grammar: time(s)
gamePause = False
logo_image = b"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"
logo = pygame.image.load(BytesIO(base64.decodebytes(logo_image)))
del base64
def windowReFront():
    subprocess.run(["osascript", "-e", '''
tell application "Finder"
    activate
end tell
'''], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def clickEvent(btn):
    global pg, fish_pos, score, wrong_time, fish
    if pg == 1:
        wrong_time = 10
        if gameMode == 1:
            global startTime
            startTime = time.time()
        fish = []
        fish_pos = []
        pg = 2
        for i in range(10):
            randomInt = random.randint(0, 5)
            fish_pos.append(randomInt)
            fish.append(('[    ]' * randomInt) + '[鱼]' + ('[    ]' * (5 - randomInt)))
        return
    if colors.index(btn.color) == fish_pos[0] and not gamePause:
        score += 1
        del fish_pos[0], fish[0]
        randomInt = random.randint(0, 5)
        fish.append(('[    ]' * randomInt) + '[鱼]' + ('[    ]' * (5 - randomInt)))
        fish_pos.append(randomInt)
        #playSound('https://creation.codemao.cn/716/appcraft/SOUND_Z66LQAW3jU_1661068419445') 延迟问题禁用音效
    else:
        wrong_time -= 1
def quitGame(nothin):
    global pg
    pg = 0
    PyTouchBar.set_touchbar([PyTouchBar.TouchBarItems.Label(text='请在Devtool中输入“eat_fish_together()”开始游戏！')])
    windowReFront()
def playSound(url):
    pygame.mixer.Sound(BytesIO(requests.get(url).content)).play()
buttons = []
for i in range(6):
    buttons.append(PyTouchBar.TouchBarItems.Button(action = clickEvent, color=colors[i]))
def eat_fish_together(mode = 0, play = None):
    global pg, gameMode
    gameMode = mode
    pg = 1
    if play:
        playSound(play)
    PyTouchBar.set_touchbar(buttons, esc_key = PyTouchBar.TouchBarItems.Button(title = "Q", action = quitGame))
    windowReFront()
PyTouchBar.set_touchbar([PyTouchBar.TouchBarItems.Label(text='请在Devtool中输入“eat_fish_together()”开始游戏！')])
print('请在Devtool中输入“eat_fish_together()”开始游戏！')
inputContent = ''
errors = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os._exit(0)
        elif event.type == 768 and pg == 0:
            if event.key == 1073742049 or event.key == 1073742053:
                shiftDown = True
            if event.key == 13:
                try:
                    eval(inputContent)
                except:
                    errors.append('Uncaught ReferenceError: ' + inputContent + ' is not defined')
                inputContent = ''
                break
            if event.key == 8:
                inputContent = inputContent[0:len(inputContent)-1]
                break
            if event.key == 57 and shiftDown:
                inputContent += '('
                lastInput = event.key
                break
            if event.key == 48 and shiftDown:
                inputContent += ')'
                lastInput = event.key
                break
            if event.key == 45 and shiftDown:
                inputContent += '_'
                lastInput = event.key
                break
            if event.key == 59 and shiftDown:
                inputContent += ':'
                lastInput = event.key
                break
            if event.key > 122:
                break
            inputContent += pygame.key.name(event.key, True)
        elif event.type == 769 and pg == 0 and (event.key == 1073742049 or event.key == 1073742053) and shiftDown:
            shiftDown = False
    window.fill((255, 255, 255))
    if pg == 0:
        pygame.draw.line(window, (50, 50, 255), (5,582), (10,587))
        pygame.draw.line(window, (50, 50, 255), (5,592), (10,587))
        window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 15).render(inputContent, True, (0, 0, 0)),(15, 580))
        for i in range(len(errors)):
            window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 15).render(errors[i], True, (255, 0, 0)),(15, 10+i*30))
    elif pg == 1:
        window.blit(logo, (20, 20))
        pygame.draw.rect(window, (0, 0, 0), (20, 170, 300, 35))
        window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 24).render('欢迎游玩《一起吃小鱼》！', True, (255, 255, 0)),(20, 172.5))
        window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 24).render('开始游戏！', True, (254, 196, 51)),(20, 215))
        window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 16).render('你可以随时按下Q键来退出游戏qwq', True, (254, 196, 51)),(135, 223))
        window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 12).render('你现在处于', True, (0, 0, 0)),(20, 250))
        if gameMode == 0:
            window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 16).render('无尽模式', True, (255, 0, 0)),(80, 246))
            window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 12).render('，如果你想切换到20秒模式，', True, (0, 0, 0)),(150, 250))
            window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 12).render('可以退出游戏后重新输入"eat_fish_together(1)"进入20秒模式。', True, (0, 0, 0)),(20, 265))
        else:
            window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 16).render('20秒模式', True, (255, 0, 0)),(80, 246))
            window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 12).render('，倒计时将会在你吃掉第一只小鱼后开始。', True, (0, 0, 0)),(150, 250))
            window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 12).render('如果你想切换到无尽模式，可以退出游戏后重新输入"eat_fish_together()"进入无尽模式。', True, (0, 0, 0)),(20, 265))
        window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 12).render('你知道吗，你可以使用', True, (0, 0, 0)),(20, 280))
        window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 16).render('eat_fish_together(mode,"[Audio URL]")', True, (255, 0, 0)),(150, 277))
        window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 12).render('来进行背景音乐的播放！', True, (0, 0, 0)),(20, 295))
    elif pg == 2:
        if gameMode == 1:
            if time.time() > startTime + 20 or wrong_time <= 0:
                pg = 3
                PyTouchBar.set_touchbar([PyTouchBar.TouchBarItems.Label(text = '←游戏结束，按Q返回')], esc_key = PyTouchBar.TouchBarItems.Button(title = "Q", action = quitGame))
                windowReFront()
            else:
                window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 48).render('分数：' + str(score) + '  倒计时：' + str(20 - (time.time() - startTime)), True, (255, 0, 0)),(20, 5))
        else:
            window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 48).render('分数：' + str(score), True, (255, 0, 0)),(20, 5))
        if not gamePause:
            i = 0
            while i < len(fish_pos):
                window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 48).render(fish[i], True, (0, 0, 0)),(10, 540 - i * 53))
                i += 1
    elif pg == 3:
        window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 48).render('分数：' + str(score), True, (255, 0, 0)),(20, 5))
        if wrong_time <= 0:
            window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 12).render('由于按错次数过多，游戏结束！', True, (0, 0, 0)),(20, 60))
        else:
            window.blit(pygame.font.Font('仓耳渔阳体W05.ttf', 12).render('游戏结束', True, (0, 0, 0)),(20, 60))
    pygame.display.update()
