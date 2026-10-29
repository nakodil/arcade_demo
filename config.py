"""Модуль конфигурации."""

import pathlib

TITLE = "Шаблон игры на Arcade 3.3.3"

FPS = 60  # сколько кадров в секунду

IMG_EXTENSIONS = ["png", "jpg", "jpeg"]
SOUND_EXTENSIONS = ["mp3", "wav", "ogg"]

BASE_DIR = pathlib.Path(__file__).resolve().parent  # папка проекта
ASSETS_DIR = BASE_DIR / "assets"
IMG_DIR = ASSETS_DIR / "img"
SOUND_DIR = ASSETS_DIR /  "sound"
