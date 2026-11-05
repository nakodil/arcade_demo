"""Текстовый объект с обводкой."""
from __future__ import annotations

from typing import TYPE_CHECKING

import arcade

if TYPE_CHECKING:
    from arcade.types.color import Color


class TextOutlined(arcade.Text):
    """arcade.Text с равномерной обводкой."""

    def __init__(
        self,
        text: str,
        x: float,
        y: float,
        color: Color = arcade.color.WHITE,
        font_size: float = 12,
        font_name: str | tuple[str, ...] = ("calibri", "arial"),
        anchor_x: str = "left",
        anchor_y: str = "baseline",
        outline_color: Color = arcade.color.BLACK,
        outline_width: int = 2,
        **kwargs,
    ) -> None:
        """Создает текст с обводкой."""
        super().__init__(
            text,
            x,
            y,
            color,
            font_size=font_size,
            font_name=font_name,
            anchor_x=anchor_x,
            anchor_y=anchor_y,
            **kwargs,
        )
        self.outline_width = outline_width
        self.outline = arcade.Text(
            text,
            x,
            y,
            outline_color,
            font_size=font_size,
            font_name=font_name,
            anchor_x=anchor_x,
            anchor_y=anchor_y,
            **kwargs,
        )

    def draw(self) -> None:
        """Обводка, затем основной текст."""
        # Синхронизируем обводку с актуальным состоянием
        self.outline.text = self.text
        self.outline.font_size = self.font_size
        self.outline.font_name = self.font_name

        w = self.outline_width
        for dx in range(-w, w + 1):
            for dy in range(-w, w + 1):
                if dx == 0 and dy == 0:
                    continue
                self.outline.x = self.x + dx
                self.outline.y = self.y + dy
                self.outline.draw()

        super().draw()
