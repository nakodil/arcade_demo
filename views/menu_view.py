"""Модуль представления меню."""

from __future__ import annotations

from functools import partial

import arcade

import config
from sprites import Button

from .base_view import BaseView


class MenuView(BaseView):
    """Меню."""

    def __init__(self) -> None:
        """Создает представление меню.

        Заглавная надпись
        Кнопки
        """
        super().__init__("menu_bg")

        self.title = arcade.Text(
            config.TITLE,
            self.window.width // 2,
            int(self.window.height * 0.9),
            anchor_x="center",
            anchor_y="center",
            font_size=100,  # TODO: рассчитать от размера окна
            color=arcade.color.BLUE,
        )
        self.text_objects.append(self.title)
        self.make_buttons()

    def on_key_press(self, symbol: int, _: int) -> None:
        """ESC: вернуться в игру (если она есть) или выйти."""
        if symbol != arcade.key.ESCAPE:
            return

        if self.window.game is not None:
            self.window.switch_view("game")

    def on_mouse_press(self, x: int, y: int, button: int, _: int) -> None:
        """Обработка нажатия левой кнопки мыши."""
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        for button_sprite in self.buttons:
            if not button_sprite.collides_with_point((x, y)):
                continue
            button_sprite.on_click()
            self.make_buttons()
            return  # Переделываем все кнопки ОДИН раз

    def make_buttons_callbacks(self) -> None:
        """Создает коллбэки для кнопок."""
        self.buttons_callbacks = {
            "новая игра": self.window.start_new_game,
        }

        if self.window.game is not None:
            self.buttons_callbacks["продолжить игру"] = partial(
            self.window.switch_view, "game",
        )

        if self.sound_manager.is_mute:
            self.buttons_callbacks["включить звук"] = partial(
                self.sound_manager.set_volume, 1.0,
            )
        else:
            self.buttons_callbacks["выключить звук"] = partial(
                self.sound_manager.set_volume, 0.0,
            )

        self.buttons_callbacks["выход"] = arcade.exit

    def make_buttons(self) -> None:
        """Создает вертикальный ряд кнопок с отступами в центре экрана."""
        self.buttons.clear()
        self.make_buttons_callbacks()

        if not self.buttons_callbacks:
            return

        # Хардкод!
        v_space = 30
        button_height = 100
        button_width = 300

        total_height = (
            len(self.buttons_callbacks) * button_height
            + (len(self.buttons_callbacks) - 1) * v_space
        )

        x = self.window.width // 2

        top = (self.window.height + total_height) // 2  # Верхний край первой кнопки
        # Центр первой (верхней) кнопки
        y = top - button_height // 2

        for label_text, callback in self.buttons_callbacks.items():
            button = Button(
                x,
                int(y),
                width=button_width,
                height=button_height,
                callback=callback,
                label_text=label_text,
            )
            self.buttons.append(button)
            y -= button_height + v_space
