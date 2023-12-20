import cv2
import pyautogui
import mss
import mss.tools
import logging
import numpy
from .field import Field

import config
from .keyboard import Keyboard, Arrow
from core.point import Point
from core.types import Seconds
from config import (
    TIME_TO_REACH_HIGHEST_POINT as TIME_TO_UP,
    FIELD_HEIGHT,
    FIELD_VIEW_WIDTH,
    ENTITIES_DIR,
)


class Dino:
    def __init__(self):
        self.keyboard = Keyboard()
        self.speed = 1.0
        self.__position = Point(1139, 348)
        self.__logger = logging.getLogger(__name__)

    def get_position(self) -> "Dino":
        pos = self.__position or pyautogui.locateOnScreen(str(ENTITIES_DIR / 'dino.png'))
        self.__position = Point(int(pos.left), int(pos.top))
        self.__logger.debug(f'Dino found at position: {self.__position}')

        return self

    def __calc_field_view_width(self) -> int:
        return int(FIELD_VIEW_WIDTH * self.speed)

    def jump(self, switch_direction_pause: Seconds = TIME_TO_UP):
        self.keyboard.press(Arrow.UP).pause(switch_direction_pause).hold(Arrow.DOWN, hold_for=TIME_TO_UP)

    def duck(self, hold_for):
        self.keyboard.hold(Arrow.DOWN, hold_for=hold_for)

    def region(self):
        return self.__position.x, self.__position.y, int(FIELD_VIEW_WIDTH * self.speed), FIELD_HEIGHT

    def watch_ahead(self) -> Field:
        with mss.mss() as sct:
            monitor = dict(
                top=self.__position.y,
                left=self.__position.x + config.FIELD_VIEW_OFFSET,
                width=self.__calc_field_view_width(),
                height=FIELD_HEIGHT
            )
            im = numpy.array(sct.grab(monitor))
            return Field(cv2.cvtColor(im, cv2.COLOR_BGRA2GRAY))
    

    def speed_up(self): 
        self.speed += config.DINO_SPEED_ACCELERATION * int(self.speed < config.DINO_SPEED_LIMIT)
