"""Модуль базового представления - родительского для всех."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

    from core import App
    from sprites import BaseSprite, Button

import arcade

import utils


class BaseView(arcade.View, ABC):
    """Базовое представление."""

    window: App

    @abstractmethod
    def __init__(self, bg_name: str = "") -> None:
        """Создает базовое представление без фона."""
        super().__init__()
        self.sound_manager = self.window.sound_manager
        self.bg_sprites = arcade.SpriteList()
        self.sprites: arcade.SpriteList[BaseSprite] = arcade.SpriteList()
        self.text_objects: list[arcade.Text] = []
        if bg_name:
            self.make_bg(bg_name)
        self.buttons_callbacks: dict[str, Callable] = {}
        self.buttons: arcade.SpriteList[Button] = arcade.SpriteList()

    def make_bg(self, bg_name: str) -> None:
        """Создает фон."""
        bg_x = self.window.width // 2
        bg_y = self.window.height // 2
        bg_texture = self.window.textures[bg_name]
        bg = arcade.Sprite()
        bg.texture = bg_texture
        bg.center_x = bg_x
        bg.center_y = bg_y
        bg.scale = utils.get_scale(
            self.window.width,
            self.window.height,
            bg.texture.width,
            bg.texture.height,
        )
        self.bg_sprites.append(bg)

    def on_draw(self) -> None:
        """Отрисовывает все объекты на экране.

        Фоны
        Спрайты
        Текстовые объекты
        Кнопки
        """
        self.clear()
        self.bg_sprites.draw()
        self.sprites.draw()
        for text_object in self.text_objects:
            text_object.draw()
        for button in self.buttons:
            button.draw()

    def on_update(self, _: float) -> None:
        """Обновляет менеджер звуков."""
        self.sound_manager.update()
