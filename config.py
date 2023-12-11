from pathlib import Path

BASE_DIR = Path.cwd().absolute()
ENTITIES_DIR = BASE_DIR / 'entities'
SCREENSHOT_DIR = BASE_DIR / 'screenshots'
Path.mkdir(SCREENSHOT_DIR, exist_ok=True)

TIME_TO_REACH_HIGHEST_POINT = .15
FIELD_HEIGHT = 70
FIELD_VIEW_WIDTH = 100
FIELD_VIEW_OFFSET = 60
GAME_LOOP_DELAY = 0.05
