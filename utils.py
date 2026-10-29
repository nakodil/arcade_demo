"""Утилиты."""

import pathlib


def get_scale(
        width_required: float,
        height_required: float,
        width_initial: float,
        height_initial: float,
    ) -> float:
    """Возвращает масштаб.

    Масштаб - множитель: наибольше из отношений
    требуемой к исходной ширине (высоте).
    """
    width_ratio = width_required / width_initial
    height_ratio = height_required / height_initial
    return max(width_ratio, height_ratio)


def get_filenames(path: pathlib.Path, extensions: list[str]) -> list[str]:
    """Возвращает имена и расширения файлов в папке."""
    files = pathlib.Path.iterdir(path)
    return [
        file.name for file in files
        if file.is_file()
        and file.suffix.lower()[1:] in extensions
    ]
