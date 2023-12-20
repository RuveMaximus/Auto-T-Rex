import logging
import time
import pyautogui
import os
from threading import Thread
from config import (
    ENTITIES_DIR,
    GAME_LOOP_DELAY
)
from bot import Dino, Entity


logging.basicConfig(level=logging.INFO)

# for focus right window in my awesome i3!
pyautogui.hotkey('win', 'l', interval=0.1)
dino = Dino()
pyautogui.press('space')


entities = [
    Entity(ENTITIES_DIR / 'small_cactus_2.png', lambda: dino.jump(.1), '2 Small'),
    Entity(ENTITIES_DIR / 'small_cactus_1.png', lambda: dino.jump(.1), '1 Small'),
    Entity(ENTITIES_DIR / 'big_cactus_1.png', lambda: dino.jump(.15), '1 Big'),
    Entity(ENTITIES_DIR / 'bird.png', lambda: dino.jump(.15), 'Bird'),
]


def accelerate_speed():
    while True:
        print(f'Current speed: {dino.speed:0.3f}       ', end='\r')
        time.sleep(GAME_LOOP_DELAY)
        dino.speed_up()


def find_entity():
    while True:
        field = dino.watch_ahead()

        for entity in entities:
            if entity in field:
                entity.action()
                break

        time.sleep(GAME_LOOP_DELAY)



speed_control_thread = Thread(target=accelerate_speed)
entity_finder_thread = Thread(target=find_entity)

speed_control_thread.start()
entity_finder_thread.start()
logging.info('Dino bot started!')

try: 
    entity_finder_thread.join()
except KeyboardInterrupt:
    print('\nStopped by keyboard')
    os._exit(0)

