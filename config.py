"""Модуль конфигурации."""

import sys
from pathlib import Path

TITLE = "Шаблон игры на Arcade 3.3.3"

FPS = 60  # сколько кадров в секунду

IMG_EXTENSIONS = ["png", "jpg", "jpeg"]
SOUND_EXTENSIONS = ["mp3", "wav", "ogg"]

FONT_EXTENSIONS = ["otf", "ttf"]
FONT_TITLE = "Determination (RUS BY LYAJKA)"
FONT_BUTTON = "Determination (RUS BY LYAJKA)"
FONT_LABEL = "Determination (RUS BY LYAJKA)"

if getattr(sys, "frozen", False):  # запуск из EXE (Pyinstaller ставит frozen)
    BASE_DIR = Path(getattr(sys, "_MEIPASS", sys.executable)).resolve()
else:  # запуск из консоли
    BASE_DIR = Path(__file__).resolve().parent

ASSETS_DIR = BASE_DIR / "assets"
IMG_DIR = ASSETS_DIR / "img"
SOUND_DIR = ASSETS_DIR /  "sound"
FONT_DIR = ASSETS_DIR /  "font"
