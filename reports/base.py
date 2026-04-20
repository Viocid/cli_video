"""Базовые абстракции для генерации отчётов."""

from abc import ABC, abstractmethod

from models import Video


class BaseReport(ABC):
    """Абстрактный интерфейс для всех отчётов проекта."""

    @abstractmethod
    def generate(self, videos: list[Video]) -> list[Video]:
        """Строит отчёт по списку видео и возвращает результат."""
        raise NotImplementedError
