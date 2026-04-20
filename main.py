"""Точка входа CLI-приложения для построения отчётов по видео."""

import argparse
import sys
from pathlib import Path
from typing import Sequence

from reports import REPORTS
from services.csv_reader import CSVReaderError, read_csv_files
from services.table_formatter import format_videos_table


def build_parser() -> argparse.ArgumentParser:
    """Создаёт и настраивает парсер аргументов командной строки."""
    parser = argparse.ArgumentParser(
        description="Анализирует метрики YouTube-канала и строит отчёты.",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Один или несколько CSV-файлов со статистикой видео.",
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=sorted(REPORTS.keys()),
        help="Название отчёта для генерации.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Запускает CLI и возвращает код завершения процесса."""
    parser = build_parser()
    args = parser.parse_args(argv)

    file_paths = [Path(file_name) for file_name in args.files]

    try:
        videos = read_csv_files(file_paths)
    except CSVReaderError as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 1

    report = REPORTS[args.report]()
    result = report.generate(videos)

    print(format_videos_table(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
