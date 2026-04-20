"""Тесты для отчёта, определяющего видео с признаками кликбейта."""

from models import Video
from reports.clickbait import ClickbaitReport


def test_clickbait_filter() -> None:
    """Проверяет фильтрацию видео по условиям кликбейт-отчёта."""
    videos = [
        Video("A", 20, 30),
        Video("B", 10, 30),
        Video("C", 20, 50),
    ]

    report = ClickbaitReport()
    result = report.generate(videos)

    assert len(result) == 1
    assert result[0].title == "A"


def test_clickbait_sorting() -> None:
    """Проверяет сортировку результата по CTR в порядке убывания."""
    videos = [
        Video("A", 18, 30),
        Video("B", 25, 20),
        Video("C", 16, 39),
    ]

    report = ClickbaitReport()
    result = report.generate(videos)

    assert [video.title for video in result] == ["B", "A", "C"]
