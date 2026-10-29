"""Модуль представления игры."""

import arcade

from views import BaseView


class GameView(BaseView):
    """Представление игры."""

    def __init__(self) -> None:
        """Создает представление игры."""
        super().__init__("game_bg")

    def on_draw(self) -> None:
        """Отрисовка спрайтов и табло счета."""
        super().on_draw()
        game = self.window.game
        if game is None:
            return
        game.sprites.draw()
        game.score_text.draw()

    def on_update(self, delta_time: float) -> None:
        """Обновление."""
        super().on_update(delta_time)
        if self.window.game:
            self.window.game.update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        """Нажатие клавиш. ESC — в меню."""
        if symbol == arcade.key.ESCAPE:
            self.window.switch_view("menu")
            return
        if self.window.game:
            self.window.game.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        """Отпускание клавиш."""
        if self.window.game:
            self.window.game.on_key_release(symbol, modifiers)
