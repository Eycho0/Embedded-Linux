import pyautogui
import time

def install(extension):
    pyautogui.hotkey("ctrl","shift","x")
    pyautogui.hotkey("ctrl","a","backspace")
    pyautogui.write(extension)
    time.sleep(2.5)
    pyautogui.moveTo(840,530)
    pyautogui.click()
    time.sleep(1)


pyautogui.press("win")
pyautogui.write("vs")
pyautogui.moveTo(1080,720)
pyautogui.sleep(0.5)
pyautogui.click()
time.sleep(2)

install("clangd")
install("c++ testmate")
install("c++ helper")
install("cmake")
install("cmake tools")
