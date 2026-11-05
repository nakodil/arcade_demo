"""Модуль представления меню."""

from __future__ import annotations

from functools import partial

import arcade

import config
from sprites import Button, TextOutlined

from .base_view import BaseView


class MenuView(BaseView):
    """Меню."""

    def __init__(self) -> None:
        """Создает представление меню.

        Заглавная надпись
        Кнопки
        """
        super().__init__("menu_bg")

        self.title = TextOutlined(
            config.TITLE,
            self.window.width // 2,
            int(self.window.height * 0.8),
            anchor_x="center",
            anchor_y="center",
            font_name=config.FONT_TITLE,
            font_size=100,  # TODO: рассчитать от размера окна
            color=arcade.color.WHITE,
            outline_width=5,
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

        v_space = 30
        x = self.window.width // 2
        temp_y = 0  # сначала у всех кнопок одинаковый y

        temp_buttons: list[Button] = []
        for label_text, callback in self.buttons_callbacks.items():
            button = Button(
                x,
                temp_y,
                callback=callback,
                label_text=label_text,
            )
            temp_buttons.append(button)

        # Высота всего блока кнопок
        heights = [btn.height for btn in temp_buttons]
        total_height = sum(heights) + (len(heights) - 1) * v_space

        # Верхний край первой кнопки
        top = (self.window.height + total_height) / 2

        current_top = top
        for button, height in zip(temp_buttons, heights, strict=True):
            button.center_y = current_top - height / 2
            button.label.x = button.center_x
            button.label.y = button.center_y
            self.buttons.append(button)
            current_top -= height + v_space
