"""Модуль кликабельной кнопки."""

from collections.abc import Callable

import arcade
from arcade.types.color import Color

import config


class Button(arcade.SpriteSolidColor):
    """Кнопка."""

    def __init__(
            self,
            x: int,
            y: int,
            callback: Callable,
            label_color: Color = arcade.color.BLACK,
            label_text: str = "КНОПКА",
            fill_color: Color = arcade.color.WHITE,
    ) -> None:
        """Создает кнопку - прямоугольный спрайт и текстовый объект.

        Центр в x y,
        шириной width, высотой height
        с текстом label_text цвета label_color,
        залитую цветом fill_color.
        """
        self.callback = callback
        self.label_text = label_text
        self.label = arcade.Text(
            self.label_text.upper(),
            x, y,
            label_color,
            font_size=30,
            font_name=config.FONT_BUTTON,
            anchor_x="center",
            anchor_y="center",
        )
        padding_x = 50
        padding_y = 25
        width = self.label.content_width + padding_x * 2
        height = self.label.content_height + padding_y * 2
        super().__init__(width, height, x, y, fill_color)

    def on_click(self) -> None:
        """Действие по клику."""
        self.callback()

    def draw(self) -> None:
        """Отрисовка прямоугольника и текста."""
        arcade.draw_sprite(self)
        self.label.draw()
