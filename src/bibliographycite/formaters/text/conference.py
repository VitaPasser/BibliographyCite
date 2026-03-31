import re
from typing import Dict

from bibliographycite.formaters.author.authors import format_authors
from bibliographycite.formaters.author.single_author import format_single_author
from bibliographycite.formaters.editor.get_editor_type import get_editor_type
from bibliographycite.formaters.text.utils.access_date import format_access_date
from bibliographycite.formaters.text.utils.clean_text import clean_text
from bibliographycite.utils.finalize_entry import finalize_entry
from bibliographycite.utils.is_english import is_english


def format_conference(entry: Dict) -> str:
    """Форматує матеріали конференції згідно з Д.13.4 DSTU 8302:2015"""
    parts = []
    _is_english = is_english(entry)

    # Автори
    authors = entry.get('author', '')
    if authors:
        formatted_authors, _ = format_authors(authors)
        parts.append(formatted_authors)

    # Назва доповіді
    title = clean_text(entry.get('title', ''))
    if title:
        title = title.replace('{', '').replace('}', '')
        parts.append(title)

    # Назва конференції
    booktitle = entry.get('booktitle', '')
    if booktitle:
        booktitle = clean_text(booktitle)
        note = entry.get('note', '')
        year = entry.get('year', '')
        editor = entry.get('editor', '')
        editortype = entry.get('editortype', '').strip()

        # Визначаємо, чи є note інформацією про дату/місце конференції
        note_is_date = note and ('р.' in note or 'р,' in note or 'Ukraine' in note
                                 or re.search(r'\b20\d\d\b', note))
        # Визначаємо, чи є editortype/note типом редактора
        editor_keywords = ['відпов. за вип.', 'відп. за вип.', 'ред.', 'упоряд.']
        note_is_editor = note and any(k in note for k in editor_keywords)
        editortype_is_editor = editortype and any(k in editortype for k in editor_keywords)

        if note_is_date:
            # Для англійських конференцій використовуємо крапку, для українських - кому
            separator = ". " if _is_english else ", "
            conf_text = f"{booktitle}{separator}{note}"
            parts.append(conf_text)
        elif (note_is_editor or editortype_is_editor) and editor:
            # note або editortype містить інформацію про редактора
            editors_list = [e.strip() for e in editor.split(' and ')]
            editors_list = [e for e in editors_list if e.lower() != 'others']
            if editors_list:
                editor_name = format_single_author(editors_list[0])
                etype = get_editor_type(entry) or (note if note_is_editor else 'ред.')
                conf_text = f"{booktitle} / {etype} {editor_name}"
                parts.append(conf_text)
            else:
                parts.append(booktitle)
        else:
            # Стара логіка
            month = entry.get('month', '')
            address = entry.get('address', '')

            conf_parts = [booktitle]
            details = []
            if month and year:
                details.append(f"{month} {year} р.")
            elif year:
                details.append(f"{year} р.")
            if address:
                details.append(address)

            if details:
                conf_parts.append(', '.join(details))

            parts.append(' : '.join(conf_parts) if len(conf_parts) > 1 else conf_parts[0])

    # Видавнича інформація (адреса, рік)
    if not (entry.get('note', '') and ('р.' in entry.get('note', '') or 'Ukraine' in entry.get('note', ''))):
        # Додаємо адресу і рік лише якщо вони не в note
        address = entry.get('address', '')
        year = entry.get('year', '')
        pub_parts = []

        if address:
            pub_parts.append(address)
        if year and address:
            pub_parts.append(year)

        if pub_parts:
            parts.append(', '.join(pub_parts))

    # Сторінки
    pages = entry.get('pages', '')
    if pages:
        pages = pages.replace('--', '-')
        page_prefix = "P." if _is_english else "С."
        # Перевіряємо формат сторінок - якщо починаються з цифри 3, прибираємо пробіл
        if pages.startswith('3'):
            parts.append(f"{page_prefix}{pages}")
        elif '-' in pages or ',' in pages:
            parts.append(f"{page_prefix} {pages}")
        else:
            parts.append(f"{page_prefix} {pages}")

    # URL
    url = entry.get('url', '')
    if url:
        url_part = f"URL: {url}"
        urldate = entry.get('urldate', '')
        if urldate:
            date_formatted = format_access_date(urldate)
            url_part += f" (дата звернення: {date_formatted})"
        parts.append(url_part)

    # DOI
    doi = entry.get('doi', '')
    if doi:
        doi_part = f"DOI: https://doi.org/{doi}"
        # Додаємо дату звернення якщо є
        if not url:
            urldate = entry.get('urldate', '')
            if urldate:
                date_formatted = format_access_date(urldate)
                doi_part += f". (дата звернення: {date_formatted})"
        parts.append(doi_part)

    return finalize_entry(parts)