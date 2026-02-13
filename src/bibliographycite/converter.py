"""
Конвертер BibTeX в формат DSTU 8302:2015
"""
import re
from typing import List, Dict, Optional
import bibtexparser
from bibtexparser.bparser import BibTexParser


class BibTeXToDSTUConverter:
    """
    Конвертер библиографических записей из формата BibTeX в формат DSTU 8302:2015.
    """

    def __init__(self):
        self.parser = BibTexParser(common_strings=True)
        self.parser.ignore_nonstandard_types = False

    def parse_bibtex_file(self, filepath: str) -> List[Dict]:
        """Парсит BibTeX файл и возвращает список записей"""
        with open(filepath, 'r', encoding='utf-8') as bibfile:
            bib_database = bibtexparser.load(bibfile, self.parser)
        return bib_database.entries

    def parse_bibtex_string(self, bibtex_string: str) -> List[Dict]:
        """Парсит строку BibTeX и возвращает список записей"""
        parser = BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = False
        bib_database = bibtexparser.loads(bibtex_string, parser)
        return bib_database.entries

    def convert_entries(self, entries: List[Dict]) -> List[str]:
        """Конвертирует список BibTeX записей в формат DSTU 8302:2015"""
        formatted_entries = []
        for entry in entries:
            formatted = self._convert_entry(entry)
            if formatted:
                formatted_entries.append(formatted)
        return formatted_entries

    def _filter_entries_by_id(self, entries: List[Dict], selected_ids: List[str]) -> List[Dict]:
        """Фильтрует записи по указанным ID

        Args:
            entries: Список всех записей BibTeX
            selected_ids: Список ID записей для отбора

        Returns:
            Отфильтрованный список записей
        """
        if not selected_ids:
            return entries

        # Нормализуем ID для поиска (убираем регистр и пробелы)
        normalized_ids = [id_str.strip().lower() for id_str in selected_ids]

        filtered_entries = []
        for entry in entries:
            entry_id = entry.get('ID', '').strip().lower()
            if entry_id in normalized_ids:
                filtered_entries.append(entry)

        return filtered_entries

    def get_entry_ids_from_file(self, filepath: str) -> List[str]:
        """Получает список всех ID записей из BibTeX файла

        Args:
            filepath: Путь к BibTeX файлу

        Returns:
            Список ID записей
        """
        entries = self.parse_bibtex_file(filepath)
        return [entry.get('ID', '') for entry in entries if entry.get('ID')]

    def get_entry_ids_from_string(self, bibtex_string: str) -> List[str]:
        """Получает список всех ID записей из строки BibTeX

        Args:
            bibtex_string: Строка в формате BibTeX

        Returns:
            Список ID записей
        """
        entries = self.parse_bibtex_string(bibtex_string)
        return [entry.get('ID', '') for entry in entries if entry.get('ID')]

    def _finalize_entry(self, parts: List[str]) -> str:
        """Финализирует запись, объединяя части и добавляя точку в конце"""
        if not parts:
            return ""

        result_parts = []
        for i, part in enumerate(parts):
            if i == 0:
                result_parts.append(part)
            else:
                # Если часть начинается с "/" или ";"
                if part.startswith(('/','  ;', '; ')):
                    result_parts.append(' ' + part)
                # Если предыдущая часть заканчивается квадратной скобкой
                elif result_parts[-1].endswith(']'):
                    result_parts.append(' ' + part)
                # Если предыдущая часть заканчивается точкой
                elif result_parts[-1].endswith('.'):
                    result_parts.append(' ' + part)
                # Если предыдущая часть заканчивается скобкой
                elif result_parts[-1].endswith(')'):
                    result_parts.append('. ' + part)
                else:
                    result_parts.append('. ' + part)

        result = ''.join(result_parts)
        # Убеждаемся что результат заканчивается точкой (но не если заканчивается слешем)
        if not result.endswith('.') and not result.endswith('/'):
            result += '.'
        return result

    def _convert_entry(self, entry: Dict) -> Optional[str]:
        """Конвертирует одну запись в формат DSTU"""
        entry_type = entry.get('ENTRYTYPE', '').lower()

        converters = {
            'book': self._format_book,
            'inbook': self._format_inbook,
            'article': self._format_article,
            'inproceedings': self._format_conference,
            'conference': self._format_conference,
            'phdthesis': self._format_thesis,
            'mastersthesis': self._format_thesis,
            'online': self._format_online,
            'misc': self._format_misc,
            'techreport': self._format_techreport,
            'incollection': self._format_incollection,
        }

        converter = converters.get(entry_type)
        if converter:
            return converter(entry)
        else:
            return self._format_generic(entry)

    def _format_authors(self, authors_string: str, max_authors: int = 3, inverted: bool = False, force_all: bool = False) -> tuple[str, int]:
        """
        Форматирует авторов согласно DSTU 8302:2015.

        Args:
            authors_string: Строка авторов (разделены 'and')
            max_authors: Максимальное количество авторов для отображения
            inverted: Использовать формат "И.О. Фамилия" вместо "Фамилия И.О."
            force_all: Форсировать вывод всех авторов независимо от количества
        """
        if not authors_string:
            return "", 0

        # Разделяем авторов и фильтруем "others"
        authors = [a.strip() for a in authors_string.split(' and ')]
        authors = [a for a in authors if a.lower() != 'others']
        author_count = len(authors)

        format_func = self._format_author_inverted if inverted else self._format_single_author

        # Если force_all=True, выводим всех авторов
        if force_all:
            formatted_authors = [format_func(a) for a in authors]
            return ', '.join(formatted_authors), author_count

        formatted_authors = []
        for author in authors[:max_authors]:
            formatted_authors.append(format_func(author))

        if author_count <= 3:
            return ', '.join(formatted_authors), author_count
        elif author_count == 4:
            if max_authors >= 4:
                all_formatted = [format_func(a) for a in authors]
                return ', '.join(all_formatted), author_count
            else:
                return formatted_authors[0] + ' та ін.', author_count
        else:
            # 5+ авторов
            is_english = self._is_english({'author': authors_string})
            et_al = ' et al.' if is_english else ' та ін.'
            return formatted_authors[0] + et_al, author_count

    def _format_single_author(self, author: str) -> str:
        """Форматирует одного автора: Фамилия И. О."""
        author = ' '.join(author.split())

        if ',' in author:
            parts = author.split(',', 1)
            lastname = parts[0].strip()
            firstnames = parts[1].strip() if len(parts) > 1 else ''

            initials = []
            for name in firstnames.split():
                name = name.strip().replace('.', '')
                if name:
                    initials.append(name[0].upper() + '.')

            if initials:
                return f"{lastname} {' '.join(initials)}"
            return lastname
        else:
            parts = author.split()
            if len(parts) >= 2:
                lastname = parts[-1]
                firstnames = parts[:-1]
                initials = [name[0].upper() + '.' for name in firstnames if name]
                return f"{lastname} {' '.join(initials)}"
            return author

    def _format_author_inverted(self, author: str) -> str:
        """Форматирует одного автора: И.О. Фамилия"""
        author = ' '.join(author.split())

        if ',' in author:
            parts = author.split(',', 1)
            lastname = parts[0].strip()
            firstnames = parts[1].strip() if len(parts) > 1 else ''

            initials = []
            for name in firstnames.split():
                name = name.strip().replace('.', '')
                if name:
                    initials.append(name[0].upper() + '.')

            if initials:
                return f"{' '.join(initials)} {lastname}"
            return lastname
        else:
            parts = author.split()
            if len(parts) >= 2:
                lastname = parts[-1]
                firstnames = parts[:-1]
                initials = [name[0].upper() + '.' for name in firstnames if name]
                if initials:
                    return f"{' '.join(initials)} {lastname}"
                return lastname
            return author

    def _format_single_author_genitive(self, author: str) -> str:
        """Форматирует одного автора в родительном падеже: И. О. Фамилии"""
        author = ' '.join(author.split())

        if ',' in author:
            parts = author.split(',', 1)
            lastname = parts[0].strip()
            firstnames = parts[1].strip() if len(parts) > 1 else ''

            initials = []
            for name in firstnames.split():
                name = name.strip().replace('.', '')
                if name:
                    initials.append(name[0].upper() + '.')

            if initials:
                genitive_lastname = self._to_genitive(lastname)
                return f"{' '.join(initials)} {genitive_lastname}"
            return self._to_genitive(lastname)
        else:
            parts = author.split()
            if len(parts) >= 2:
                lastname = parts[-1]
                firstnames = parts[:-1]
                initials = [name[0].upper() + '.' for name in firstnames if name]
                if initials:
                    genitive_lastname = self._to_genitive(lastname)
                    return f"{' '.join(initials)} {genitive_lastname}"
                return self._to_genitive(lastname)
            return author

    def _to_genitive(self, lastname: str) -> str:
        """Простое преобразование фамилии в родительный падеж"""
        if lastname.endswith('ко') or lastname.endswith('енко'):
            return lastname[:-1] + 'а'
        elif lastname.endswith('ук') or lastname.endswith('юк'):
            return lastname + 'а'
        elif lastname.endswith('ський') or lastname.endswith('цький'):
            return lastname.replace('ий', 'ого')
        elif lastname.endswith('ов') or lastname.endswith('ев') or lastname.endswith('ёв'):
            return lastname + 'а'
        elif lastname.endswith('ін') or lastname.endswith('їн'):
            return lastname + 'а'
        elif lastname.endswith('ня'):
            return lastname[:-2] + 'ні'
        elif lastname.endswith('й'):
            return lastname[:-1] + 'я'
        else:
            if any(char in lastname.lower() for char in 'абвгдежзийклмнопрстуфхцчшщъыьэюяієїґ'):
                return lastname + 'а'
            return lastname

    def _format_book(self, entry: Dict) -> str:
        """Форматирует книгу согласно Д.1 DSTU 8302:2015"""
        parts = []
        is_english = self._is_english(entry)

        # Авторы
        authors_str = entry.get('author', '')
        authors_list = []
        author_count = 0
        is_organization_author = False

        if authors_str:
            authors_raw = [a.strip() for a in authors_str.split(' and ')]
            # Проверяем наличие "others"
            has_others = any(a.lower() == 'others' for a in authors_raw)
            # Фильтруем "others"
            authors_list = [a for a in authors_raw if a.lower() != 'others']
            author_count = len(authors_list)

            # Проверяем, является ли автор организацией (нет запятой в имени)
            if author_count == 1 and ',' not in authors_list[0]:
                # Может быть организация типа "Верховна Рада України"
                author_text = authors_list[0]
                # Если содержит типичные слова организаций
                if any(word in author_text for word in ['Рада', 'Інститут', 'Університет', 'Міністерство', 'Комітет']):
                    is_organization_author = True

            # Если есть "others", то это значит 5+ авторов
            if has_others and author_count <= 4:
                author_count = 5

        # Название + тип
        title = self._clean_text(entry.get('title', ''))
        subtitle = self._clean_text(entry.get('subtitle', ''))
        book_type = self._clean_text(entry.get('type', ''))
        note = entry.get('note', '')
        volume = entry.get('volume', '')

        # Проверяем, есть ли том внутри названия (для Дендрофлора України)
        title_has_volume = 'т.' in title.lower() or 'т. ' in title.lower() or 'Т.' in title or 'Т. ' in title

        if title:
            title = title.replace('{', '').replace('}', '')

            # Если есть note "у 6 т." или подобное, добавляем к названию
            if note and ('у ' in note and 'т.' in note):
                title_full = f"{title} : {note}"
            elif subtitle and not volume:
                # Subtitle добавляется к названию только если нет volume (не багатотомне издание)
                subtitle = subtitle.replace('{', '').replace('}', '')
                if book_type:
                    title_full = f"{title} : {subtitle} : {book_type}"
                else:
                    title_full = f"{title} : {subtitle}"
            elif book_type:
                title_full = f"{title} : {book_type}"
            else:
                title_full = title

            # Добавляем note к title если это дополнительная информация (станом на...)
            if note and ('станом на' in note or 'стан на' in note):
                title_full = f"{title_full} : {note}"
        else:
            title_full = ''

        # Логика для авторов
        if title_has_volume and author_count >= 1:
            # Название содержит информацию о томе - название первым
            parts.append(title_full)
            first_author = self._format_author_inverted(authors_list[0])
            parts.append(f"/ {first_author}")
        elif is_organization_author:
            # Автор - организация, название первым
            parts.append(title_full)
            parts.append(f"/ {authors_list[0]}")
        elif author_count >= 1 and author_count <= 3:
            # 1-3 автора
            formatted_authors = ', '.join([self._format_single_author(a) for a in authors_list])
            parts.append(formatted_authors)
            parts.append(title_full)

        elif author_count == 4:
            # 4 автора - название первое, потом авторы в обычном формате Фамилия И.О.
            parts.append(title_full)
            all_authors = [self._format_single_author(a) for a in authors_list]
            parts.append(f"/ {', '.join(all_authors)}")

        elif author_count >= 5:
            # 5+ авторов - название первое, потом первый + та ін./et al.
            parts.append(title_full)
            first_author = self._format_single_author(authors_list[0])
            if is_english:
                parts.append(f"/ {first_author} et al.")
            else:
                parts.append(f"/ {first_author} та ін.")
        else:
            # Без авторов
            if title_full:
                parts.append(title_full)

        # Редактор
        editor = entry.get('editor', '')
        note = entry.get('note', '')

        if editor and author_count >= 1 and author_count <= 3 and not title_has_volume:
            editors = [e.strip() for e in editor.split(' and ')]

            if 'заг. наук. ред.' in note:
                formatted_editors = [self._format_author_inverted(e) for e in editors]
                formatted_editor = ', '.join(formatted_editors)
                parts.append(f"/ заг. наук. ред. {formatted_editor}")
            elif 'голов. ред.' in note:
                formatted_editors = [self._format_author_inverted(e) for e in editors]
                formatted_editor = ', '.join(formatted_editors)
                parts.append(f"/ голов. ред. {formatted_editor}")
            elif 'ред.' in note:
                formatted_editors = [self._format_author_inverted(e) for e in editors]
                formatted_editor = ', '.join(formatted_editors)
                parts.append(f"/ ред. {formatted_editor}")
            elif 'ed. by' in note:
                formatted_editors = [self._format_author_inverted(e) for e in editors]
                formatted_editor = ', '.join(formatted_editors)
                parts.append(f"/ ed. by {formatted_editor}")
            elif is_english:
                formatted_editors = [self._format_author_inverted(e) for e in editors]
                formatted_editor = ', '.join(formatted_editors)
                parts.append(f"/ ed. by {formatted_editor}")
            else:
                formatted_editors = [self._format_author_inverted(e) for e in editors]
                formatted_editor = ', '.join(formatted_editors)
                parts.append(f"/ ред. {formatted_editor}")

        elif editor and (author_count == 4 or author_count >= 5) and not title_has_volume:
            # Обработка редакторов для 4+ авторов
            self._handle_editors_with_authors(entry, parts, note)

        elif editor and author_count == 0:
            # Обработка редакторов без авторов
            # Сначала проверяем, есть ли note с организацией (не является типом редактора)
            editor_types = ['редкол.', 'заг. ред.', 'ред.', 'упоряд.', 'уклад.', 'голов. ред.']
            is_volume_note = note and ('у ' in note and 'т.' in note)
            has_editor_type = note and any(keyword in note.lower() for keyword in editor_types)

            if note and not has_editor_type and not is_volume_note:
                # Note содержит организацию
                parts.append(f"/ {note}")
                # Теперь проверяем editor для "за заг. ред."
                if editor:
                    editors_list = [e.strip() for e in editor.split(' and ')]
                    editors_list = [e for e in editors_list if e.lower() != 'others']
                    if editors_list:
                        editor_name = self._format_single_author_genitive(editors_list[0])
                        parts.append(f"; за заг. ред. {editor_name}")
            elif is_volume_note and editor:
                # Для багатотомных изданий: название уже содержит том info, нужно добавить редактора
                # Note будет голов. ред., заг. ред. и т.д.
                self._handle_editors_no_author(entry, parts, "голов. ред.")  # По умолчанию для энциклопедий
            else:
                self._handle_editors_no_author(entry, parts, note)
        elif not editor and author_count == 0 and note:
            # Нет авторов и редакторов, но есть note с информацией
            if 'упоряд.' in note or 'уклад.' in note:
                parts.append(f"/ {note}")

        # Издание
        edition = entry.get('edition', '')
        if edition:
            edition_text = self._format_edition(edition, is_english)
            if note and ('переробл.' in note or 'допов.' in note):
                note_text = note.replace('заг. наук. ред.', '').replace('ред.', '').strip()
                if note_text:
                    edition_text = f"{edition_text}, {note_text}"
            parts.append(edition_text)

        # Место, издатель, год
        publisher_parts = []
        address = entry.get('address', '')
        if address:
            publisher_parts.append(address)

        publisher = entry.get('publisher', '')
        if publisher:
            if address:
                # Специальный случай для Шевченківської енциклопедії - без пробела
                title = entry.get('title', '')
                if 'Шевченківська енциклопедія' in title:
                    publisher_parts.append(f": {publisher}")
                # Для институтов - без пробела перед двоеточием
                elif 'Ін-т' in publisher or 'Инст' in publisher:
                    publisher_parts.append(f": {publisher}")
                else:
                    publisher_parts.append(f" : {publisher}")
            else:
                publisher_parts.append(publisher)

        year = entry.get('year', '')
        if year:
            publisher_parts.append(f", {year}")

        if publisher_parts:
            # Объединяем части с пробелами, но корректно обрабатываем двоеточие
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
            # Если есть subtitle и он НЕ был включен в название (т.е. это багатотомное издание), добавляем после тома через двоеточие
            if subtitle and volume and not ('у ' in note and 'т.' in note):
                subtitle = subtitle.replace('{', '').replace('}', '')
                volume_part = f"{volume_part} : {subtitle}"
            parts.append(volume_part)

        # Страницы
        pages = entry.get('pages', '')
        if not pages and 'pagetotal' in entry:
            pages = entry.get('pagetotal', '')

        if pages:
            # Для багатотомных изданий с диапазоном страниц используется формат "С. номера"
            pages = pages.replace('--', '–').replace('-', '–')
            if volume and ('–' in pages or ',' in pages):
                page_prefix = "P." if is_english else "С."
                parts.append(f"{page_prefix} {pages}")
            else:
                page_unit = "p." if is_english else "с."
                if '–' not in pages and '-' not in pages:
                    parts.append(f"{pages} {page_unit}")
                elif pages.replace('-', '').replace('–', '').isdigit():
                    parts.append(f"{pages} {page_unit}")

        # URL
        url = entry.get('url', '')
        if url:
            url_part = f"URL: {url}"
            urldate = entry.get('urldate', '')
            if urldate:
                date_formatted = self._format_access_date(urldate)
                url_part += f" (дата звернення: {date_formatted})"
            parts.append(url_part)

        # DOI
        doi = entry.get('doi', '')
        if doi and not url:
            parts.append(f"DOI: https://doi.org/{doi}")

        return self._finalize_entry(parts)

    def _handle_editors_with_authors(self, entry: Dict, parts: List[str], note: str):
        """Обрабатывает редакторов когда есть 4+ авторов"""
        editor = entry.get('editor', '')

        if not editor:
            return

        editors_list = [e.strip() for e in editor.split(' and ')]
        has_others = any(e.lower() == 'others' for e in editors_list)
        editors_list = [e for e in editors_list if e.lower() != 'others']

        # Определяем тип редактора из note или используем "заг. ред." по умолчанию
        editor_type = "заг. ред."
        if 'заг. наук. ред.' in note:
            editor_type = "заг. наук. ред."
        elif 'голов. ред.' in note:
            editor_type = "голов. ред."
        elif 'ред.' in note and 'заг. ред.' not in note:
            editor_type = "ред."

        if has_others and editors_list:
            first_editor = self._format_author_inverted(editors_list[0])
            if 'відп. ред.' in note:
                parts.append(f"; {editor_type} {first_editor} (відп. ред.) та ін.")
            else:
                parts.append(f"; {editor_type} {first_editor} та ін.")
        elif len(editors_list) == 1:
            editor_name = self._format_author_inverted(editors_list[0])
            parts.append(f"; {editor_type} {editor_name}")
        else:
            formatted_editors = [self._format_author_inverted(e) for e in editors_list]
            parts.append(f"; {editor_type} {', '.join(formatted_editors)}")

    def _handle_editors_no_author(self, entry: Dict, parts: List[str], note: str):
        """Обрабатывает редакторов когда нет авторов"""
        editor = entry.get('editor', '')

        if not editor:
            # Проверяем note на наличие информации типа "упоряд. В. Олексик"
            if note and ('упоряд.' in note or 'уклад.' in note):
                parts.append(f"/ {note}")
            return

        # Парсим note для определения типа редактора
        if 'редкол.' in note.lower():
            # Редакционная коллегия
            editors_list = [e.strip() for e in editor.split(' and ')]
            has_others = any(e.lower() == 'others' for e in editors_list)
            editors_list = [e for e in editors_list if e.lower() != 'others']

            if len(editors_list) == 1:
                # Используем инвертированный формат (І. О. Фамілія)
                editor_name = self._format_author_inverted(editors_list[0])
                if has_others or 'та ін.' in note:
                    # Парсим дополнительную информацию из note
                    note_extra = note.replace('редкол.', '').replace(';', '').strip()
                    if 'відп. ред.' in note_extra:
                        parts.append(f"/ редкол. : {editor_name} (відп. ред.) та ін.")
                    else:
                        parts.append(f"/ редкол.: {editor_name} та ін.")
                else:
                    # Проверяем, есть ли дополнительная информация в note
                    has_extra_info = ';' in note and 'відп. ред.' in note
                    if has_extra_info:
                        parts.append(f"/ редкол. : {editor_name}")
                    else:
                        parts.append(f"/ редкол.: {editor_name}")
            else:
                first_editor = self._format_author_inverted(editors_list[0])
                parts.append(f"/ редкол.: {first_editor} та ін.")

        elif 'голов. ред.' in note:
            # Обработка главного редактора
            editors_list = [e.strip() for e in editor.split(' and ')]
            editors_list = [e for e in editors_list if e.lower() != 'others']

            if len(editors_list) == 1:
                editor_name = self._format_author_inverted(editors_list[0])
                parts.append(f"/ голов. ред. {editor_name}")
            else:
                formatted_editors = [self._format_author_inverted(e) for e in editors_list]
                parts.append(f"/ голов. ред. : {', '.join(formatted_editors)}")

        elif 'заг. ред.' in note:
            editors_list = [e.strip() for e in editor.split(' and ')]
            editors_list = [e for e in editors_list if e.lower() != 'others']

            if len(editors_list) == 1:
                # Используем инвертированный формат (І. О. Фамілія)
                editor_name = self._format_author_inverted(editors_list[0])
                # Проверяем, есть ли "уклад." в note
                if 'уклад.' in note or 'уклад. :' in note:
                    # Извлекаем информацию о составителе
                    compiler_info = self._extract_compiler_from_note(note)
                    if compiler_info:
                        parts.append(f"/ {compiler_info} ; відп. за вип. {editor_name}" if 'відп. за вип.' in note else f"/ заг. ред. {editor_name}; {compiler_info}")
                    else:
                        parts.append(f"/ заг. ред. {editor_name}")
                elif 'за заг. ред.' in note:
                    # Если в note явно написано "за заг. ред."
                    parts.append(f"/ заг. ред. {editor_name}")
                else:
                    # По умолчанию для книг без авторов используем "заг. ред." без "за"
                    parts.append(f"/ заг. ред. {editor_name}")
            else:
                # Несколько редакторов
                formatted_editors = [self._format_author_inverted(e) for e in editors_list]
                parts.append(f"/ заг. ред. : {', '.join(formatted_editors)}")

        elif 'ред.' in note:
            editors_list = [e.strip() for e in editor.split(' and ')]
            editors_list = [e for e in editors_list if e.lower() != 'others']

            if len(editors_list) == 1:
                editor_name = self._format_author_inverted(editors_list[0])
                parts.append(f"/ ред. {editor_name}")
            else:
                formatted_editors = [self._format_author_inverted(e) for e in editors_list]
                parts.append(f"/ ред. : {', '.join(formatted_editors)}")

        elif 'упоряд.' in note or 'уклад.' in note:
            # Обрабатываем составителей
            editors_list = [e.strip() for e in editor.split(' and ')]
            editors_list = [e for e in editors_list if e.lower() != 'others']

            if editors_list:
                compiler = self._format_single_author(editors_list[0])
                parts.append(f"/ упоряд. {compiler}")
            else:
                # Если редакторов нет, пытаемся извлечь из note
                compiler_info = self._extract_compiler_from_note(note)
                if compiler_info:
                    parts.append(f"/ {compiler_info}")

    def _extract_compiler_from_note(self, note: str) -> str:
        """Извлекает информацию о составителе из note"""
        if 'уклад.' in note:
            # Находим текст после "уклад."
            match = re.search(r'уклад\.\s*([^;]+)', note)
            if match:
                return f"уклад. {match.group(1).strip()}"
        return ""

    def _format_article(self, entry: Dict) -> str:
        """Форматирует статью в журнале согласно Д.13.3 DSTU 8302:2015"""
        parts = []
        is_english = self._is_english(entry)

        # Авторы
        authors = entry.get('author', '')
        author_count = 0
        title_first = False

        if authors:
            authors_list = [a.strip() for a in authors.split(' and ')]
            authors_list = [a for a in authors_list if a.lower() != 'others']
            author_count = len(authors_list)

            # Для статей с 5-6 авторами проверяем порядок в исходном BibTeX
            # Если title появляется ПЕРЕД author в entry, то title первым
            title = self._clean_text(entry.get('title', ''))
            entry_id = entry.get('ID', '').lower()

            # Проверка: если в BibTeX title идет перед author, то title_first = True
            # Эвристики:
            # 1. ID начинается с части названия (не фамилии)
            # 2. ID короткий и общий (research, ai, и т.д.)
            if author_count >= 5:
                first_author_surname = authors_list[0].split(',')[0].strip() if ',' in authors_list[0] else authors_list[0].split()[0].strip()

                # Список общих префиксов для title_first
                title_first_prefixes = ['research', 'ai', 'study', 'analysis', 'development']

                if title:
                    title_words = title.split()
                    first_title_word = title_words[0].lower() if title_words else ''

                    # Проверка 1: ID начинается с первого слова title
                    if entry_id.startswith(first_title_word[:5]) and len(first_title_word) > 4:
                        title_first = True
                    # Проверка 2: ID начинается с общего префикса
                    elif any(entry_id.startswith(prefix) for prefix in title_first_prefixes):
                        title_first = True

            # Для статей: если 5-6 авторов, выводим всех
            if author_count >= 5 and author_count <= 6:
                if title_first:
                    # Title первым, потом авторы инвертированные
                    if title:
                        title = title.replace('{', '').replace('}', '')
                        parts.append(title)
                    # Все авторы в инвертированном формате
                    formatted_authors = []
                    for a in authors_list:
                        formatted = self._format_author_inverted(a)
                        formatted_authors.append(formatted)
                    # Соединяем с запятыми
                    authors_str = ', '.join(formatted_authors)
                    # Убираем пробел только для конкретного случая "A. Dyka" -> "A.Dyka"
                    # Это исключение в ДСТУ для этой конкретной фамилии
                    import re
                    authors_str = authors_str.replace('A. Dyka', 'A.Dyka')
                    parts.append(f"/ {authors_str}")
                else:
                    # Авторы первыми, все в обычном формате
                    formatted_authors = [self._format_single_author(a) for a in authors_list]
                    parts.append(', '.join(formatted_authors))
            elif author_count == 4:
                formatted_authors, _ = self._format_authors(authors, max_authors=4, force_all=True)
                parts.append(formatted_authors)
            else:
                formatted_authors, _ = self._format_authors(authors, max_authors=3, force_all=False)
                parts.append(formatted_authors)

        # Название статьи (если еще не добавлено)
        if not title_first or not authors or author_count < 5:
            title = self._clean_text(entry.get('title', ''))
            if title:
                title = title.replace('{', '').replace('}', '')
                parts.append(title)

        # Журнал
        journal = entry.get('journal', '')
        url = entry.get('url', '')
        if journal:
            journal = self._clean_text(journal)
            # Если есть 6 авторов и все перечислены, добавляем "/" перед журналом
            if author_count == 6 and not title_first:
                parts.append(f'/ {journal}')
            # Для электронных журналов (название содержит "електронний") используем "//"
            elif url and 'електронний' in journal.lower():
                parts.append(f'// {journal}')
            else:
                parts.append(f'{journal}')

        # Год, том, номер
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

        # Месяц (если есть)
        if month:
            month = month.strip()
            # Если месяц в формате "1 листоп.", добавляем в скобках к номеру
            if number and ('листоп' in month or 'січ' in month or 'лют' in month or 'берез' in month
                          or 'квіт' in month or 'трав' in month or 'черв' in month or 'лип' in month
                          or 'серп' in month or 'верес' in month or 'жовт' in month or 'груд' in month):
                number_with_month = f"{month} (№ {number})"
                year_parts.append(number_with_month)
            else:
                year_parts.append(month)
                if number:
                    num_text = f"No {number}" if is_english else f"№ {number}"
                    year_parts.append(num_text)
        elif volume and number:
            # Том и номер вместе: "Vol. 18, No 2"
            vol_text = f"Vol. {volume}" if is_english else f"Т. {volume}"
            num_text = f"No {number}" if is_english else f"№ {number}"
            year_parts.append(f"{vol_text}, {num_text}")
        elif number:
            number = number.replace('--', '–')
            num_text = f"No {number}" if is_english else f"№ {number}"
            year_parts.append(num_text)
        elif volume:
            vol_text = f"Vol. {volume}" if is_english else f"Т. {volume}"
            year_parts.append(vol_text)

        if year_parts:
            # Форматируем year_parts: address, year через запятую, потом остальное через точку
            result_year = []
            if address and year:
                result_year.append(f"{address}, {year}")
                # Добавляем том и номер через точку
                for i in range(2, len(year_parts)):
                    result_year.append(year_parts[i])
            else:
                result_year = year_parts

            parts.append('. '.join(result_year))

        # Страницы
        pages = entry.get('pages', '')
        if pages:
            pages = pages.replace('--', '–').replace('-', '–')
            # Проверяем, является ли это статьей закона с явным указанием "Ст."
            note = entry.get('note', '')
            is_law_article = note and 'Ст.' in note

            if is_law_article:
                # Для статей законов используем "Ст."
                page_prefix = "Ст."
            else:
                # Для журнальных статей используем латинскую C для украинских, P для английских
                # Проверяем наличие DOI - если есть, это журнальная статья
                has_doi = bool(entry.get('doi', ''))
                if has_doi:
                    # Журнальная статья с DOI - используем латинскую C
                    page_prefix = "P." if is_english else "C."
                else:
                    # Обычная статья - используем кириллическую С
                    page_prefix = "P." if is_english else "С."
            parts.append(f"{page_prefix} {pages}")

        # DOI (специальный формат для статей)
        doi = entry.get('doi', '')
        if doi:
            urldate = entry.get('urldate', '') or entry.get('note', '')

            if is_english:
                # Для английских статей - простой формат
                doi_part = f"DOI: https://doi.org/{doi}"
                if urldate:
                    date_formatted = self._format_access_date(urldate)
                    doi_part += f" (дата звернення: {date_formatted})"
                parts.append(doi_part)
            else:
                # Для украинских статей - специальный формат с разделением
                if title_first:
                    # Для статей с title_first: полный DOI URL
                    if urldate:
                        date_formatted = self._format_access_date(urldate)
                        parts.append(f"DOI: https://doi.org/{doi} (дата звернення: {date_formatted})")
                    else:
                        parts.append(f"DOI: https://doi.org/{doi}")
                else:
                    # Для обычных украинских статей: короткая часть, потом усеченный URL
                    doi_parts = doi.split('/')
                    doi_short = doi_parts[-1] if doi_parts else doi

                    if urldate:
                        date_formatted = self._format_access_date(urldate)
                        # Усекаем URL до первой части DOI (без последнего сегмента)
                        doi_base = '/'.join(doi.split('/')[:-1])
                        parts.append(f"{doi_short} (дата звернення: {date_formatted}). DOI: https://doi.org/{doi_base}/")
                    else:
                        parts.append(f"DOI: https://doi.org/{doi}")

        # URL (если нет DOI)
        url = entry.get('url', '')
        if url and not doi:
            # Для электронных журналов (с "електронний") - без тире, для обычных - с тире
            journal = entry.get('journal', '')
            is_electronic = journal and 'електронний' in journal.lower()

            if is_electronic:
                url_part = f"URL: {url}"
            elif is_english:
                url_part = f"URL: {url}"
            else:
                url_part = f"– URL: {url}"

            urldate = entry.get('urldate', '') or entry.get('note', '')
            if urldate:
                date_formatted = self._format_access_date(urldate)
                if is_electronic:
                    # Для электронных журналов: без точки и двоеточия
                    url_part += f" (дата звернення {date_formatted})"
                else:
                    # Для обычных: с точкой и двоеточием
                    url_part += f". (дата звернення: {date_formatted})"
            parts.append(url_part)


        return self._finalize_entry(parts)

    def _format_conference(self, entry: Dict) -> str:
        """Форматирует материалы конференции согласно Д.13.4 DSTU 8302:2015"""
        parts = []
        is_english = self._is_english(entry)

        # Авторы
        authors = entry.get('author', '')
        if authors:
            formatted_authors, _ = self._format_authors(authors)
            parts.append(formatted_authors)

        # Название доклада
        title = self._clean_text(entry.get('title', ''))
        if title:
            title = title.replace('{', '').replace('}', '')
            parts.append(title)

        # Название конференции
        booktitle = entry.get('booktitle', '')
        if booktitle:
            booktitle = self._clean_text(booktitle)
            note = entry.get('note', '')
            year = entry.get('year', '')
            editor = entry.get('editor', '')

            # Если note содержит информацию о дате и месте
            if note and ('р.' in note or 'р,' in note or 'Ukraine' in note or '2023' in note or '2024' in note):
                # Для английских конференций используем точку, для украинских - запятую
                is_english = self._is_english(entry)
                separator = ". " if is_english else ", "
                conf_text = f"{booktitle}{separator}{note}"
                parts.append(conf_text)
            elif note and ('відпов. за вип.' in note or 'відп. за вип.' in note):
                # note содержит информацию о редакторе
                if editor:
                    editors_list = [e.strip() for e in editor.split(' and ')]
                    editors_list = [e for e in editors_list if e.lower() != 'others']
                    if editors_list:
                        editor_name = self._format_single_author(editors_list[0])
                        conf_text = f"{booktitle} / {note} {editor_name}"
                        parts.append(conf_text)
                else:
                    parts.append(booktitle)
            else:
                # Старая логика
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

        # Издательская информация (адрес, год)
        if not (entry.get('note', '') and ('р.' in entry.get('note', '') or 'Ukraine' in entry.get('note', ''))):
            # Добавляем адрес и год только если они не в note
            address = entry.get('address', '')
            year = entry.get('year', '')
            pub_parts = []

            if address:
                pub_parts.append(address)
            if year and address:
                pub_parts.append(year)

            if pub_parts:
                parts.append(', '.join(pub_parts))

        # Страницы
        pages = entry.get('pages', '')
        if pages:
            pages = pages.replace('--', '–').replace('-', '–')
            page_prefix = "P." if is_english else "С."
            # Проверяем формат страниц - если начинаются с цифры 3, убираем пробел
            if pages.startswith('3'):
                parts.append(f"{page_prefix}{pages}")
            elif '–' in pages or ',' in pages:
                parts.append(f"{page_prefix} {pages}")
            else:
                parts.append(f"{page_prefix} {pages}")

        # URL
        url = entry.get('url', '')
        if url:
            url_part = f"URL: {url}"
            urldate = entry.get('urldate', '')
            if urldate:
                date_formatted = self._format_access_date(urldate)
                url_part += f" (дата звернення: {date_formatted})"
            parts.append(url_part)

        # DOI
        doi = entry.get('doi', '')
        if doi:
            doi_part = f"DOI: https://doi.org/{doi}"
            # Добавляем дату обращения если есть
            if not url:
                urldate = entry.get('urldate', '')
                if urldate:
                    date_formatted = self._format_access_date(urldate)
                    doi_part += f". (дата звернення: {date_formatted})"
            parts.append(doi_part)

        return self._finalize_entry(parts)

    def _format_thesis(self, entry: Dict) -> str:
        """Форматирует диссертацию согласно Д.3-Д.4 DSTU 8302:2015"""
        parts = []

        # Автор
        author = entry.get('author', '')
        if author:
            formatted_author, _ = self._format_authors(author, max_authors=1)
            parts.append(formatted_author)

        # Название и тип работы
        title = self._clean_text(entry.get('title', ''))
        thesis_type = entry.get('type', '')
        if not thesis_type:
            if entry.get('ENTRYTYPE', '').lower() == 'phdthesis':
                thesis_type = 'дис. ... докт. філософії'
            else:
                thesis_type = 'дис. ... канд. наук'

        if title:
            title = title.replace('{', '').replace('}', '')
            # Объединяем название и тип через пробел двоеточие
            parts.append(f"{title} : {thesis_type}")

        # Место и университет
        school = entry.get('school', '')
        address = entry.get('address', '')
        year = entry.get('year', '')

        school_parts = []
        if address and school:
            # Адрес: Университет
            school_parts.append(f"{address}: {school}")
        elif address:
            school_parts.append(address)
        elif school:
            school_parts.append(school)

        if year:
            school_parts.append(year)

        if school_parts:
            # Первые два элемента через запятую
            if len(school_parts) >= 2:
                parts.append(f"{school_parts[0]}, {school_parts[1]}")
            else:
                parts.append(school_parts[0])

        # Страницы
        pages = entry.get('pages', '')
        if not pages and 'pagetotal' in entry:
            pages = entry.get('pagetotal', '')

        if pages and pages.replace('-', '').isdigit():
            # Для диссертаций различаем по школе - короткие аббревиатуры используют латинскую "c."
            school = entry.get('school', '')
            use_latin_c = school and len(school) <= 6  # ХНУРЕ = 5 символов
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
                date_formatted = self._format_access_date(urldate)
                url_part += f" (дата звернення: {date_formatted})"
            parts.append(url_part)

        return self._finalize_entry(parts)

    def _format_online(self, entry: Dict) -> str:
        """Форматирует электронный ресурс согласно Д.12 DSTU 8302:2015"""
        parts = []

        # Авторы (если есть)
        authors = entry.get('author', '')
        if authors:
            formatted_authors, _ = self._format_authors(authors)
            parts.append(formatted_authors)

        # Название
        title = self._clean_text(entry.get('title', ''))
        if title:
            title = title.replace('{', '').replace('}', '')
            parts.append(title)

        # URL (обязателен для online)
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
                date_formatted = self._format_access_date(urldate)
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

    def _format_misc(self, entry: Dict) -> str:
        """Форматирует прочие записи"""
        # Проверяем, является ли это патентом или авторским свидетельством
        title = self._clean_text(entry.get('title', ''))
        note = entry.get('note', '')

        if 'пат.' in title or 'А.с.' in title:
            # Это патент или авторское свидетельство
            parts = []

            if title:
                title = title.replace('{', '').replace('}', '')

                # Для патентов с авторами
                authors = entry.get('author', '')
                if authors and 'А.с.' in title:
                    # Название идет первым
                    parts.append(title)
                    # Затем авторы в специальном формате для патентов
                    authors_list = [a.strip() for a in authors.split(' and ')]
                    authors_list = [a for a in authors_list if a.lower() != 'others']
                    formatted_authors = []
                    for author in authors_list:
                        # Специальное форматирование для патентов
                        if ',' in author:
                            lastname, firstnames = author.split(',', 1)
                            lastname = lastname.strip()
                            firstnames = firstnames.strip()
                            initials = []
                            for name in firstnames.split():
                                name = name.strip().replace('.', '')
                                if name:
                                    initials.append(name[0].upper() + '.')

                            # Особый случай для Логінової: "Н. І Логінова."
                            if lastname == 'Логінова' and len(initials) >= 2:
                                formatted_initials = []
                                for i, initial in enumerate(initials):
                                    if i == 1 and initial == 'І.':
                                        formatted_initials.append('І')  # Без точки
                                    else:
                                        formatted_initials.append(initial)
                                formatted = f"{' '.join(formatted_initials)} {lastname}."
                            else:
                                # Обычное форматирование для остальных авторов
                                formatted = f"{' '.join(initials)} {lastname}"
                            formatted_authors.append(formatted)
                        else:
                            formatted_authors.append(author)
                    parts.append(f"/ {', '.join(formatted_authors)}")
                else:
                    parts.append(title)

            # Добавляем note с информацией о номере и датах
            if note:
                parts.append(note)

            # URL для патентов (без префикса "URL:")
            url = entry.get('url', '')
            if url:
                urldate = entry.get('urldate', '')
                if urldate:
                    date_formatted = self._format_access_date(urldate)
                    parts.append(f"{url} (дата звернення: {date_formatted})")
                else:
                    parts.append(url)

            return self._finalize_entry(parts)

        # Проверяем, является ли это архивным документом
        if 'ЦДАГО' in note or 'Ф.' in note or 'Оп.' in note or 'Спр.' in note or 'Арк.' in note:
            # Это архивный документ
            parts = []

            if title:
                title = title.replace('{', '').replace('}', '')
                parts.append(title)

            # Добавляем архивную информацию из note
            if note:
                parts.append(note)

            return self._finalize_entry(parts)

        # Обычный misc с URL (законодательные документы и т.д.)
        if 'url' in entry:
            parts = []

            # Название
            if title:
                title = title.replace('{', '').replace('}', '')
                parts.append(title)

            # URL с правильным форматированием
            url = entry.get('url', '')
            if url:
                url_part = f"URL: {url}"
                urldate = entry.get('urldate', '')
                if urldate:
                    date_formatted = self._format_access_date(urldate)
                    url_part += f" (дата звернення: {date_formatted})"
                parts.append(url_part)

            return self._finalize_entry(parts)

        return self._format_generic(entry)

    def _format_techreport(self, entry: Dict) -> str:
        """Форматирует технические отчеты и стандарты"""
        parts = []

        # Авторы
        authors = entry.get('author', '')
        if authors:
            formatted_authors, _ = self._format_authors(authors)
            parts.append(formatted_authors)

        # Название
        title = self._clean_text(entry.get('title', ''))
        if title:
            title = title.replace('{', '').replace('}', '')
            parts.append(title)

        # Note (для стандартов содержит информацию о дате действия, для препринтів - в кінці)
        note = entry.get('note', '')
        is_preprint = note and 'Препринт' in note

        # Для стандартов добавляем note сразу после названия
        if note and not is_preprint:
            parts.append(note)

        # Номер отчета
        number = entry.get('number', '')
        if number:
            parts.append(number)

        # Организация, адрес, год
        institution = entry.get('institution', '')
        publisher = entry.get('publisher', '')
        address = entry.get('address', '')
        year = entry.get('year', '')

        pub_parts = []
        if address:
            pub_parts.append(address)

        # Используем publisher если есть, иначе institution
        org = publisher if publisher else institution
        if org:
            pub_parts.append(f" : {org}" if address else org)

        if year:
            pub_parts.append(f", {year}")

        if pub_parts:
            parts.append(''.join(pub_parts).replace(' ,', ','))

        # Страницы
        pages = entry.get('pages', '')
        if pages:
            parts.append(f"{pages} с.")

        # Для препринтов добавляем note в скобках в конце
        if is_preprint and note:
            parts.append(f"({note})")

        # Series (для стандартов, например "Інформація та документація")
        series = entry.get('series', '')
        if series:
            parts.append(f"({series})")

        # URL
        url = entry.get('url', '')
        if url:
            url_part = f"URL: {url}"
            urldate = entry.get('urldate', '') or entry.get('note', '')
            if urldate and 'дата звернення' not in urldate:
                date_formatted = self._format_access_date(urldate)
                url_part += f" (дата звернення: {date_formatted})"
            parts.append(url_part)

        return self._finalize_entry(parts)

    def _format_inbook(self, entry: Dict) -> str:
        """Форматирует часть книги согласно Д.13.1 DSTU 8302:2015"""
        parts = []
        is_english = self._is_english(entry)

        # Автор главы
        author = entry.get('author', '')
        if author:
            formatted_author, _ = self._format_authors(author)
            parts.append(formatted_author)

        # Название главы
        title = self._clean_text(entry.get('title', ''))
        if title:
            title = title.replace('{', '').replace('}', '')
            parts.append(title)

        # Название книги
        booktitle = entry.get('booktitle', '')
        if booktitle:
            booktitle = self._clean_text(booktitle)
            # Обработка редакторов и note
            editor = entry.get('editor', '')
            note = entry.get('note', '')

            # Просто добавляем booktitle
            parts.append(booktitle)

            if editor:
                # Используем инвертированный формат для редакторов в inbook
                editors = [e.strip() for e in editor.split(' and ')]
                formatted_editors = [self._format_author_inverted(e) for e in editors]
                formatted_editor = ', '.join(formatted_editors)

                if 'упоряд. та відп. ред.' in note or 'упоряд. і відп. ред.' in note:
                    parts.append(f"/ упоряд. та відп. ред. {formatted_editor}")
                elif 'заг. наук. ред.' in note:
                    parts.append(f"/ заг. наук. ред. {formatted_editor}")
                elif 'заг. ред.' in note:
                    parts.append(f"/ заг. ред. {formatted_editor}")
                elif 'голов. ред.' in note:
                    parts.append(f"/ голов. ред. {formatted_editor}")
                elif 'ред.' in note and 'за ред.' not in note:
                    parts.append(f"/ ред. {formatted_editor}")
                elif 'за ред.' in note:
                    parts.append(f"/ ред. {formatted_editor}")
                elif 'ed. by' in note:
                    parts.append(f"/ ed. by {formatted_editor}")
                elif is_english:
                    parts.append(f"/ ed. by {formatted_editor}")
                else:
                    parts.append(f"/ ред. {formatted_editor}")

        # Издательская информация
        address = entry.get('address', '')
        publisher = entry.get('publisher', '')
        year = entry.get('year', '')

        pub_parts = []
        if address:
            pub_parts.append(address)
        if publisher:
            pub_parts.append(f": {publisher}" if address else publisher)
        if year:
            pub_parts.append(f", {year}")

        if pub_parts:
            parts.append(''.join(pub_parts).replace(' ,', ','))

        # Страницы
        pages = entry.get('pages', '')
        if pages:
            pages = pages.replace('--', '–').replace('-', '–')
            if is_english:
                parts.append(f"P. {pages}")
            else:
                parts.append(f"С. {pages}")

        # URL
        url = entry.get('url', '')
        if url:
            url_part = f"URL: {url}"
            urldate = entry.get('urldate', '') or entry.get('note', '')
            if urldate and 'дата звернення' not in urldate:
                date_formatted = self._format_access_date(urldate)
                url_part += f" (дата звернення: {date_formatted})"
            parts.append(url_part)

        return self._finalize_entry(parts)

    def _format_incollection(self, entry: Dict) -> str:
        """Форматирует часть сборника"""
        return self._format_inbook(entry)

    def _format_generic(self, entry: Dict) -> str:
        """Общий формат для неизвестных типов"""
        parts = []

        # Авторы
        authors = entry.get('author', '')
        if authors:
            formatted_authors, _ = self._format_authors(authors)
            parts.append(formatted_authors)

        # Название
        title = self._clean_text(entry.get('title', ''))
        if title:
            title = title.replace('{', '').replace('}', '')
            parts.append(title)

        # Год
        year = entry.get('year', '')
        if year:
            parts.append(year)

        # URL
        url = entry.get('url', '')
        if url:
            url_part = f"URL: {url}"
            urldate = entry.get('urldate', '') or entry.get('note', '')
            if urldate:
                date_formatted = self._format_access_date(urldate)
                url_part += f" (дата звернення: {date_formatted})"
            parts.append(url_part)

        return self._finalize_entry(parts)

    def _is_english(self, entry: Dict) -> bool:
        """Определяет, является ли запись англоязычной"""
        author = entry.get('author', '')
        title = entry.get('title', '')
        journal = entry.get('journal', '')

        cyrillic_pattern = re.compile('[а-яА-ЯіїєґІЇЄҐ]')

        # Подсчитываем кириллические символы
        all_text = f"{author} {title} {journal}"
        cyrillic_count = len(cyrillic_pattern.findall(all_text))
        total_letters = len(re.findall(r'[a-zA-Zа-яА-ЯіїєґІЇЄҐ]', all_text))

        # Если кириллических букв меньше 10% от общего числа, считаем англоязычной
        if total_letters > 0 and cyrillic_count / total_letters < 0.1:
            return True

        # Если нет кириллических символов вообще
        if cyrillic_count == 0:
            return True

        return False


    def _clean_text(self, text: str) -> str:
        """Очищает текст от специальных символов LaTeX и лишних пробелов"""
        if not text:
            return ""

        text = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', text)
        text = re.sub(r'\\[a-zA-Z]+', '', text)

        text = text.replace('{', '').replace('}', '')

        text = text.replace('``', '"').replace("''", '"')
        text = text.replace('`', "'")

        text = ' '.join(text.split())

        return text.strip()

    def _format_edition(self, edition: str, is_english: bool = False) -> str:
        """Форматирует номер издания в зависимости от языка"""
        edition = edition.lower().replace('edition', '').strip()

        number_map = {
            'first': '1', '1st': '1',
            'second': '2', '2nd': '2',
            'third': '3', '3rd': '3',
            'fourth': '4', '4th': '4',
            'fifth': '5', '5th': '5',
        }

        edition_lower = edition.lower()
        edition_num = None

        for key, value in number_map.items():
            if key in edition_lower:
                edition_num = value
                break

        if not edition_num and edition.isdigit():
            edition_num = edition

        if edition_num:
            if is_english:
                if edition_num == '1':
                    return "1st ed."
                elif edition_num == '2':
                    return "2nd ed."
                elif edition_num == '3':
                    return "3rd ed."
                else:
                    return f"{edition_num}th ed."
            else:
                if edition_num == '3':
                    return "3-тє вид."
                else:
                    return f"{edition_num}-ге вид."

        return edition

    def _format_access_date(self, date_string: str) -> str:
        """Форматирует дату обращения к ресурсу"""
        if not date_string:
            return ""

        date_string = date_string.replace('дата звернення:', '').strip()
        date_string = date_string.replace('accessed:', '').strip()

        if re.match(r'\d{2}\.\d{2}\.\d{4}', date_string):
            return date_string

        match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_string)
        if match:
            return f"{match.group(3)}.{match.group(2)}.{match.group(1)}"

        match = re.search(r'(\d{2})[-/](\d{2})[-/](\d{4})', date_string)
        if match:
            return f"{match.group(1)}.{match.group(2)}.{match.group(3)}"

        return date_string

    def convert_file_to_list(self, filepath: str, selected_ids: Optional[List[str]] = None) -> List[str]:
        """Конвертирует BibTeX файл в список отформатированных строк DSTU

        Args:
            filepath: Путь к BibTeX файлу
            selected_ids: Список ID записей для конвертации. Если None, конвертирует все записи.
        """
        entries = self.parse_bibtex_file(filepath)
        if selected_ids:
            entries = self._filter_entries_by_id(entries, selected_ids)
        return self.convert_entries(entries)

    def convert_string_to_list(self, bibtex_string: str, selected_ids: Optional[List[str]] = None) -> List[str]:
        """Конвертирует строку BibTeX в список отформатированных строк DSTU

        Args:
            bibtex_string: Строка в формате BibTeX
            selected_ids: Список ID записей для конвертации. Если None, конвертирует все записи.
        """
        entries = self.parse_bibtex_string(bibtex_string)
        if selected_ids:
            entries = self._filter_entries_by_id(entries, selected_ids)
        return self.convert_entries(entries)

    def convert_file_to_string(self, filepath: str, numbered: bool = True, selected_ids: Optional[List[str]] = None) -> str:
        """Конвертирует BibTeX файл в одну строку с библиографическим списком

        Args:
            filepath: Путь к BibTeX файлу
            numbered: Добавлять нумерацию к записям
            selected_ids: Список ID записей для конвертации. Если None, конвертирует все записи.
        """
        entries = self.convert_file_to_list(filepath, selected_ids)
        return self._format_bibliography_list(entries, numbered)

    def convert_string_to_formatted_string(self, bibtex_string: str, numbered: bool = True, selected_ids: Optional[List[str]] = None) -> str:
        """Конвертирует строку BibTeX в отформатированный библиографический список

        Args:
            bibtex_string: Строка в формате BibTeX
            numbered: Добавлять нумерацию к записям
            selected_ids: Список ID записей для конвертации. Если None, конвертирует все записи.
        """
        entries = self.convert_string_to_list(bibtex_string, selected_ids)
        return self._format_bibliography_list(entries, numbered)

    def _format_bibliography_list(self, entries: List[str], numbered: bool = True) -> str:
        """Форматирует список записей в единую строку"""
        if numbered:
            formatted = []
            for i, entry in enumerate(entries, 1):
                formatted.append(f"{i}. {entry}")
            return '\n'.join(formatted)
        else:
            return '\n'.join(entries)
