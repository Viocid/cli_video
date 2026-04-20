"""Отчёт для поиска видео с признаками кликбейта."""

from models import Video
from reports.base import BaseReport


class ClickbaitReport(BaseReport):
    """Отбирает видео с высоким CTR и низким удержанием."""

    CTR_THRESHOLD = 15.0
    RETENTION_THRESHOLD = 40.0

    def generate(self, videos: list[Video]) -> list[Video]:
        """Фильтрует и сортирует видео по правилам кликбейт-отчёта."""
        filtered_videos = [
            video
            for video in videos
            if video.ctr > self.CTR_THRESHOLD
            and video.retention_rate < self.RETENTION_THRESHOLD
        ]
        return sorted(
            filtered_videos, key=lambda video: video.ctr, reverse=True
        )
