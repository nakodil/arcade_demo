"""Модуль звука."""

from typing import TYPE_CHECKING

import arcade

if TYPE_CHECKING:
    from pyglet.media import Player


class SoundManager:
    """Менеджер звука."""

    def __init__(self) -> None:
        """Создает менеджер звуков."""
        self._volume = 1.0
        self.sounds: dict[str, arcade.Sound] = {}
        self.players: list[Player] = []

    @property
    def is_mute(self) -> bool:
        """Заглушен ли звук."""
        return self._volume == 0.0

    def set_volume(self, value: float) -> None:
        """Задает уровень громкости в пределах 0-1 каждому плееру."""
        value = max(0.0, min(1.0, value))
        self._volume = value
        for player in self.players:
            player.volume = self._volume

    def add_sound(self, name: str, sound: arcade.Sound) -> None:
        """Добавляет звук."""
        self.sounds[name] = sound

    def play_sound(self, sound_name: str) -> None:
        """Издает звук один раз."""
        sound = self.sounds.get(sound_name)
        if not sound:
            return
        player = sound.play(volume=self._volume)
        self.players.append(player)

    def play_music(self) -> None:
        """Проигрывает музыку циклично."""
        sound = self.sounds.get("music")
        if not sound:
            return
        player = sound.play(loop=True, volume=self._volume)
        self.players.append(player)

    def update(self) -> None:
        """Удаляет отыгравшие плееры."""
        self.players = [player for player in self.players if player.playing]
