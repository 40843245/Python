import pyautogui
import time

print("請在5秒內開啟記事本並設為焦點視窗")
time.sleep(5) #程式暫停五秒，讓你有時間打開記事本
pyautogui.typewrite(['H','e','l','l','o'],0.1) #每隔0.1秒輸出一個字