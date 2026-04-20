from reports.base import BaseReport
from reports.clickbait import ClickbaitReport

REPORTS: dict[str, type[BaseReport]] = {
    "clickbait": ClickbaitReport,
}

__all__ = ["BaseReport", "ClickbaitReport", "REPORTS"]
