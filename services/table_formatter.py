"""Форматирование результатов отчёта в текстовую таблицу."""

from models import Video


def format_videos_table(videos: list[Video]) -> str:
    """Преобразует список видео в таблицу для вывода в консоль."""
    headers = ["title", "ctr", "retention_rate"]
    rows = [
        [video.title, f"{video.ctr:.2f}", f"{video.retention_rate:.2f}"]
        for video in videos
    ]

    widths = [len(header) for header in headers]
    for row in rows:
        for index, cell in enumerate(row):
            widths[index] = max(widths[index], len(cell))

    formatted_rows = [
        " | ".join(
            header.ljust(widths[index]) for index, header in enumerate(headers)
        ),
        "-+-".join("-" * width for width in widths),
    ]
    formatted_rows.extend(
        " | ".join(cell.ljust(widths[index]) for index, cell in enumerate(row))
        for row in rows
    )
    return "\n".join(formatted_rows)
