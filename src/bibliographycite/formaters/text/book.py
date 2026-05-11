from typing import Dict

from bibliographycite.formaters.author.author_inverted import format_author_inverted, format_author_inverted_fullname
from bibliographycite.formaters.author.single_author import format_single_author
from bibliographycite.formaters.author.single_author_genitive import format_single_author_genitive
from bibliographycite.formaters.editor.handle_editors_no_author import handle_editors_no_author
from bibliographycite.formaters.editor.get_editor_type import get_editor_type
from bibliographycite.formaters.editor.handle_editors_with_authors import handle_editors_with_authors
from bibliographycite.formaters.text.edition import format_edition
from bibliographycite.formaters.text.utils.abbreviate_publisher import abbreviate_publisher
from bibliographycite.formaters.text.utils.access_date import format_access_date
from bibliographycite.formaters.text.utils.clean_text import clean_text
from bibliographycite.utils.finalize_entry import finalize_entry
from bibliographycite.utils.is_english import is_english
from bibliographycite.utils.is_odesa_polytech_style import is_odesa_polytech_style


def format_book(entry: Dict) -> str:
    """Форматує книгу згідно з Д.1 DSTU 8302:2015"""
    parts = []
    _is_english = is_english(entry)
    _is_odesa_polytech_style = is_odesa_polytech_style(entry)

    # Автори
    authors_str = entry.get('author', '')
    authors_list = []
    author_count = 0
    is_organization_author = False

    if authors_str:
        authors_raw = [a.strip() for a in authors_str.split(' and ')]
        # Перевіряємо наявність "others"
        has_others = any(a.lower() == 'others' for a in authors_raw)
        # Фільтруємо "others"
        authors_list = [a for a in authors_raw if a.lower() != 'others']
        author_count = len(authors_list)

        # Перевіряємо, чи є автор організацією (немає коми в імені)
        if author_count == 1 and ',' not in authors_list[0]:
            # Може бути організація на кшталт "Верховна Рада України"
            author_text = authors_list[0]
            # Якщо містить типові слова організацій
            if any(word in author_text for word in ['Рада', 'Інститут', 'Університет', 'Міністерство', 'Комітет']):
                is_organization_author = True

        # Якщо є "others", це означає 5+ авторів
        if has_others and author_count <= 4:
            author_count = 5

    # Назва + тип
    title = clean_text(entry.get('title', ''))
    subtitle = clean_text(entry.get('subtitle', ''))
    if _is_odesa_polytech_style:
        subtitle = (subtitle[0].lower() + subtitle[1:]) if len(subtitle) > 1 else ''
    book_type = clean_text(entry.get('type', ''))
    note = entry.get('note', '')
    volume = entry.get('volume', '')

    # Перевіряємо, чи є том у назві (для Дендрофлора України)
    title_has_volume = 'т.' in title.lower() or 'т. ' in title.lower() or 'Т.' in title or 'Т. ' in title

    if title:
        title = title.replace('{', '').replace('}', '')

        # Якщо є note "у 6 т." або подібне, додаємо до назви
        if note and ('у ' in note and 'т.' in note):
            title_full = f"{title} : {note}"
        elif subtitle and not volume:
            # Subtitle додається до назви лише якщо немає volume (не багатотомне видання)
            subtitle = subtitle.replace('{', '').replace('}', '')
            if book_type:
                title_full = f"{title} : {subtitle} : {book_type}"
            else:
                title_full = f"{title} : {subtitle}"
        elif book_type:
            title_full = f"{title} : {book_type}"
        else:
            title_full = title

        # Додаємо note до title, якщо це додаткова інформація (станом на...)
        if note and ('станом на' in note or 'стан на' in note):
            title_full = f"{title_full} : {note}"
    else:
        title_full = ''

    # Логіка для авторів
    if title_has_volume and author_count >= 1:
        # Назва містить інформацію про том - назва першою
        parts.append(title_full)
        first_author = format_author_inverted(authors_list[0])
        parts.append(f"/ {first_author}")
    elif is_organization_author:
        # Автор - організація, назва першою
        parts.append(title_full)
        parts.append(f"/ {authors_list[0]}")
    elif author_count >= 1 and author_count <= 3:
        # 1-3 автора
        formatted_authors = ', '.join([format_single_author(a) for a in authors_list])
        parts.append(formatted_authors)
        parts.append(title_full)
        if _is_odesa_polytech_style:
            parts.append(f"/ {', '.join([format_author_inverted_fullname(a) for a in authors_list])}")

    elif author_count == 4:
        # 4 автора - назва перша, потім автори в звичайному форматі Прізвище І.О.
        parts.append(title_full)
        all_authors = [format_single_author(a) for a in authors_list]
        parts.append(f"/ {', '.join(all_authors)}")

    elif author_count >= 5:
        # 5+ авторів - назва перша, потім перший + та ін./et al.
        parts.append(title_full)
        first_author = format_single_author(authors_list[0])
        if _is_english:
            parts.append(f"/ {first_author} et al.")
        else:
            parts.append(f"/ {first_author} та ін.")
    else:
        # Без авторів
        if title_full:
            parts.append(title_full)

    # Редактор
    editor = entry.get('editor', '')
    note = entry.get('note', '')

    if editor and author_count >= 1 and author_count <= 3 and not title_has_volume:
        editors = [e.strip() for e in editor.split(' and ')]
        editors = [e for e in editors if e.lower() != 'others']
        etype = get_editor_type(entry)

        if not etype and _is_english:
            etype = 'ed. by'
        elif not etype:
            etype = 'ред.'

        if _is_odesa_polytech_style:
            formatted_editors = [format_author_inverted_fullname(e) for e in editors]
            formatted_editor = ', '.join(formatted_editors)
            parts.append(f"; {etype} {formatted_editor}")
        else:
            formatted_editors = [format_author_inverted(e) for e in editors]
            formatted_editor = ', '.join(formatted_editors)
            parts.append(f"/ {etype} {formatted_editor}")

    elif editor and (author_count == 4 or author_count >= 5) and not title_has_volume:
        # Обробка редакторів для 4+ авторів
        handle_editors_with_authors(entry, parts, note)

    elif editor and author_count == 0:
        # Обробка редакторів без авторів
        # Спочатку перевіряємо, чи є note з організацією (не є типом редактора)
        editor_types = ['редкол.', 'заг. ред.', 'ред.', 'упоряд.', 'уклад.', 'голов. ред.']
        editortype = entry.get('editortype', '').strip()
        is_volume_note = note and ('у ' in note and 'т.' in note)
        has_editor_type = (editortype or
                           (note and any(keyword in note.lower() for keyword in editor_types)))

        if note and not has_editor_type and not is_volume_note:
            # Note містить організацію
            parts.append(f"/ {note}")
            # Тепер перевіряємо editor для "за заг. ред."
            if editor:
                editors_list = [e.strip() for e in editor.split(' and ')]
                editors_list = [e for e in editors_list if e.lower() != 'others']
                if editors_list:
                    editor_name = format_single_author_genitive(editors_list[0])
                    parts.append(f"; за заг. ред. {editor_name}")
        elif is_volume_note and editor:
            # Для багатотомних видань: назва вже містить інформацію про том, треба додати редактора
            etype = get_editor_type(entry)
            if not etype:
                etype = 'голов. ред.'
            handle_editors_no_author(entry, parts, etype)
        else:
            etype = get_editor_type(entry)
            handle_editors_no_author(entry, parts, etype if etype else note)
    elif not editor and author_count == 0 and note:
        # Немає авторів і редакторів, але є note з інформацією
        if 'упоряд.' in note or 'уклад.' in note:
            parts.append(f"/ {note}")

    # Видання
    edition = entry.get('edition', '')
    if edition:
        edition_text = format_edition(edition, _is_english)
        if note and ('переробл.' in note or 'допов.' in note):
            note_text = note.replace('заг. наук. ред.', '').replace('ред.', '').strip()
            if note_text:
                edition_text = f"{edition_text}, {note_text}"
        parts.append(edition_text)

    # Місце, видавець, рік
    publisher_parts = []
    address = entry.get('address', '')
    if address:
        if _is_odesa_polytech_style:
            publisher_parts.append('-')
        publisher_parts.append(address)

    publisher = entry.get('publisher', '')
    if publisher:
        publisher = abbreviate_publisher(publisher)
        if address:
            # Для інститутів і скорочених назв - без зайвого пробілу
            if 'Ін-т' in publisher or 'ін-т' in publisher or 'ун-т' in publisher:
                publisher_parts.append(f": {publisher}")
            else:
                publisher_parts.append(f" : {publisher}")
        else:
            publisher_parts.append(publisher)

    year = entry.get('year', '')
    if year:
        publisher_parts.append(f", {year}")

    if publisher_parts:
        # Об'єднуємо частини з пробілами, але коректно обробляємо двокрапку
        pub_text = ''
        for i, part in enumerate(publisher_parts):
            if i == 0:
                pub_text += part
            elif part.startswith(':'):
                pub_text += f' {part}'  # Без пробела перед двоеточием
            else:
                pub_text += ' ' + part  # С пробелом для остальных частей
        pub_text = pub_text.replace(' ,', ',').replace('  ', ' ')
        parts.append(pub_text)

    # Том
    if volume and not title_has_volume:
        volume_part = f"Т. {volume}"
        # Якщо є subtitle і він НЕ був включений до назви (тобто це багатотомне видання), додаємо після тому через двокрапку
        if subtitle and volume and not ('у ' in note and 'т.' in note):
            subtitle = subtitle.replace('{', '').replace('}', '')
            volume_part = f"{volume_part} : {subtitle}"
        parts.append(volume_part)

    # Сторінки
    pages = entry.get('pages', '')
    if not pages and 'pagetotal' in entry:
        pages = entry.get('pagetotal', '')

    if pages:
        # Для багатотомних видань з діапазоном сторінок використовується формат "С. номера"
        delimeter = ''
        if _is_odesa_polytech_style:
            delimeter = '- '
        pages = pages.replace('--', '-')
        if volume and ('-' in pages or ',' in pages):
            page_prefix = "P." if _is_english else "С."
            parts.append(f"{delimeter}{page_prefix} {pages}")
        else:
            page_unit = "p." if _is_english else "с."
            if '-' not in pages:
                parts.append(f"{delimeter}{pages} {page_unit}")
            elif pages.replace('-', '').isdigit():
                parts.append(f"{delimeter}{pages} {page_unit}")

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
    if doi and not url:
        parts.append(f"DOI: https://doi.org/{doi}")

    return finalize_entry(parts)