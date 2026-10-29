"""Модуль игры."""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

import arcade

from sprites import BaseSprite, Mouse, Player

if TYPE_CHECKING:
    from core.app import App


class Game:
    """Игровая сессия: состояние и логика геймплея."""

    def __init__(self, window: App) -> None:
        """Создает игру."""
        self.window = window
        self.sprites: arcade.SpriteList[BaseSprite] = arcade.SpriteList()
        self.mice: arcade.SpriteList[Mouse] = arcade.SpriteList()
        self.player: Player | None = None
        self.mice_caught_counter = 0
        self.mice_spawn_interval = 1.0
        self.mice_spawn_timer = 0.0

        self.score_text = arcade.Text(
            "0",
            window.width // 2,
            int(window.height * 0.9),
            font_size=100,
            anchor_x="center",
            anchor_y="center",
        )

    def start_new_game(self) -> None:
        """Полный сброс и подготовка новой игры."""
        self.sprites.clear()
        self.mice.clear()

        self.mice_caught_counter = 0
        self.mice_spawn_timer = 0.0

        player_x = self.window.width // 2
        player_y = self.window.height // 2
        self.player = Player(player_x, player_y, self.window.textures["player"])
        self.sprites.append(self.player)

        self.score_text.text = "0"

    def update(self, delta_time: float) -> None:
        """Обновление.

        Спавн мышей;
        Движение мышей;
        Возвращение спрайтов в границы экрана;
        Ловля мышей.
        """
        if self.player is None:
            return

        self.mice_spawn_timer += delta_time
        if self.mice_spawn_timer >= self.mice_spawn_interval:
            self.spawn_mouse()
            self.mice_spawn_timer = 0.0

        for mouse in self.mice:
            mouse.move(int(self.player.center_x), int(self.player.center_y))

        self.sprites.update(delta_time)

        for sprite in self.sprites:
            sprite.stay_inside_bounds(self.window.width, self.window.height)

        caught = arcade.check_for_collision_with_list(self.player, self.mice)
        for mouse in caught:
            self.window.sound_manager.play_sound("catch")
            mouse.remove_from_sprite_lists()
            self.mice_caught_counter += 1
            self.score_text.text = str(self.mice_caught_counter)

    def spawn_mouse(self) -> None:
        """Спавнит мышь в случайные координаты в пределах 90% размеров экрана."""
        texture = self.window.textures["mouse"]
        x = random.randint(
            int(self.window.width * 0.1),
            int(self.window.width * 0.9),
        )
        y = random.randint(
            int(self.window.height * 0.1),
            int(self.window.height * 0.9),
        )
        mouse = Mouse(x, y, texture)
        mouse.scale = 0.1
        self.sprites.append(mouse)
        self.mice.append(mouse)

    def on_key_press(self, symbol: int, _: int) -> None:
        """Управление игроком."""
        if self.player is None:
            return
        if symbol == arcade.key.D:
            self.player.turn_direction = 1
        elif symbol == arcade.key.A:
            self.player.turn_direction = -1
        elif symbol == arcade.key.W:
            self.player.move_direction = 1
        elif symbol == arcade.key.S:
            self.player.move_direction = -1

    def on_key_release(self, symbol: int, _: int) -> None:
        """Управление игроком."""
        if self.player is None:
            return
        if symbol in (arcade.key.D, arcade.key.A):
            self.player.turn_direction = 0
        if symbol in (arcade.key.W, arcade.key.S):
            self.player.move_direction = 0
