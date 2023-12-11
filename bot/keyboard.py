import time
import logging
import pyautogui
from enum import StrEnum
from config import (
    TIME_TO_REACH_HIGHEST_POINT
)
from core.types import Seconds


class Arrow(StrEnum):
    UP = 'up'
    DOWN = 'down'


class Keyboard:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def pause(self, s: Seconds):
        time.sleep(s)
        return self

    def press(self, key: Arrow):
        pyautogui.press(key.value)
        self.logger.debug(f'Pressed {key}')
        return self

    def hold(self, key: Arrow, hold_for: Seconds = TIME_TO_REACH_HIGHEST_POINT):
        self.logger.debug(f'Holding {key} for {hold_for} seconds...')
        with pyautogui.hold(key.value):
            time.sleep(hold_for)
