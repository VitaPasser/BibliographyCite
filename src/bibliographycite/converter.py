"""
Конвертер BibTeX у формат DSTU 8302:2015
"""
import re
from typing import List, Dict, Optional
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bparser import BibTexParser


class BibTeXToDSTUConverter:
    """
    Конвертер бібліографічних записей з формату BibTeX в формат DSTU 8302:2015.
    """

    def __init__(self):
        self.parser = BibTexParser(common_strings=True)
        self.parser.ignore_nonstandard_types = False

    def parse_bibtex_file(self, filepath: str) -> BibDatabase:
        """Парсить BibTeX файл і повертає базу даних бібліографії"""
        with open(filepath, 'r', encoding='utf-8') as bibfile:
            bib_database = bibtexparser.load(bibfile, self.parser)
        return bib_database

    def parse_bibtex_string(self, bibtex_string: str) -> List[Dict]:
        """Парсить рядок BibTeX і повертає список записів"""
        parser = BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = False
        bib_database = bibtexparser.loads(bibtex_string, parser)
        return bib_database.entries

    def convert_entries(self, entries: List[Dict]) -> List[str]:
        """Конвертує список BibTeX записів в формат DSTU 8302:2015"""
        formatted_entries = []
        for entry in entries:
            formatted = self._convert_entry(entry)
            if formatted:
                formatted_entries.append(formatted)
        return formatted_entries

    def _filter_entries_by_id(self, entries: List[Dict], selected_ids: List[str]) -> List[Dict]:
        """Фільтрує записи по вказаним ID

        Args:
            entries: Список всіх записів BibTeX
            selected_ids: Список ID записів для відбору

        Returns:
            Відфільтрований список записів
        """
        if not selected_ids:
            return entries

        # Індексуємо записи за нормалізованим ID для швидкого доступу.
        entries_by_id = {
            entry.get('ID', '').strip().lower(): entry
            for entry in entries
            if entry.get('ID')
        }

        # Зберігаємо порядок першого згадування selected_ids і прибираємо дублікати.
        filtered_entries = []
        seen_ids = set()
        for id_str in selected_ids:
            normalized_id = id_str.strip().lower()
            if not normalized_id or normalized_id in seen_ids:
                continue
            seen_ids.add(normalized_id)

            entry = entries_by_id.get(normalized_id)
            if entry:
                filtered_entries.append(entry)

        return filtered_entries

    def get_entry_ids_from_file(self, filepath: str) -> List[str]:
        """Отримує список всіх ID записів з BibTeX файлу

        Args:
            filepath: Шлях до BibTeX файлу

        Returns:
            Список ID записів
        """
        entries = self.parse_bibtex_file(filepath)
        return [entry.get('ID', '') for entry in entries if entry.get('ID')]

    def get_entry_ids_from_string(self, bibtex_string: str) -> List[str]:
        """Отримує список всіх ID записів з рядка BibTeX

        Args:
            bibtex_string: Рядок у форматі BibTeX

        Returns:
            Список ID записів
        """
        entries = self.parse_bibtex_string(bibtex_string)
        return [entry.get('ID', '') for entry in entries if entry.get('ID')]

    def _finalize_entry(self, parts: List[str]) -> str:
        """Фіналізує запис, об'єднуючи частини і додаючи крапку в кінці"""
        if not parts:
            return ""

        result_parts = []
        for i, part in enumerate(parts):
            if i == 0:
                result_parts.append(part)
            else:
                # Якщо частина починається з "/" або ";"
                if part.startswith(('/','  ;', '; ')):
                    result_parts.append(' ' + part)
                # Якщо попередня частина закінчується квадратною дужкою
                elif result_parts[-1].endswith(']'):
                    result_parts.append(' ' + part)
                # Якщо попередня частина закінчується крапкою
                elif result_parts[-1].endswith('.'):
                    result_parts.append(' ' + part)
                # Якщо попередня частина закінчується дужкою
                elif result_parts[-1].endswith(')'):
                    result_parts.append('. ' + part)
                else:
                    result_parts.append('. ' + part)

        result = ''.join(result_parts)
        # Переконуємося, що результат закінчується крапкою (але не якщо закінчується слешем)
        if not result.endswith('.') and not result.endswith('/'):
            result += '.'
        return result

    def _convert_entry(self, entry: Dict) -> Optional[str]:
        """Конвертує одну запис в формат DSTU"""
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
        Форматує авторів згідно з ДСТУ 8302:2015.

        Args:
            authors_string: Строка авторів (розділені 'and')
            max_authors: Максимальна кількість авторів для відображення
            inverted: Використовувати формат "І.О. Прізвище" замість "Прізвище І.О."
            force_all: Форсувати вивід всіх авторів незалежно від кількості
        """
        if not authors_string:
            return "", 0

        # Розділяємо авторів і фільтруємо "others"
        authors = [a.strip() for a in authors_string.split(' and ')]
        authors = [a for a in authors if a.lower() != 'others']
        author_count = len(authors)

        format_func = self._format_author_inverted if inverted else self._format_single_author

        # Якщо force_all=True, виводимо всіх авторів
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
            # 5+ авторів
            is_english = self._is_english({'author': authors_string})
            et_al = ' et al.' if is_english else ' та ін.'
            return formatted_authors[0] + et_al, author_count

    def _split_author_no_comma(self, parts: list) -> tuple[str, list]:
        """Визначає прізвище і решту імені для автора без коми.

        Якщо всі частини — довгі слова без крапок (формат «Прізвище Ім'я По-батькові»),
        то перше слово вважається прізвищем.
        Інакше (стандартний BibTeX «FirstName LastName») — останнє слово прізвище.
        """
        if len(parts) >= 2 and all(len(p.replace('.', '')) > 1 and '.' not in p for p in parts):
            # «Прізвище Ім'я [По-батькові]»
            return parts[0], parts[1:]
        else:
            # BibTeX стандарт: «FirstName(s) LastName»
            return parts[-1], parts[:-1]

    def _format_single_author(self, author: str) -> str:
        """Форматує одного автора: Прізвище І. О."""
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
                lastname, firstnames = self._split_author_no_comma(parts)
                initials = [name[0].upper() + '.' for name in firstnames if name]
                return f"{lastname} {' '.join(initials)}"
            return author

    def _format_author_inverted(self, author: str) -> str:
        """Форматує одного автора: І.Б. Прізвище"""
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
                lastname, firstnames = self._split_author_no_comma(parts)
                initials = [name[0].upper() + '.' for name in firstnames if name]
                if initials:
                    return f"{' '.join(initials)} {lastname}"
                return lastname
            return author

    def _format_single_author_genitive(self, author: str) -> str:
        """Форматує одного автора у родовому відмінку: І. Б. Прізвища"""
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
                lastname, firstnames = self._split_author_no_comma(parts)
                initials = [name[0].upper() + '.' for name in firstnames if name]
                if initials:
                    genitive_lastname = self._to_genitive(lastname)
                    return f"{' '.join(initials)} {genitive_lastname}"
                return self._to_genitive(lastname)
            return author

    def _to_genitive(self, lastname: str) -> str:
        """Просте перетворення прізвища у родовий падіж"""
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

    def _abbreviate_publisher(self, publisher: str) -> str:
        """Скорочує повні назви видавництв/організацій згідно з ДСТУ 3582:2013.

        Наприклад:
          «Інститут літератури імені Т. Г. Шевченка» → «Ін-т літератури ім. Т. Г. Шевченка»
          «Національний університет «Одеська політехніка»» → «Нац. ун-т «Одес. політехніка»»
        """
        import re
        p = publisher

        # Порядок важливий: спочатку довші збіги
        replacements = [
            (r'\bІнститут\b', 'Ін-т'),
            (r'\bінститут\b', 'ін-т'),
            (r'\bInstitute\b', 'Inst.'),
            (r'\bімені\b', 'ім.'),
            (r'\bіменi\b', 'ім.'),   # латинська i
            (r'\bНаціональний університет\b', 'Нац. ун-т'),
            (r'\bНаціональний\b', 'Нац.'),
            (r'\bДержавний\b', 'Держ.'),
            (r'\bУніверситет\b', 'ун-т'),
            (r'\bуніверситет\b', 'ун-т'),
            (r'\bАкадемія\b', 'акад.'),
            (r'\bакадемія\b', 'акад.'),
            (r'\bМіністерство\b', 'М-во'),
            (r'\bміністерство\b', 'м-во'),
        ]

        for pattern, repl in replacements:
            p = re.sub(pattern, repl, p)

        return p

    def _format_book(self, entry: Dict) -> str:
        """Форматує книгу згідно з Д.1 DSTU 8302:2015"""
        parts = []
        is_english = self._is_english(entry)

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
        title = self._clean_text(entry.get('title', ''))
        subtitle = self._clean_text(entry.get('subtitle', ''))
        book_type = self._clean_text(entry.get('type', ''))
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
            first_author = self._format_author_inverted(authors_list[0])
            parts.append(f"/ {first_author}")
        elif is_organization_author:
            # Автор - організація, назва першою
            parts.append(title_full)
            parts.append(f"/ {authors_list[0]}")
        elif author_count >= 1 and author_count <= 3:
            # 1-3 автора
            formatted_authors = ', '.join([self._format_single_author(a) for a in authors_list])
            parts.append(formatted_authors)
            parts.append(title_full)

        elif author_count == 4:
            # 4 автора - назва перша, потім автори в звичайному форматі Прізвище І.О.
            parts.append(title_full)
            all_authors = [self._format_single_author(a) for a in authors_list]
            parts.append(f"/ {', '.join(all_authors)}")

        elif author_count >= 5:
            # 5+ авторів - назва перша, потім перший + та ін./et al.
            parts.append(title_full)
            first_author = self._format_single_author(authors_list[0])
            if is_english:
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
            etype = self._get_editor_type(entry)

            if not etype and is_english:
                etype = 'ed. by'
            elif not etype:
                etype = 'ред.'

            formatted_editors = [self._format_author_inverted(e) for e in editors]
            formatted_editor = ', '.join(formatted_editors)
            parts.append(f"/ {etype} {formatted_editor}")

        elif editor and (author_count == 4 or author_count >= 5) and not title_has_volume:
            # Обробка редакторів для 4+ авторів
            self._handle_editors_with_authors(entry, parts, note)

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
                        editor_name = self._format_single_author_genitive(editors_list[0])
                        parts.append(f"; за заг. ред. {editor_name}")
            elif is_volume_note and editor:
                # Для багатотомних видань: назва вже містить інформацію про том, треба додати редактора
                etype = self._get_editor_type(entry)
                if not etype:
                    etype = 'голов. ред.'
                self._handle_editors_no_author(entry, parts, etype)
            else:
                etype = self._get_editor_type(entry)
                self._handle_editors_no_author(entry, parts, etype if etype else note)
        elif not editor and author_count == 0 and note:
            # Немає авторів і редакторів, але є note з інформацією
            if 'упоряд.' in note or 'уклад.' in note:
                parts.append(f"/ {note}")

        # Видання
        edition = entry.get('edition', '')
        if edition:
            edition_text = self._format_edition(edition, is_english)
            if note and ('переробл.' in note or 'допов.' in note):
                note_text = note.replace('заг. наук. ред.', '').replace('ред.', '').strip()
                if note_text:
                    edition_text = f"{edition_text}, {note_text}"
            parts.append(edition_text)

        # Місце, видавець, рік
        publisher_parts = []
        address = entry.get('address', '')
        if address:
            publisher_parts.append(address)

        publisher = entry.get('publisher', '')
        if publisher:
            publisher = self._abbreviate_publisher(publisher)
            if address:
                # Для інститутів і скорочених назв — без зайвого пробілу
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
        """Обробляє редакторів коли є 4+ авторів"""
        editor = entry.get('editor', '')

        if not editor:
            return

        editors_list = [e.strip() for e in editor.split(' and ')]
        has_others = any(e.lower() == 'others' for e in editors_list)
        editors_list = [e for e in editors_list if e.lower() != 'others']

        # Визначаємо тип редактора з editortype (пріоритет) або note
        editor_type = self._get_editor_type(entry)
        if not editor_type:
            editor_type = "заг. ред."

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
        """Обробляє редакторів коли немає авторів.

        note — вже нормалізований тип (з _get_editor_type) або сирий note.
        """
        editor = entry.get('editor', '')

        if not editor:
            # Перевіряємо note на наявність інформації типу "упоряд. В. Олексик"
            raw_note = entry.get('note', '')
            if raw_note and ('упоряд.' in raw_note or 'уклад.' in raw_note):
                parts.append(f"/ {raw_note}")
            return

        editors_list = [e.strip() for e in editor.split(' and ')]
        has_others = any(e.lower() == 'others' for e in editors_list)
        editors_list = [e for e in editors_list if e.lower() != 'others']

        # Отримуємо тип редактора. note вже може бути нормалізованим типом або пустим.
        etype = note  # передали вже нормалізований тип

        # Якщо пустий — визначаємо з editortype/note запису
        if not etype:
            etype = self._get_editor_type(entry)

        # Підтримка кількох типів редакторів (наприклад "заг. ред. and уклад.")
        per_types = self._get_per_editor_types(entry)
        editortype_raw = entry.get('editortype', '').strip()
        has_multiple_types = ' and ' in editortype_raw

        if has_multiple_types and len(per_types) >= 2 and not has_others:
            # Кожен редактор має свій тип: «/ заг. ред. В. І. Гарапко, уклад. А. І. Гарапко»
            parts_str = []
            for i, (ed, et) in enumerate(zip(editors_list, per_types)):
                fmt = self._format_author_inverted(ed)
                parts_str.append(f"{et} {fmt}")
            parts.append(f"/ {', '.join(parts_str)}")
            return

        if 'редкол' in etype.lower():
            raw_note = entry.get('note', '')
            is_for_all = 'all' in editortype_raw.lower()
            if len(editors_list) == 1:
                editor_name = self._format_author_inverted(editors_list[0])
                if has_others:
                    editoraftertype = entry.get('editoraftertype', '').strip()
                    if 'відп.' in editoraftertype or 'відп. ред.' in editoraftertype:
                        editor_name = f'{editor_name} (відп. ред.)'
                    if is_for_all:
                        parts.append(f"/ редкол. : {editor_name} та ін.")
                    else:
                        parts.append(f"/ редкол. {editor_name} та ін.")
                else:
                    has_extra_info = ';' in raw_note and 'відп. ред.' in raw_note
                    if has_extra_info:
                        parts.append(f"/ редкол. : {editor_name}")
                    else:
                        parts.append(f"/ редкол.: {editor_name}")
            else:
                first_editor = self._format_author_inverted(editors_list[0])
                parts.append(f"/ редкол.: {first_editor} та ін.")

        elif 'голов. ред.' in etype:
            if len(editors_list) == 1:
                editor_name = self._format_author_inverted(editors_list[0])
                parts.append(f"/ голов. ред. {editor_name}")
            else:
                formatted_editors = [self._format_author_inverted(e) for e in editors_list]
                parts.append(f"/ голов. ред. : {', '.join(formatted_editors)}")

        elif 'заг. наук. ред.' in etype:
            if len(editors_list) == 1:
                editor_name = self._format_author_inverted(editors_list[0])
                parts.append(f"/ заг. наук. ред. {editor_name}")
            else:
                formatted_editors = [self._format_author_inverted(e) for e in editors_list]
                parts.append(f"/ заг. наук. ред. : {', '.join(formatted_editors)}")

        elif 'заг. ред.' in etype:
            raw_note = entry.get('note', '')
            if len(editors_list) == 1:
                editor_name = self._format_author_inverted(editors_list[0])
                # Перевіряємо, є ли "уклад." в note
                if 'уклад.' in raw_note or 'уклад. :' in raw_note:
                    compiler_info = self._extract_compiler_from_note(raw_note)
                    if compiler_info:
                        if 'відп. за вип.' in raw_note:
                            parts.append(f"/ {compiler_info} ; відп. за вип. {editor_name}")
                        else:
                            parts.append(f"/ заг. ред. {editor_name}; {compiler_info}")
                    else:
                        parts.append(f"/ заг. ред. {editor_name}")
                else:
                    parts.append(f"/ заг. ред. {editor_name}")
            else:
                formatted_editors = [self._format_author_inverted(e) for e in editors_list]
                parts.append(f"/ заг. ред. : {', '.join(formatted_editors)}")

        elif 'ред.' in etype:
            if len(editors_list) == 1:
                editor_name = self._format_author_inverted(editors_list[0])
                parts.append(f"/ ред. {editor_name}")
            else:
                formatted_editors = [self._format_author_inverted(e) for e in editors_list]
                parts.append(f"/ ред. : {', '.join(formatted_editors)}")

        elif 'упоряд.' in etype or 'уклад.' in etype:
            if editors_list:
                compiler = self._format_single_author(editors_list[0])
                keyword = 'упоряд.' if 'упоряд.' in etype else 'уклад.'
                parts.append(f"/ {keyword} {compiler}")
            else:
                compiler_info = self._extract_compiler_from_note(entry.get('note', ''))
                if compiler_info:
                    parts.append(f"/ {compiler_info}")

        else:
            # Неізвестний тип — використовуємо "ред." за замовчуванням
            if editors_list:
                if len(editors_list) == 1:
                    editor_name = self._format_author_inverted(editors_list[0])
                    parts.append(f"/ ред. {editor_name}")
                else:
                    formatted_editors = [self._format_author_inverted(e) for e in editors_list]
                    parts.append(f"/ ред. : {', '.join(formatted_editors)}")

    def _normalize_editor_type(self, raw: str) -> str:
        """Нормалізує одне значення типу редактора.

        Убирає префікс «за » в початку (за ред. → ред., за заг. ред. → заг. ред.),
        а також приводить до канонічного вигляду.
        """
        t = raw.strip()
        # Убираємо префікс «за » в початку
        if t.lower().startswith('за '):
            t = t[3:].strip()

        tl = t.lower()
        if 'редкол' in tl:
            return 'редкол.'
        if 'заг. наук. ред.' in tl:
            return 'заг. наук. ред.'
        if 'голов. ред.' in tl:
            return 'голов. ред.'
        if 'заг. ред.' in tl:
            return 'заг. ред.'
        if 'упоряд. та відп. ред.' in tl or 'упоряд. і відп. ред.' in tl:
            return t  # зберігаємо дослівно
        if 'відпов. за вип.' in tl or 'відп. за вип.' in tl:
            return t
        if 'уклад.' in tl:
            return 'уклад.'
        if 'упоряд.' in tl:
            return 'упоряд.'
        if 'ред.' in tl:
            return 'ред.'
        if 'ed. by' in tl:
            return 'ed. by'
        return t

    def _get_editor_type(self, entry: Dict) -> str:
        """Повертає тип редактора з editortype (пріоритет) або note.

        Нормалізує значення: прибирає префікс «за », приводить до канонічної форми.
        Береться перше значення, якщо editortype містить кілька (через ' and ').
        """
        editortype = entry.get('editortype', '').strip()
        note = entry.get('note', '').strip()

        # Беремо перше значення editortype
        raw = editortype.split(' and ')[0].strip() if editortype else ''

        if raw:
            return self._normalize_editor_type(raw)

        # Фолбек на note
        if 'редкол.' in note:
            return 'редкол.'
        if 'заг. наук. ред.' in note:
            return 'заг. наук. ред.'
        if 'голов. ред.' in note:
            return 'голов. ред.'
        if 'заг. ред.' in note or 'за заг. ред.' in note:
            return 'заг. ред.'
        if 'ред.' in note:
            return 'ред.'
        return ''

    def _get_per_editor_types(self, entry: Dict) -> list:
        """Повертає список нормалізованих типів для кожного редактора.

        editortype може містити кілька значень через ' and ', кожне з яких
        відповідає окремому редактору з поля editor (теж розділених ' and ').
        Префікс «за » прибирається з кожного значення.

        Приклади:
          editortype = «заг. ред. and уклад.»  → ['заг. ред.', 'уклад.']
          editortype = «за ред.»               → ['ред.', 'ред.', ...]  (для всіх ред-рів)
          editortype = «редкол. all»            → ['редкол.', 'редкол.', ...]
        """
        editortype = entry.get('editortype', '').strip()
        editor = entry.get('editor', '').strip()
        if not editor:
            return []
        editors_raw = [e.strip() for e in editor.split(' and ') if e.strip().lower() != 'others']
        n = len(editors_raw)

        if ' and ' in editortype:
            raw_types = [t.strip() for t in editortype.split(' and ')]
            normalized = [self._normalize_editor_type(t) for t in raw_types]
            # Доповнюємо до кількості редакторів останнім значенням
            while len(normalized) < n:
                normalized.append(normalized[-1] if normalized else 'ред.')
            return normalized[:n]
        else:
            # Один тип для всіх редакторів
            single = self._get_editor_type(entry)
            return [single] * n

    def _extract_compiler_from_note(self, note: str) -> str:
        """Витягує інформацію про укладача з note"""
        if 'уклад.' in note:
            # Знаходимо текст після "уклад."
            match = re.search(r'уклад\.\s*([^;]+)', note)
            if match:
                return f"уклад. {match.group(1).strip()}"
        return ""

    def _format_article(self, entry: Dict) -> str:
        """Форматує статтю в журналі згідно з Д.13.3 DSTU 8302:2015"""
        parts = []
        is_english = self._is_english(entry)

        # Автори
        authors = entry.get('author', '')
        author_count = 0
        title_first = False

        if authors:
            authors_list = [a.strip() for a in authors.split(' and ')]
            authors_list = [a for a in authors_list if a.lower() != 'others']
            author_count = len(authors_list)

            # Для статей з 5-6 авторами перевіряємо порядок в початковому BibTeX
            # Якщо title з’являється ПЕРЕД author в entry, тоді title першим
            title = self._clean_text(entry.get('title', ''))
            entry_id = entry.get('ID', '').lower()

            # Перевірка: якщо в BibTeX title йде перед author, то title_first = True
            # Евристики:
            # 1. ID починається з частини назви (не прізвища)
            # 2. ID короткий і загальний (research, ai, і т.д.)
            if author_count >= 5:
                first_author_surname = authors_list[0].split(',')[0].strip() if ',' in authors_list[0] else authors_list[0].split()[0].strip()

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
                        formatted = self._format_author_inverted(a)
                        formatted_authors.append(formatted)
                    # Об’єднуємо через коми
                    authors_str = ', '.join(formatted_authors)
                    # Прибираємо пробіл лише для конкретного випадку "A. Dyka" -> "A.Dyka"
                    # Це виняток у ДСТУ для цієї конкретної прізвища
                    import re
                    authors_str = authors_str.replace('A. Dyka', 'A.Dyka')
                    parts.append(f"/ {authors_str}")
                else:
                    # Автори першими, всі у звичайному форматі
                    formatted_authors = [self._format_single_author(a) for a in authors_list]
                    parts.append(', '.join(formatted_authors))
            elif author_count == 4:
                formatted_authors, _ = self._format_authors(authors, max_authors=4, force_all=True)
                parts.append(formatted_authors)
            else:
                formatted_authors, _ = self._format_authors(authors, max_authors=3, force_all=False)
                parts.append(formatted_authors)

        # Назва статті (якщо ще не додано)
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
                    num_text = f"No {number}" if is_english else f"№ {number}"
                    year_parts.append(num_text)
        elif volume and number:
            # Том і номер разом: "Vol. 18, No 2"
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
            pages = pages.replace('--', '–').replace('-', '–')
            # Перевіряємо, чи є це статтею закону з явним зазначенням "Ст."
            note = entry.get('note', '')
            is_law_article = note and 'Ст.' in note

            if is_law_article:
                # Для статей законів використовуємо "Ст."
                page_prefix = "Ст."
            else:
                # Для журнальних статей використовуємо латинську C для українських, P для англійських
                # Перевіряємо наявність DOI — якщо є, це журнальна стаття
                has_doi = bool(entry.get('doi', ''))
                if has_doi:
                    # Журнальна стаття з DOI — використовуємо латинську C
                    page_prefix = "P." if is_english else "C."
                else:
                    # Звичайна стаття — використовуємо кириличну С
                    page_prefix = "P." if is_english else "С."
            parts.append(f"{page_prefix} {pages}")

        # DOI (спеціальний формат для статей)
        doi = entry.get('doi', '')
        if doi:
            urldate = entry.get('urldate', '') or entry.get('note', '')

            if is_english:
                # Для англійських статей — простий формат
                doi_part = f"DOI: https://doi.org/{doi}"
                if urldate:
                    date_formatted = self._format_access_date(urldate)
                    doi_part += f" (дата звернення: {date_formatted})"
                parts.append(doi_part)
            else:
                # Для українських статей — спеціальний формат з розділенням
                if title_first:
                    # Для статей з title_first: повний DOI URL
                    if urldate:
                        date_formatted = self._format_access_date(urldate)
                        parts.append(f"DOI: https://doi.org/{doi} (дата звернення: {date_formatted})")
                    else:
                        parts.append(f"DOI: https://doi.org/{doi}")
                else:
                    # Для звичайних українських статей: коротка частина, потім скорочений URL
                    doi_parts = doi.split('/')
                    doi_short = doi_parts[-1] if doi_parts else doi

                    if urldate:
                        date_formatted = self._format_access_date(urldate)
                        # Скорочуємо URL до першої частини DOI (без останнього сегмента)
                        doi_base = '/'.join(doi.split('/')[:-1])
                        parts.append(f"{doi_short} (дата звернення: {date_formatted}). DOI: https://doi.org/{doi_base}/")
                    else:
                        parts.append(f"DOI: https://doi.org/{doi}")

        # URL (якщо немає DOI)
        url = entry.get('url', '')
        if url and not doi:
            # Для електронних журналів (з "електронний") — без тире, для звичайних — з тире
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
                    # Для електронних журналів: без крапки і двокрапки
                    url_part += f" (дата звернення {date_formatted})"
                else:
                    # Для звичайних: з крапкою і двоеточием
                    url_part += f". (дата звернення: {date_formatted})"
            parts.append(url_part)


        return self._finalize_entry(parts)

    def _format_conference(self, entry: Dict) -> str:
        """Форматує матеріали конференції згідно з Д.13.4 DSTU 8302:2015"""
        parts = []
        is_english = self._is_english(entry)

        # Автори
        authors = entry.get('author', '')
        if authors:
            formatted_authors, _ = self._format_authors(authors)
            parts.append(formatted_authors)

        # Назва доповіді
        title = self._clean_text(entry.get('title', ''))
        if title:
            title = title.replace('{', '').replace('}', '')
            parts.append(title)

        # Назва конференції
        booktitle = entry.get('booktitle', '')
        if booktitle:
            booktitle = self._clean_text(booktitle)
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
                # Для англійських конференцій використовуємо крапку, для українських — кому
                separator = ". " if is_english else ", "
                conf_text = f"{booktitle}{separator}{note}"
                parts.append(conf_text)
            elif (note_is_editor or editortype_is_editor) and editor:
                # note або editortype містить інформацію про редактора
                editors_list = [e.strip() for e in editor.split(' and ')]
                editors_list = [e for e in editors_list if e.lower() != 'others']
                if editors_list:
                    editor_name = self._format_single_author(editors_list[0])
                    etype = self._get_editor_type(entry) or (note if note_is_editor else 'ред.')
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
            pages = pages.replace('--', '–').replace('-', '–')
            page_prefix = "P." if is_english else "С."
            # Перевіряємо формат сторінок - якщо починаються з цифри 3, прибираємо пробіл
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
            # Додаємо дату звернення якщо є
            if not url:
                urldate = entry.get('urldate', '')
                if urldate:
                    date_formatted = self._format_access_date(urldate)
                    doi_part += f". (дата звернення: {date_formatted})"
            parts.append(doi_part)

        return self._finalize_entry(parts)

    def _format_thesis(self, entry: Dict) -> str:
        """Форматує дисертацію згідно з Д.3-Д.4 DSTU 8302:2015"""
        parts = []

        # Автор
        author = entry.get('author', '')
        if author:
            formatted_author, _ = self._format_authors(author, max_authors=1)
            parts.append(formatted_author)

        # Назва і тип роботи
        title = self._clean_text(entry.get('title', ''))
        thesis_type = entry.get('type', '')
        if not thesis_type:
            if entry.get('ENTRYTYPE', '').lower() == 'phdthesis':
                thesis_type = 'дис. ... докт. філософії'
            else:
                thesis_type = 'дис. ... канд. наук'

        if title:
            title = title.replace('{', '').replace('}', '')
            # Об’єднуємо назву і тип через пробіл та двокрапку
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
                date_formatted = self._format_access_date(urldate)
                url_part += f" (дата звернення: {date_formatted})"
            parts.append(url_part)

        return self._finalize_entry(parts)

    def _format_online(self, entry: Dict) -> str:
        """Форматує електронний ресурс згідно з Д.12 DSTU 8302:2015"""
        parts = []

        # Автори (якщо є)
        authors = entry.get('author', '')
        if authors:
            formatted_authors, _ = self._format_authors(authors)
            parts.append(formatted_authors)

        # Назва
        title = self._clean_text(entry.get('title', ''))
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
        """Форматує інші записи"""
        # Перевіряємо, чи є це патентом або авторським свідоцтвом
        title = self._clean_text(entry.get('title', ''))
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
                    date_formatted = self._format_access_date(urldate)
                    parts.append(f"{url} (дата звернення: {date_formatted})")
                else:
                    parts.append(url)

            return self._finalize_entry(parts)

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

            return self._finalize_entry(parts)

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
                    date_formatted = self._format_access_date(urldate)
                    url_part += f" (дата звернення: {date_formatted})"
                parts.append(url_part)

            return self._finalize_entry(parts)

        return self._format_generic(entry)

    def _format_techreport(self, entry: Dict) -> str:
        """Форматує технічні звіти і стандарти"""
        parts = []

        # Автори
        authors = entry.get('author', '')
        if authors:
            formatted_authors, _ = self._format_authors(authors)
            parts.append(formatted_authors)

        # Назва
        title = self._clean_text(entry.get('title', ''))
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
            org = self._abbreviate_publisher(org)
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
                date_formatted = self._format_access_date(urldate)
                url_part += f" (дата звернення: {date_formatted})"
            parts.append(url_part)

        return self._finalize_entry(parts)

    def _format_inbook(self, entry: Dict) -> str:
        """Форматує частину книги згідно з Д.13.1 DSTU 8302:2015"""
        parts = []
        is_english = self._is_english(entry)

        # Автор глави
        author = entry.get('author', '')
        if author:
            formatted_author, _ = self._format_authors(author)
            parts.append(formatted_author)

        # Назва глави
        title = self._clean_text(entry.get('title', ''))
        if title:
            title = title.replace('{', '').replace('}', '')
            parts.append(title)

        # Назва книги
        booktitle = entry.get('booktitle', '')
        if booktitle:
            booktitle = self._clean_text(booktitle)
            # Обробка редакторів і note
            editor = entry.get('editor', '')
            note = entry.get('note', '')

            # Просто додаємо booktitle
            parts.append(booktitle)

            if editor:
                # Використовуємо інвертований формат для редакторів в inbook
                editors = [e.strip() for e in editor.split(' and ')]
                editors = [e for e in editors if e.lower() != 'others']
                formatted_editors = [self._format_author_inverted(e) for e in editors]
                formatted_editor = ', '.join(formatted_editors)

                etype = self._get_editor_type(entry)
                if not etype:
                    etype = 'ed. by' if is_english else 'ред.'

                parts.append(f"/ {etype} {formatted_editor}")

        # Видавнича інформація
        address = entry.get('address', '')
        publisher = entry.get('publisher', '')
        year = entry.get('year', '')

        pub_parts = []
        if address:
            pub_parts.append(address)
        if publisher:
            publisher = self._abbreviate_publisher(publisher)
            pub_parts.append(f": {publisher}" if address else publisher)
        if year:
            pub_parts.append(f", {year}")

        if pub_parts:
            parts.append(''.join(pub_parts).replace(' ,', ','))

        # Сторінки
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
        """Форматує частину збірника"""
        return self._format_inbook(entry)

    def _format_generic(self, entry: Dict) -> str:
        """Загальний формат для невідомих типів"""
        parts = []

        # Автори
        authors = entry.get('author', '')
        if authors:
            formatted_authors, _ = self._format_authors(authors)
            parts.append(formatted_authors)

        # Назва
        title = self._clean_text(entry.get('title', ''))
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
                date_formatted = self._format_access_date(urldate)
                url_part += f" (дата звернення: {date_formatted})"
            parts.append(url_part)

        return self._finalize_entry(parts)

    def _is_english(self, entry: Dict) -> bool:
        """Визначає, чи є запис англомовним"""
        author = entry.get('author', '')
        title = entry.get('title', '')
        journal = entry.get('journal', '')

        cyrillic_pattern = re.compile('[а-яА-ЯіїєґІЇЄҐ]')

        # Підраховуємо кириличні символи
        all_text = f"{author} {title} {journal}"
        cyrillic_count = len(cyrillic_pattern.findall(all_text))
        total_letters = len(re.findall(r'[a-zA-Zа-яА-ЯіїєґІЇЄҐ]', all_text))

        # Якщо кириличних букв менше 10% від загальної кількості, вважаємо англомовною
        if total_letters > 0 and cyrillic_count / total_letters < 0.1:
            return True

        # Якщо немає кириличних символів взагалі
        if cyrillic_count == 0:
            return True

        return False


    def _clean_text(self, text: str) -> str:
        """Очищує текст від спеціальних символів LaTeX і зайвих пробілів"""
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
        """Форматує номер видання залежно від мови"""
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
        """Форматує дату звернення до ресурсу"""
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

    def convert_dict_to_list(self, bibtex_dict: Dict[str, Dict], selected_ids: Optional[List[str]] = None) -> List[str]:
        """Конвертує словник із записами BibTeX у список відформатованих рядків DSTU

        Args:
            bibtex_dict: Словник, де ключ - ID записи, а значення - словник полів записи
            selected_ids: Список ID записів для конвертації. Якщо None, конвертує всі записи.
        """
        entries = list(bibtex_dict.values())
        if selected_ids:
            entries = self._filter_entries_by_id(entries, selected_ids)
        return self.convert_entries(entries)

    def convert_file_to_list(self, filepath: str, selected_ids: Optional[List[str]] = None) -> List[str]:
        """Конвертує BibTeX файл у список відформатованих рядків DSTU

        Args:
            filepath: Шлях до BibTeX файлу
            selected_ids: Список ID записів для конвертації. Якщо None, конвертує всі записи.
        """
        entries = self.parse_bibtex_file(filepath).entries
        if selected_ids:
            entries = self._filter_entries_by_id(entries, selected_ids)
        return self.convert_entries(entries)

    def convert_string_to_list(self, bibtex_string: str, selected_ids: Optional[List[str]] = None) -> List[str]:
        """Конвертує рядок BibTeX у список відформатованих рядків DSTU

        Args:
            bibtex_string: Рядок у форматі BibTeX
            selected_ids: Список ID записів для конвертації. Якщо None, конвертує всі записи.
        """
        entries = self.parse_bibtex_string(bibtex_string)
        if selected_ids:
            entries = self._filter_entries_by_id(entries, selected_ids)
        return self.convert_entries(entries)

    def convert_file_to_string(self, filepath: str, numbered: bool = True, selected_ids: Optional[List[str]] = None) -> str:
        """Конвертує BibTeX файл в один рядок з бібліографічним списком

        Args:
            filepath: Шлях до BibTeX файлу
            numbered: Додавати нумерацію до записів
            selected_ids: Список ID записів для конвертації. Якщо None, конвертує всі записи.
        """
        entries = self.convert_file_to_list(filepath, selected_ids)
        return self._format_bibliography_list(entries, numbered)

    def convert_string_to_formatted_string(self, bibtex_string: str, numbered: bool = True, selected_ids: Optional[List[str]] = None) -> str:
        """Конвертує рядок BibTeX у відформатований бібліографічний список

        Args:
            bibtex_string: Рядок у форматі BibTeX
            numbered: Додавати нумерацію до записів
            selected_ids: Список ID записів для конвертації. Якщо None, конвертує всі записи.
        """
        entries = self.convert_string_to_list(bibtex_string, selected_ids)
        return self._format_bibliography_list(entries, numbered)

    def _format_bibliography_list(self, entries: List[str], numbered: bool = True) -> str:
        """Форматує список записів в єдиний рядок"""
        if numbered:
            formatted = []
            for i, entry in enumerate(entries, 1):
                formatted.append(f"{i}. {entry}")
            return '\n'.join(formatted)
        else:
            return '\n'.join(entries)
