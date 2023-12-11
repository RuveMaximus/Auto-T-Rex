import pyautogui
import logging
from .keyboard import Keyboard, Arrow
from core.point import Point
from config import (
    SCREENSHOT_DIR,
    BASE_DIR,
    TIME_TO_REACH_HIGHEST_POINT as TIME_TO_UP,
    FIELD_HEIGHT,
    FIELD_WIDTH,
)


class Dino:
    def __init__(self):
        self.position = None
        self.keyboard = Keyboard()
        self.logger = logging.getLogger(__name__)

    def get_position(self) -> "Dino":
        pos = pyautogui.locateOnScreen(str(BASE_DIR / 'images/dino.png'))
        self.position = Point(int(pos.left), int(pos.top))
        self.logger.debug(f'Dino found at position: {self.position}')

        return self

    def jump(self):
        self.keyboard.press(Arrow.UP).pause(TIME_TO_UP).hold(Arrow.DOWN, hold_for=TIME_TO_UP)

    def duck(self):
        self.keyboard.hold(Arrow.DOWN, hold_for=TIME_TO_UP)

    def screenshot(self):
        im = pyautogui.screenshot(region=(
            self.position.x, self.position.y,
            FIELD_WIDTH, FIELD_HEIGHT
        ))
        im.save(SCREENSHOT_DIR / 'dino.png')
