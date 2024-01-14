from win32api import *
from win32gui import *
import win32con
import sys, os
import time
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
}


# World
world_URL = "https://www.worldometers.info/coronavirus/"
world_page = requests.get(world_URL, headers=headers)
world_src = BeautifulSoup(world_page.content, "html.parser")

world = world_src.find_all(class_="maincounter-number")
world = [item.get_text().strip() for item in world]

world = world_src.find_all(class_="maincounter-number")
world = [item.get_text().strip() for item in world]

# India
india_URL = "https://www.worldometers.info/coronavirus/country/india/"
india_page = requests.get(india_URL, headers=headers)
india_src = BeautifulSoup(india_page.content, "html.parser")

india = india_src.find_all(class_="maincounter-number")
india = [item.get_text().strip() for item in india]

india = india_src.find_all(class_="maincounter-number")
india = [item.get_text().strip() for item in india]


class WindowsBalloonTip:
    def __init__(self, title, msg):
        message_map = {
            win32con.WM_DESTROY: self.OnDestroy,
        }
        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = message_map  # could also specify a wndproc.
        classAtom = RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow(
            classAtom,
            "Taskbar",
            style,
            0,
            0,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            0,
            0,
            hinst,
            None,
        )
        UpdateWindow(self.hwnd)
        iconPathName = os.path.abspath(os.path.join(sys.path[0], "balloontip.ico"))
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
            hicon = LoadImage(
                hinst, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags
            )
        except:
            hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "tooltip")
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(
            NIM_MODIFY,
            (
                self.hwnd,
                0,
                NIF_INFO,
                win32con.WM_USER + 20,
                hicon,
                "Balloon  tooltip",
                msg,
                200,
                title,
            ),
        )
        # self.show_balloon(title, msg)
        time.sleep(20)
        DestroyWindow(self.hwnd)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)  # Terminate the app.


def balloon_tip(title, msg):
    w = WindowsBalloonTip(title, msg)


if __name__ == "__main__":
    balloon_tip(
        "Covid-19 info",
        "World:\n{:10s} {:10s}\n{:10s} {:10s}\n{:10s} {:10s}\n\nIndia:\n{:10s} {:10s}\n{:10s} {:10s}\n{:10s} {:10s}\n".format(
            "Cases:",
            world[0],
            "Deaths:",
            world[1],
            "Recovered:",
            world[2],
            "Cases:",
            india[0],
            "Deaths:",
            india[1],
            "Recovered:",
            india[2],
        ),
    )
