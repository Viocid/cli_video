"""Тесты для чтения CSV-файлов и валидации входных данных."""

from pathlib import Path

import pytest

from services.csv_reader import CSVReaderError, read_csv


def test_read_csv_parses_rows(tmp_path: Path) -> None:
    """Проверяет корректный разбор строк CSV в объекты видео."""
    csv_path = tmp_path / "stats.csv"
    csv_path.write_text(
        "title,ctr,retention_rate\nVideo 1,16.5,35\nVideo 2,11,41\n",
        encoding="utf-8",
    )

    videos = read_csv(csv_path)

    assert len(videos) == 2
    assert videos[0].title == "Video 1"
    assert videos[0].ctr == 16.5
    assert videos[0].retention_rate == 35.0


def test_read_csv_raises_for_missing_columns(tmp_path: Path) -> None:
    """Проверяет ошибку при отсутствии обязательных колонок."""
    csv_path = tmp_path / "stats.csv"
    csv_path.write_text("title,ctr\nVideo 1,16.5\n", encoding="utf-8")

    with pytest.raises(
        CSVReaderError, match="отсутствуют обязательные колонки"
    ):
        read_csv(csv_path)


def test_read_csv_raises_for_missing_file(tmp_path: Path) -> None:
    """Проверяет ошибку при чтении несуществующего файла."""
    missing_path = tmp_path / "missing.csv"

    with pytest.raises(CSVReaderError, match="Файл не найден"):
        read_csv(missing_path)
