from typing import Dict

from ..author.author_inverted import format_author_inverted
from ..author.authors import format_authors
from ..editor.get_editor_type import get_editor_type
from .utils.abbreviate_publisher import abbreviate_publisher
from .utils.access_date import format_access_date
from .utils.clean_text import clean_text
from ...utils.finalize_entry import finalize_entry
from ...utils.is_english import is_english


def format_inbook(entry: Dict) -> str:
    """Форматує частину книги згідно з Д.13.1 DSTU 8302:2015"""
    parts = []
    _is_english = is_english(entry)

    # Автор глави
    author = entry.get('author', '')
    if author:
        formatted_author, _ = format_authors(author)
        parts.append(formatted_author)

    # Назва глави
    title = clean_text(entry.get('title', ''))
    if title:
        title = title.replace('{', '').replace('}', '')
        parts.append(title)

    # Назва книги
    booktitle = entry.get('booktitle', '')
    if booktitle:
        booktitle = clean_text(booktitle)
        # Обробка редакторів і note
        editor = entry.get('editor', '')
        note = entry.get('note', '')

        # Просто додаємо booktitle
        parts.append(booktitle)

        if editor:
            # Використовуємо інвертований формат для редакторів в inbook
            editors = [e.strip() for e in editor.split(' and ')]
            editors = [e for e in editors if e.lower() != 'others']
            formatted_editors = [format_author_inverted(e) for e in editors]
            formatted_editor = ', '.join(formatted_editors)

            etype = get_editor_type(entry)
            if not etype:
                etype = 'ed. by' if _is_english else 'ред.'

            parts.append(f"/ {etype} {formatted_editor}")

    # Видавнича інформація
    address = entry.get('address', '')
    publisher = entry.get('publisher', '')
    year = entry.get('year', '')

    pub_parts = []
    if address:
        pub_parts.append(address)
    if publisher:
        publisher = abbreviate_publisher(publisher)
        pub_parts.append(f": {publisher}" if address else publisher)
    if year:
        pub_parts.append(f", {year}")

    if pub_parts:
        parts.append(''.join(pub_parts).replace(' ,', ','))

    # Сторінки
    pages = entry.get('pages', '')
    if pages:
        pages = pages.replace('--', '-')
        if _is_english:
            parts.append(f"P. {pages}")
        else:
            parts.append(f"С. {pages}")

    # URL
    url = entry.get('url', '')
    if url:
        url_part = f"URL: {url}"
        urldate = entry.get('urldate', '') or entry.get('note', '')
        if urldate and 'дата звернення' not in urldate:
            date_formatted = format_access_date(urldate)
            url_part += f" (дата звернення: {date_formatted})"
        parts.append(url_part)

    return finalize_entry(parts)