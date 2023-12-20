import logging
import cv2
from pathlib import Path


class Entity:
    def __init__(self, image_path: Path, action: callable, name: str):
        self.image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
        self.name = name
        self.action = action

    def __str__(self):
        return self.name

