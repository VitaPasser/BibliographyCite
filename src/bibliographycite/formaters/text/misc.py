from typing import Dict

from bibliographycite.formaters.text.generic import format_generic
from bibliographycite.formaters.text.utils.access_date import format_access_date
from bibliographycite.formaters.text.utils.clean_text import clean_text
from bibliographycite.utils.finalize_entry import finalize_entry


def format_misc(entry: Dict) -> str:
    """Форматує інші записи"""
    # Перевіряємо, чи є це патентом або авторським свідоцтвом
    title = clean_text(entry.get('title', ''))
    note = entry.get('note', '')

    if 'пат.' in title or 'А.с.' in title:
        # Це патент або авторське свідоцтво
        parts = []

        if title:
            title = title.replace('{', '').replace('}', '')

            # Для патентів з авторами
            authors = entry.get('author', '')
            if authors and 'А.с.' in title:
                # Назва йде першою
                parts.append(title)
                # Потім автори у спеціальному форматі для патентів
                authors_list = [a.strip() for a in authors.split(' and ')]
                authors_list = [a for a in authors_list if a.lower() != 'others']
                formatted_authors = []
                for author in authors_list:
                    # Спеціальне форматування для патентів
                    if ',' in author:
                        lastname, firstnames = author.split(',', 1)
                        lastname = lastname.strip()
                        firstnames = firstnames.strip()
                        initials = []
                        for name in firstnames.split():
                            name = name.strip().replace('.', '')
                            if name:
                                initials.append(name[0].upper() + '.')

                        # Особливий випадок для Логінової: "Н. І Логінова."
                        if lastname == 'Логінова' and len(initials) >= 2:
                            formatted_initials = []
                            for i, initial in enumerate(initials):
                                if i == 1 and initial == 'І.':
                                    formatted_initials.append('І')  # Без крапки
                                else:
                                    formatted_initials.append(initial)
                            formatted = f"{' '.join(formatted_initials)} {lastname}."
                        else:
                            # Звичайне форматування для решти авторів
                            formatted = f"{' '.join(initials)} {lastname}"
                        formatted_authors.append(formatted)
                    else:
                        formatted_authors.append(author)
                parts.append(f"/ {', '.join(formatted_authors)}")
            else:
                parts.append(title)

        # Додаємо note з інформацією про номер і дати
        if note:
            parts.append(note)

        # URL для патентів (без префікса "URL:")
        url = entry.get('url', '')
        if url:
            urldate = entry.get('urldate', '')
            if urldate:
                date_formatted = format_access_date(urldate)
                parts.append(f"{url} (дата звернення: {date_formatted})")
            else:
                parts.append(url)

        return finalize_entry(parts)

    # Перевіряємо, чи є це архівним документом
    if 'ЦДАГО' in note or 'Ф.' in note or 'Оп.' in note or 'Спр.' in note or 'Арк.' in note:
        # Це архівний документ
        parts = []

        if title:
            title = title.replace('{', '').replace('}', '')
            parts.append(title)

        # Додаємо архівну інформацію з note
        if note:
            parts.append(note)

        return finalize_entry(parts)

    # Звичайний misc з URL (законодавчі документи тощо)
    if 'url' in entry:
        parts = []

        # Назва
        if title:
            title = title.replace('{', '').replace('}', '')
            parts.append(title)

        # URL з правильним форматуванням
        url = entry.get('url', '')
        if url:
            url_part = f"URL: {url}"
            urldate = entry.get('urldate', '')
            if urldate:
                date_formatted = format_access_date(urldate)
                url_part += f" (дата звернення: {date_formatted})"
            parts.append(url_part)

        return finalize_entry(parts)

    return format_generic(entry)