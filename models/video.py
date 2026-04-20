"""Модель данных для видео и его ключевых метрик."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Video:
    """Описывает видео и показатели, используемые в отчётах."""

    title: str
    ctr: float
    retention_rate: float
