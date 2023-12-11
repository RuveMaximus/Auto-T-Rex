import logging
import time
import pyautogui
import cv2

import config
from bot import Dino

logging.basicConfig(level=logging.DEBUG)

# for focus right window in my awesome i3!
pyautogui.hotkey('win', 'l', interval=0.4)
pyautogui.press('space')
dino = Dino().get_position()

small_cactus_2 = cv2.imread('./entities/small_cactus_2.png', cv2.IMREAD_GRAYSCALE)
small_cactus_1 = cv2.imread('./entities/small_cactus_1.png', cv2.IMREAD_GRAYSCALE)
big_cactus_1 = cv2.imread('./entities/big_cactus_1.png', cv2.IMREAD_GRAYSCALE)
pterodactil = cv2.imread('./entities/pterodactil.png', cv2.IMREAD_GRAYSCALE)
pterodactil_down = cv2.imread('./entities/pterodactil_down.png', cv2.IMREAD_GRAYSCALE)


def match(image, template):
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)
    return max_val > 0.8


print('started')

while True:
    field_img = dino.screenshot()
    if match(field_img, big_cactus_1):
        print('bc1')
        dino.jump(0.15)
    elif match(field_img, small_cactus_2):
        print('sc2')
        dino.jump(0.15)
    elif match(field_img, small_cactus_1):
        print('sc1')
        dino.jump(0.1)
    elif match(field_img, pterodactil):
        print('pterodactil in sky')
        dino.duck(0.5)
    elif match(field_img, pterodactil_down):
        print('pterodactil on floor')
        dino.jump(0.1)
    dino.speed += 0.0042 * int(dino.speed < 3.25)
    print(dino.speed)
    time.sleep(config.GAME_LOOP_DELAY)
