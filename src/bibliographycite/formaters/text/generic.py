from typing import Dict

from ..author.authors import format_authors
from .utils.access_date import format_access_date
from .utils.clean_text import clean_text
from ...utils.finalize_entry import finalize_entry


def format_generic(entry: Dict) -> str:
    """Загальний формат для невідомих типів"""
    parts = []

    # Автори
    authors = entry.get('author', '')
    if authors:
        formatted_authors, _ = format_authors(authors)
        parts.append(formatted_authors)

    # Назва
    title = clean_text(entry.get('title', ''))
    if title:
        title = title.replace('{', '').replace('}', '')
        parts.append(title)

    # Рік
    year = entry.get('year', '')
    if year:
        parts.append(year)

    # URL
    url = entry.get('url', '')
    if url:
        url_part = f"URL: {url}"
        urldate = entry.get('urldate', '') or entry.get('note', '')
        if urldate:
            date_formatted = format_access_date(urldate)
            url_part += f" (дата звернення: {date_formatted})"
        parts.append(url_part)

    return finalize_entry(parts)