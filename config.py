from pathlib import Path

BASE_DIR = Path.cwd().absolute()
SCREENSHOT_DIR = BASE_DIR / 'screenshots'
Path.mkdir(SCREENSHOT_DIR, exist_ok=True)

TIME_TO_REACH_HIGHEST_POINT = .15
FIELD_HEIGHT = 70
FIELD_WIDTH = 700
