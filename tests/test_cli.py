"""Тесты для CLI-приложения и обработки пользовательских сценариев."""

from pathlib import Path

from main import main


def test_main_prints_clickbait_report(capsys, tmp_path: Path) -> None:
    """Проверяет успешный вывод кликбейт-отчёта в консоль."""
    csv_path = tmp_path / "stats.csv"
    csv_path.write_text(
        (
            "title,ctr,retention_rate\n"
            "Video A,17.5,35\n"
            "Video B,22,25\n"
            "Video C,10,20\n"
        ),
        encoding="utf-8",
    )

    exit_code = main(["--files", str(csv_path), "--report", "clickbait"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Video B" in captured.out
    assert "Video A" in captured.out
    assert captured.out.index("Video B") < captured.out.index("Video A")


def test_main_returns_error_for_missing_file(capsys, tmp_path: Path) -> None:
    """Проверяет возврат ошибки при отсутствии входного файла."""
    missing_path = tmp_path / "missing.csv"

    exit_code = main(["--files", str(missing_path), "--report", "clickbait"])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Файл не найден" in captured.err
