"""Модуль спрайта мыши."""

import math

import arcade

from .base_sprite import BaseSprite


class Mouse(BaseSprite):
    """Мышь."""

    def __init__(self, x: int, y: int, texture: arcade.Texture) -> None:
        """Создает мышь с центром в x y с текстурой texture."""
        super().__init__(x, y, texture)
        self.motion_speed = 200
        self.rotation_speed = 300
        self.flee_distance = 200

    def move(self, player_x: int, player_y: int) -> None:
        """Бегство или стояние на месте."""
        d_x = self.center_x - player_x
        d_y = self.center_y - player_y
        distance_to_player = math.hypot(d_x, d_y)
        if distance_to_player <= self.flee_distance:  # бегство
            angle_to_player = math.degrees(math.atan2(d_x, d_y))
            target_angle = angle_to_player + 180

            # определить, нужно ли повернуться
            diff = (target_angle - self.angle) % 360 - 180
            angle_threshold = 5
            if abs(diff) < angle_threshold:
                self.turn_direction = 0
                self.move_direction = 1
            elif diff > 0:
                self.turn_direction = 1
                self.move_direction = 0
            else:
                self.turn_direction = -1
                self.move_direction = 0
        else:
            self.move_direction = 0
            self.turn_direction = 0
