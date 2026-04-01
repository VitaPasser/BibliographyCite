from typing import Dict

from ..author.authors import format_authors
from .utils.access_date import format_access_date
from .utils.clean_text import clean_text
from ...utils.finalize_entry import finalize_entry


def format_thesis(entry: Dict) -> str:
    """Форматує дисертацію згідно з Д.3-Д.4 DSTU 8302:2015"""
    parts = []

    # Автор
    author = entry.get('author', '')
    if author:
        formatted_author, _ = format_authors(author, max_authors=1)
        parts.append(formatted_author)

    # Назва і тип роботи
    title = clean_text(entry.get('title', ''))
    thesis_type = entry.get('type', '')
    if not thesis_type:
        if entry.get('ENTRYTYPE', '').lower() == 'phdthesis':
            thesis_type = 'дис. ... докт. філософії'
        else:
            thesis_type = 'дис. ... канд. наук'

    if title:
        title = title.replace('{', '').replace('}', '')
        # Об`єднуємо назву і тип через пробіл та двокрапку
        parts.append(f"{title} : {thesis_type}")

    # Місце і університет
    school = entry.get('school', '')
    address = entry.get('address', '')
    year = entry.get('year', '')

    school_parts = []
    if address and school:
        # Адреса: Університет
        school_parts.append(f"{address}: {school}")
    elif address:
        school_parts.append(address)
    elif school:
        school_parts.append(school)

    if year:
        school_parts.append(year)

    if school_parts:
        # Перші два елементи через кому
        if len(school_parts) >= 2:
            parts.append(f"{school_parts[0]}, {school_parts[1]}")
        else:
            parts.append(school_parts[0])

    # Сторінки
    pages = entry.get('pages', '')
    if not pages and 'pagetotal' in entry:
        pages = entry.get('pagetotal', '')

    if pages and pages.replace('-', '').isdigit():
        # Для дисертацій розрізняємо за школою - короткі абревіатури використовують латинську "c."
        school = entry.get('school', '')
        use_latin_c = school and len(school) <= 6  # ХНУРЕ = 5 символів
        if use_latin_c:
            parts.append(f"{pages} c.")
        else:
            parts.append(f"{pages} с.")

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