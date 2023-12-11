import logging

import pyautogui

from bot import Dino

logging.basicConfig(level=logging.DEBUG)

dino = Dino().get_position()

dino.screenshot()
# for focus right window in my awesome i3!
pyautogui.hotkey('win', 'l')
