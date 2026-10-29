"""Модуль представления загрузки ассетов."""

from __future__ import annotations

import arcade

from .base_view import BaseView


class LoadView(BaseView):
    """Представление загрузки."""

    def __init__(self) -> None:
        """Создает представление загрузки."""
        super().__init__()
        self.title_text = arcade.Text(
            "Загрузка текстур",
            self.window.width // 2,
            self.window.height // 2,
            font_size=50,
            anchor_x="center",
            anchor_y="center",
        )
        self.percentage_text = arcade.Text(
            "0",
            self.window.width // 2,
            round(self.window.height * 0.2),
            font_size=50,
            anchor_x="center",
            anchor_y="center",
        )
        self.text_objects.append(self.title_text)
        self.text_objects.append(self.percentage_text)

    def on_update(self, _: float) -> None:
        """Обновление счетчика загрузки."""
        try:
            self.percentage_text.text = str(next(self.window.loader))
        except StopIteration:  # Все ассеты загружены.
            self.percentage_text.text = "100"
            self.window.on_setup()
