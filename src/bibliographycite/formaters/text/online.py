from typing import Dict

from bibliographycite.formaters.author.authors import format_authors
from bibliographycite.formaters.text.utils.access_date import format_access_date
from bibliographycite.formaters.text.utils.clean_text import clean_text


def format_online(entry: Dict) -> str:
    """Форматує електронний ресурс згідно з Д.12 DSTU 8302:2015"""
    parts = []

    # Автори (якщо є)
    authors = entry.get('author', '')
    if authors:
        formatted_authors, _ = format_authors(authors)
        parts.append(formatted_authors)

    # Назва
    title = clean_text(entry.get('title', ''))
    if title:
        title = title.replace('{', '').replace('}', '')
        parts.append(title)

    # URL (обов'язковий для online)
    url = entry.get('url', '')
    if url:
        need_dot = True
        if title and title.rstrip().endswith(('?', '!', '.')):
            need_dot = False

        if need_dot:
            url_part = f"{url}."
        else:
            url_part = url

        urldate = entry.get('urldate', '') or entry.get('note', '')
        if urldate:
            date_formatted = format_access_date(urldate)
            url_part += f" (дата звернення: {date_formatted})"
        parts.append(url_part)

    if not parts:
        return ""

    result_parts = []
    for i, part in enumerate(parts):
        if i == 0:
            result_parts.append(part)
        else:
            if result_parts[-1].endswith(('.', '?', '!')):
                result_parts.append(' ' + part)
            else:
                result_parts.append('. ' + part)

    result = ''.join(result_parts)
    result = result.replace('.. http', '. http')
    result = result.replace('?. http', '? http')
    result = result.replace('!. http', '! http')

    if not result.endswith('.'):
        result += '.'

    return result