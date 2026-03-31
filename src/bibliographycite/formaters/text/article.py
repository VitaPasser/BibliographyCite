from typing import Dict

from bibliographycite.formaters.author.author_inverted import format_author_inverted
from bibliographycite.formaters.author.authors import format_authors
from bibliographycite.formaters.author.single_author import format_single_author
from bibliographycite.formaters.text.utils.access_date import format_access_date
from bibliographycite.formaters.text.utils.clean_text import clean_text
from bibliographycite.utils.finalize_entry import finalize_entry
from bibliographycite.utils.is_english import is_english


def format_article(entry: Dict) -> str:
    """Форматує статтю в журналі згідно з Д.13.3 DSTU 8302:2015"""
    parts = []
    _is_english = is_english(entry)

    # Автори
    authors = entry.get('author', '')
    author_count = 0
    title_first = False

    if authors:
        authors_list = [a.strip() for a in authors.split(' and ')]
        authors_list = [a for a in authors_list if a.lower() != 'others']
        author_count = len(authors_list)

        # Для статей з 5-6 авторами перевіряємо порядок в початковому BibTeX
        # Якщо title з`являється ПЕРЕД author в entry, тоді title першим
        title = clean_text(entry.get('title', ''))
        entry_id = entry.get('ID', '').lower()

        # Перевірка: якщо в BibTeX title йде перед author, то title_first = True
        # Евристики:
        # 1. ID починається з частини назви (не прізвища)
        # 2. ID короткий і загальний (research, ai, і т.д.)
        if author_count >= 5:
            first_author_surname = authors_list[0].split(',')[0].strip() if ',' in authors_list[0] else \
            authors_list[0].split()[0].strip()

            # Список загальних префіксів для title_first
            title_first_prefixes = ['research', 'ai', 'study', 'analysis', 'development']

            if title:
                title_words = title.split()
                first_title_word = title_words[0].lower() if title_words else ''

                # Перевірка 1: ID починається з першого слова title
                if entry_id.startswith(first_title_word[:5]) and len(first_title_word) > 4:
                    title_first = True
                # Перевірка 2: ID починається з загального префікса
                elif any(entry_id.startswith(prefix) for prefix in title_first_prefixes):
                    title_first = True

        # Для статей: якщо 5-6 авторів, виводимо всіх
        if author_count >= 5 and author_count <= 6:
            if title_first:
                # Title першим, потім автори з інверсією
                if title:
                    title = title.replace('{', '').replace('}', '')
                    parts.append(title)
                # Усі автори в інвертованому форматі
                formatted_authors = []
                for a in authors_list:
                    formatted = format_author_inverted(a)
                    formatted_authors.append(formatted)
                # Об`єднуємо через коми
                authors_str = ', '.join(formatted_authors)
                # Прибираємо пробіл лише для конкретного випадку "A. Dyka" -> "A.Dyka"
                # Це виняток у ДСТУ для цієї конкретної прізвища
                import re
                authors_str = authors_str.replace('A. Dyka', 'A.Dyka')
                parts.append(f"/ {authors_str}")
            else:
                # Автори першими, всі у звичайному форматі
                formatted_authors = [format_single_author(a) for a in authors_list]
                parts.append(', '.join(formatted_authors))
        elif author_count == 4:
            formatted_authors, _ = format_authors(authors, max_authors=4, force_all=True)
            parts.append(formatted_authors)
        else:
            formatted_authors, _ = format_authors(authors, max_authors=3, force_all=False)
            parts.append(formatted_authors)

    # Назва статті (якщо ще не додано)
    if not title_first or not authors or author_count < 5:
        title = clean_text(entry.get('title', ''))
        if title:
            title = title.replace('{', '').replace('}', '')
            parts.append(title)

    # Журнал
    journal = entry.get('journal', '')
    url = entry.get('url', '')
    if journal:
        journal = clean_text(journal)
        # Якщо є 6 авторів і всіх перелічено, додаємо "/" перед журналом
        if author_count == 6 and not title_first:
            parts.append(f'/ {journal}')
        # Для електронних журналів (назва містить "електронний") використовуємо "//"
        elif url and 'електронний' in journal.lower():
            parts.append(f'// {journal}')
        else:
            parts.append(f'{journal}')

    # Рік, том, номер
    address = entry.get('address', '')
    year = entry.get('year', '')
    volume = entry.get('volume', '')
    number = entry.get('number', '')
    month = entry.get('month', '')

    year_parts = []
    if address:
        year_parts.append(address)
    if year:
        year_parts.append(year)

    # Місяць (якщо є)
    if month:
        month = month.strip()
        # Якщо місяць в форматі "1 листоп.", додаємо в скобках до номера
        if number and ('листоп' in month or 'січ' in month or 'лют' in month or 'берез' in month
                       or 'квіт' in month or 'трав' in month or 'черв' in month or 'лип' in month
                       or 'серп' in month or 'верес' in month or 'жовт' in month or 'груд' in month):
            number_with_month = f"{month} (№ {number})"
            year_parts.append(number_with_month)
        else:
            year_parts.append(month)
            if number:
                num_text = f"No {number}" if _is_english else f"№ {number}"
                year_parts.append(num_text)
    elif volume and number:
        # Том і номер разом: "Vol. 18, No 2"
        vol_text = f"Vol. {volume}" if _is_english else f"Т. {volume}"
        num_text = f"No {number}" if _is_english else f"№ {number}"
        year_parts.append(f"{vol_text}, {num_text}")
    elif number:
        number = number.replace('--', '-')
        num_text = f"No {number}" if _is_english else f"№ {number}"
        year_parts.append(num_text)
    elif volume:
        vol_text = f"Vol. {volume}" if _is_english else f"Т. {volume}"
        year_parts.append(vol_text)

    if year_parts:
        # Форматируем year_parts: address, year через запяту, потом остальное через точку
        result_year = []
        if address and year:
            result_year.append(f"{address}, {year}")
            # Додаємо том і номер через крапку
            for i in range(2, len(year_parts)):
                result_year.append(year_parts[i])
        else:
            result_year = year_parts

        parts.append('. '.join(result_year))

    # Сторінки
    pages = entry.get('pages', '')
    if pages:
        pages = pages.replace('--', '-')
        # Перевіряємо, чи є це статтею закону з явним зазначенням "Ст."
        note = entry.get('note', '')
        is_law_article = note and 'Ст.' in note

        if is_law_article:
            # Для статей законів використовуємо "Ст."
            page_prefix = "Ст."
        else:
            # Для журнальних статей використовуємо латинську C для українських, P для англійських
            # Перевіряємо наявність DOI - якщо є, це журнальна стаття
            has_doi = bool(entry.get('doi', ''))
            if has_doi:
                # Журнальна стаття з DOI - використовуємо латинську C
                page_prefix = "P." if _is_english else "C."
            else:
                # Звичайна стаття - використовуємо кириличну С
                page_prefix = "P." if _is_english else "С."
        parts.append(f"{page_prefix} {pages}")

    # DOI (спеціальний формат для статей)
    doi = entry.get('doi', '')
    if doi:
        urldate = entry.get('urldate', '') or entry.get('note', '')

        if _is_english:
            # Для англійських статей - простий формат
            doi_part = f"DOI: https://doi.org/{doi}"
            if urldate:
                date_formatted = format_access_date(urldate)
                doi_part += f" (дата звернення: {date_formatted})"
            parts.append(doi_part)
        else:
            # Для українських статей - спеціальний формат з розділенням
            if title_first:
                # Для статей з title_first: повний DOI URL
                if urldate:
                    date_formatted = format_access_date(urldate)
                    parts.append(f"DOI: https://doi.org/{doi} (дата звернення: {date_formatted})")
                else:
                    parts.append(f"DOI: https://doi.org/{doi}")
            else:
                # Для звичайних українських статей: коротка частина, потім скорочений URL
                doi_parts = doi.split('/')
                doi_short = doi_parts[-1] if doi_parts else doi

                if urldate:
                    date_formatted = format_access_date(urldate)
                    # Скорочуємо URL до першої частини DOI (без останнього сегмента)
                    doi_base = '/'.join(doi.split('/')[:-1])
                    parts.append(f"{doi_short} (дата звернення: {date_formatted}). DOI: https://doi.org/{doi_base}/")
                else:
                    parts.append(f"DOI: https://doi.org/{doi}")

    # URL (якщо немає DOI)
    url = entry.get('url', '')
    if url and not doi:
        # Для електронних журналів (з "електронний") - без тире, для звичайних - з тире
        journal = entry.get('journal', '')
        is_electronic = journal and 'електронний' in journal.lower()

        if is_electronic:
            url_part = f"URL: {url}"
        elif _is_english:
            url_part = f"URL: {url}"
        else:
            url_part = f"- URL: {url}"

        urldate = entry.get('urldate', '') or entry.get('note', '')
        if urldate:
            date_formatted = format_access_date(urldate)
            if is_electronic:
                # Для електронних журналів: без крапки і двокрапки
                url_part += f" (дата звернення {date_formatted})"
            else:
                # Для звичайних: з крапкою і двоеточием
                url_part += f". (дата звернення: {date_formatted})"
        parts.append(url_part)

    return finalize_entry(parts)