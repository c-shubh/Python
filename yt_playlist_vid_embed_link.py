'''Gets the embed link of youtube playlist url.'''
import webbrowser
import time
import pyautogui as gui
import os


def waitForMe():
    while True:
        time.sleep(0.2)
        a, b = gui.position()
        # 1260,0    1288,0
        # 1260,17   1288,17
        if 1259 <= a <= 1288 and 0 <= b <= 17:
            break


os.system('title Youtube player')
while True:
    try:
        URL = input("Enter playlist video url: ")
        print()
        URL = URL[:24] + "embed/" + URL[32:43]
        webbrowser.open(URL)
        waitForMe()
        gui.click(x=681, y=399)  # start (screen center yt logo)
        time.sleep(3)
        gui.click(x=1232, y=721)  # settings
        waitForMe()
        gui.click(x=1232, y=590)  # speed
        time.sleep(0.5)
        gui.click(x=1318, y=321)  # custom
        time.sleep(0.5)
        gui.press(['up']*4)  # change speed
        time.sleep(0.5)
        gui.click(x=1232, y=721)  # close settings
        waitForMe()
        gui.click(x=681, y=399)  # pause (screen center)
        time.sleep(0.5)
        gui.click(x=1322, y=539)  # close more vids
        time.sleep(0.5)
        gui.click(x=681, y=399)  # play (screen center)
        os.system('cls')  # clear console
    except KeyboardInterrupt:
        exit()
    except gui.FailSafeException:
        raise
