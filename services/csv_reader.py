"""Чтение CSV-файлов со статистикой видео и преобразование в модели."""

import csv
from pathlib import Path
from typing import Iterable

from models import Video

REQUIRED_COLUMNS = {"title", "ctr", "retention_rate"}


class CSVReaderError(Exception):
    """Ошибка чтения или валидации CSV-файла."""

    pass


def read_csv(file_path: Path) -> list[Video]:
    """Читает один CSV-файл и возвращает список видео."""
    if not file_path.exists():
        raise CSVReaderError(f"Файл не найден: {file_path}")
    if not file_path.is_file():
        raise CSVReaderError(f"Указанный путь не является файлом: {file_path}")

    try:
        with file_path.open(newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            missing_columns = REQUIRED_COLUMNS.difference(
                reader.fieldnames or []
            )
            if missing_columns:
                missing = ", ".join(sorted(missing_columns))
                raise CSVReaderError(
                    f"В файле {file_path}"
                    f"отсутствуют обязательные колонки: {missing}",
                )

            videos: list[Video] = []
            for row_number, row in enumerate(reader, start=2):
                try:
                    videos.append(
                        Video(
                            title=row["title"].strip(),
                            ctr=float(row["ctr"]),
                            retention_rate=float(row["retention_rate"]),
                        ),
                    )
                except (TypeError, ValueError) as error:
                    raise CSVReaderError(
                        f"Некорректные данные в файле {file_path},"
                        f"строка {row_number}: {error}",
                    ) from error
    except UnicodeDecodeError as error:
        raise CSVReaderError(
            f"Не удалось декодировать файл {file_path} в кодировке UTF-8",
        ) from error

    return videos


def read_csv_files(file_paths: Iterable[Path]) -> list[Video]:
    """Читает несколько CSV-файлов и объединяет все видео в один список."""
    videos: list[Video] = []
    for file_path in file_paths:
        videos.extend(read_csv(file_path))
    return videos
