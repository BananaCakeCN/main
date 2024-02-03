import pyautogui,time
print('5秒后开始')
time.sleep(5)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2.7)
for i in range(28):
    pyautogui.click(x=(443+i*20),y=475)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2.7)
for i in range(28):
    if(i==3 or i==6 or i==9 or i==12 or i==15 or i==18 or i==21 or i==24):
        pyautogui.click(x=(443+i*20),y=460)
    else:
        pyautogui.click(x=(443+i*20),y=475)
