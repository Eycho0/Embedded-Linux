import time
import os
import pyautogui
from plyer import notification
import psutil


os.system("start \"\" https://mail.google.com/mail/u/2/#inbox")
time.sleep(3)

pyautogui.moveTo(420,300)
pyautogui.leftClick()
pyautogui.moveTo(730,300)
pyautogui.leftClick()
    
battery = psutil.sensors_battery().percent
print(battery)
notification.notify(
    title="Battery Percentage",
    message=f"{battery}% remaining",
    timeout=10
)
