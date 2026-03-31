from typing import Dict

from bibliographycite.formaters.author.authors import format_authors
from bibliographycite.formaters.text.utils.abbreviate_publisher import abbreviate_publisher
from bibliographycite.formaters.text.utils.access_date import format_access_date
from bibliographycite.formaters.text.utils.clean_text import clean_text
from bibliographycite.utils.finalize_entry import finalize_entry


def format_techreport(entry: Dict) -> str:
    """Форматує технічні звіти і стандарти"""
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

    # Note (для стандартів містить інформацію про дату дії, для препринтів - в кінці)
    note = entry.get('note', '')
    is_preprint = note and 'Препринт' in note

    # Для стандартів додаємо note відразу після назви
    if note and not is_preprint:
        parts.append(note)

    # Номер звіту
    number = entry.get('number', '')
    if number:
        parts.append(number)

    # Організація, адреса, рік
    institution = entry.get('institution', '')
    publisher = entry.get('publisher', '')
    address = entry.get('address', '')
    year = entry.get('year', '')

    pub_parts = []
    if address:
        pub_parts.append(address)

    # Використовуємо publisher якщо є, інакше institution
    org = publisher if publisher else institution
    if org:
        org = abbreviate_publisher(org)
        pub_parts.append(f" : {org}" if address else org)

    if year:
        pub_parts.append(f", {year}")

    if pub_parts:
        parts.append(''.join(pub_parts).replace(' ,', ','))

    # Сторінки
    pages = entry.get('pages', '')
    if pages:
        parts.append(f"{pages} с.")

    # Для препринтів додаємо note в дужках в кінці
    if is_preprint and note:
        parts.append(f"({note})")

    # Series (для стандартів, наприклад "Інформація та документація")
    series = entry.get('series', '')
    if series:
        parts.append(f"({series})")

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