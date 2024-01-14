'''Automation of the game Stack Smash - https://games.cdn.famobi.com/html5games/s/stack-smash/v030/?fg_domain=play.famobi.com&fg_aid=A1000-1&fg_uid=3ad5d684-ab8b-4730-a209-8a614030c39a&fg_pid=4638e320-4444-4514-81c4-d80a8c662371&fg_beat=440&original_ref=https%3A%2F%2Fgames.cdn.famobi.com%2Fhtml5games%2Fs%2Fstack-smash%2Fv030%2F%3Ffg_domain%3Dplay.famobi.com%26fg_aid%3DA1000-1%26fg_uid%3D3ad5d684-ab8b-4730-a209-8a614030c39a%26fg_pid%3D4638e320-4444-4514-81c4-d80a8c662371%26fg_beat%3D714'''
import pyautogui
from PIL import Image
import numpy

while True:
    pyautogui.screenshot('sshot.png', region=(664, 379, 30, 10))
    img = numpy.array(Image.open('sshot.png'), dtype=numpy.uint8)
    if list(img[0][0]) != [48, 48, 48]:
        pyautogui.click(918, 236)
