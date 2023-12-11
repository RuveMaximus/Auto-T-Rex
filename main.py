import time
import pyautogui
import logging

import config

from bot.keyboard import Keyboard, Arrow

logging.basicConfig(level=logging.INFO)

kb = Keyboard()

# for focus right window in my awesome i3wm!
pyautogui.hotkey('win', 'l') 


kb.press(Arrow.UP).pause(config.TIME_TO_REACH_HIGHEST_POINT).hold(Arrow.DOWN, hold_for=config.TIME_TO_REACH_HIGHEST_POINT)