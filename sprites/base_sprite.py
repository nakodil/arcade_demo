"""Базовый спрайт - родительский для остальных."""

import math
from abc import ABC, abstractmethod

import arcade


class BaseSprite(arcade.Sprite, ABC):
    """Базовый спрайт."""

    @abstractmethod
    def __init__(self, x: int, y: int, texture: arcade.Texture) -> None:
        """Создает базовый спрайт с центром в x y и текстурой texture."""
        super().__init__()
        self.texture = texture
        self.center_x = x
        self.center_y = y
        self.motion_speed = 200
        self.rotation_speed = 100
        self.turn_direction = 0
        self.move_direction = 0

    def __str__(self) -> str:
        """Строковое представление."""
        return f"Спрайт {self.__class__.__name__} в {self.center_x} {self.center_y}"

    def update(self, delta_time: float) -> None:
        """Обновление.

        Перемещение и поворот.
        """
        self.angle += self.turn_direction * self.rotation_speed * delta_time
        angle_rad = math.radians(self.angle)

        self.center_x += (
            math.sin(angle_rad)
            * self.move_direction
            * self.motion_speed
            * delta_time
        )
        self.center_y += (
            math.cos(angle_rad)
            * self.move_direction
            * self.motion_speed
            * delta_time
        )

    def stay_inside_bounds(self, w_width: int, w_height: int) -> None:
        """Не дает спрайту выйти за границы экрана."""
        if self.center_x > w_width:
            self.center_x = w_width
        elif self.center_x < 0:
            self.center_x = 0

        if self.center_y > w_height:
            self.center_y = w_height
        elif self.center_y < 0:
            self.center_y = 0
