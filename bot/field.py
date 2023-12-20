import cv2
import logging
from dataclasses import dataclass
from .entity import Entity


@dataclass
class Field: 
    value: list
    __logger = logging.getLogger(__name__)

    def __contains__(self, __item: Entity):
        res = cv2.matchTemplate(self.value, __item.image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)
        if max_val > .85:
            self.__logger.debug(f'Matching {__item}')
            return True
        return False