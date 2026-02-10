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

    Поддерживает различные типы записей:
    - Книги (book, inbook)
    - Статьи в журналах (article)
    - Материалы конференций (inproceedings, conference)
    - Диссертации и авторефераты (phdthesis, mastersthesis)
    - Веб-ресурсы (online, misc с url)
    - Стандарты (techreport, standard)
    """

    def __init__(self):
        self.parser = BibTexParser(common_strings=True)
        self.parser.ignore_nonstandard_types = False
        self.parser.expect_multiple_parse = True  # Избегаем warning при множественных вызовах

    def parse_bibtex_file(self, filepath: str) -> List[Dict]:
        """Парсит BibTeX файл и возвращает список записей"""
        with open(filepath, 'r', encoding='utf-8') as bibfile:
            bib_database = bibtexparser.load(bibfile, self.parser)
        return bib_database.entries

    def parse_bibtex_string(self, bibtex_string: str) -> List[Dict]:
        """Парсит строку BibTeX и возвращает список записей"""
        # Создаём новый парсер для каждого вызова, чтобы избежать кэширования
        parser = BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = False
        bib_database = bibtexparser.loads(bibtex_string, parser)
        return bib_database.entries

    def convert_entries(self, entries: List[Dict]) -> List[str]:
        """
        Конвертирует список BibTeX записей в формат DSTU 8302:2015.

        Args:
            entries: Список словарей с ключами BibTeX (author, title, year, и т.д.)

        Returns:
            Список отформатированных строк согласно DSTU 8302:2015
        """
        formatted_entries = []
        for entry in entries:
            formatted = self._convert_entry(entry)
            if formatted:
                formatted_entries.append(formatted)
        return formatted_entries

    def _finalize_entry(self, parts: List[str]) -> str:
        """Финализирует запись, объединяя части и добавляя точку в конце"""
        if not parts:
            return ""

        # Объединяем части с правильной пунктуацией
        result_parts = []
        for i, part in enumerate(parts):
            if i == 0:
                result_parts.append(part)
            else:
                # Если часть начинается с "/" (редактор), не добавляем точку
                if part.startswith('/'):
                    result_parts.append(' ' + part)
                # Если предыдущая часть заканчивается квадратной скобкой, не добавляем точку
                elif result_parts[-1].endswith(']'):
                    result_parts.append(' ' + part)
                # Если предыдущая часть заканчивается точкой, используем пробел вместо ". "
                elif result_parts[-1].endswith('.'):
                    result_parts.append(' ' + part)
                else:
                    result_parts.append('. ' + part)

        result = ''.join(result_parts)
        if not result.endswith('.'):
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
            # Для неизвестных типов используем общий формат
            return self._format_generic(entry)

    def _format_authors(self, authors_string: str, max_authors: int = 3) -> tuple[str, int]:
        """
        Форматирует авторов согласно DSTU 8302:2015.

        Правила:
        - 1-3 автора: все перечисляются
        - 4 автора: можно перечислить всех или первого + "та ін."
        - 5+ авторов: первый автор + "та ін."

        Returns:
            (formatted_string, author_count)
        """
        if not authors_string:
            return "", 0

        # Разделяем авторов (BibTeX использует 'and')
        authors = [a.strip() for a in authors_string.split(' and ')]
        author_count = len(authors)

        formatted_authors = []
        for author in authors[:max_authors]:
            formatted_authors.append(self._format_single_author(author))

        if author_count <= 3:
            return ', '.join(formatted_authors), author_count
        elif author_count == 4:
            # Можно все 4 или первый + "та ін."
            if max_authors >= 4:
                all_formatted = [self._format_single_author(a) for a in authors]
                return ', '.join(all_formatted), author_count
            else:
                return formatted_authors[0] + ' та ін.', author_count
        else:
            # 5+ авторов - только первый + "та ін."
            return formatted_authors[0] + ' та ін.', author_count

    def _format_single_author(self, author: str) -> str:
        """
        Форматирует одного автора: Фамилия И. О.
        """
        # Убираем лишние пробелы
        author = ' '.join(author.split())

        # Если автор в формате "Фамилия, Имя Отчество"
        if ',' in author:
            parts = author.split(',', 1)
            lastname = parts[0].strip()
            firstnames = parts[1].strip() if len(parts) > 1 else ''

            # Инициалы
            initials = []
            for name in firstnames.split():
                name = name.strip()
                if name:
                    # Убираем точки если есть
                    name = name.replace('.', '')
                    if len(name) > 0:
                        initials.append(name[0].upper() + '.')

            if initials:
                return f"{lastname} {' '.join(initials)}"
            return lastname
        else:
            # Формат "Имя Отчество Фамилия" или "Имя Фамилия"
            parts = author.split()
            if len(parts) >= 2:
                # Последняя часть - фамилия
                lastname = parts[-1]
                firstnames = parts[:-1]
                initials = [name[0].upper() + '.' for name in firstnames if name]
                return f"{lastname} {' '.join(initials)}"
            return author

    def _format_single_author_genitive(self, author: str) -> str:
        """
        Форматирует одного автора в родительном падеже для редактора: И. О. Фамилии
        """
        # Убираем лишние пробелы
        author = ' '.join(author.split())

        # Если автор в формате "Фамилия, Имя Отчество"
        if ',' in author:
            parts = author.split(',', 1)
            lastname = parts[0].strip()
            firstnames = parts[1].strip() if len(parts) > 1 else ''

            # Инициалы
            initials = []
            for name in firstnames.split():
                name = name.strip()
                if name:
                    # Убираем точки если есть
                    name = name.replace('.', '')
                    if len(name) > 0:
                        initials.append(name[0].upper() + '.')

            # Родительный падеж фамилии
            lastname_gen = self._to_genitive(lastname)

            if initials:
                return f"{' '.join(initials)} {lastname_gen}"
            return lastname_gen
        else:
            # Формат "Имя Отчество Фамилия" или "Имя Фамилия"
            parts = author.split()
            if len(parts) >= 2:
                # Последняя часть - фамилия
                lastname = parts[-1]
                firstnames = parts[:-1]
                initials = [name[0].upper() + '.' for name in firstnames if name]

                lastname_gen = self._to_genitive(lastname)

                if initials:
                    return f"{' '.join(initials)} {lastname_gen}"
                return lastname_gen
            return author

    def _to_genitive(self, lastname: str) -> str:
        """Простое преобразование фамилии в родительный падеж"""
        # Простые правила для украинских/русских фамилий
        if lastname.endswith('ко') or lastname.endswith('енко'):
            return lastname  # Фамилии на -ко не изменяются
        elif lastname.endswith('ук') or lastname.endswith('юк'):
            return lastname + 'а'
        elif lastname.endswith('ський') or lastname.endswith('цький'):
            return lastname.replace('ий', 'ого')
        elif lastname.endswith('ов') or lastname.endswith('ев') or lastname.endswith('ёв'):
            return lastname + 'а'
        elif lastname.endswith('ін') or lastname.endswith('їн'):
            return lastname + 'а'
        else:
            # По умолчанию добавляем 'а' если фамилия не латинская
            if any(char in lastname.lower() for char in 'абвгдежзийклмнопрстуфхцчшщъыьэюяієїґ'):
                return lastname + 'а'
            return lastname  # Для латинских фамилий не изменяем

    def _format_book(self, entry: Dict) -> str:
        """Форматирует книгу согласно Д.1 DSTU 8302:2015"""
        parts = []

        # Определяем язык
        is_english = self._is_english(entry)

        # Авторы
        authors = entry.get('author', '')
        if authors:
            formatted_authors, author_count = self._format_authors(authors)
            parts.append(formatted_authors)

        # Название книги + подзаголовок
        title = self._clean_text(entry.get('title', ''))
        subtitle = self._clean_text(entry.get('subtitle', ''))

        if title:
            title = title.replace('{', '').replace('}', '')

            # Тип издания (например, "монографія", "підручник")
            book_type = entry.get('type', '')
            if book_type:
                book_type = self._clean_text(book_type)

            # Формируем заголовок с подзаголовком и типом
            if subtitle:
                subtitle = subtitle.replace('{', '').replace('}', '')
                if book_type:
                    # Если есть subtitle и type, структура: "Название : подзаголовок : тип"
                    # НО если type в квадратных скобках, он идет без двоеточия
                    if book_type.startswith('['):
                        title_full = f"{title} : {subtitle} {book_type}"
                    else:
                        title_full = f"{title} : {subtitle} : {book_type}"
                else:
                    title_full = f"{title} : {subtitle}"
            elif book_type:
                title_full = f"{title} : {book_type}"
            else:
                title_full = title

            parts.append(title_full)

        # Редактор (с информацией о типе редакции)
        editor = entry.get('editor', '')
        note = entry.get('note', '')

        if editor and authors:
            # Если есть автор, редактор идет через "/ за ред." в родительном падеже
            # Разделяем редакторов
            editors = [e.strip() for e in editor.split(' and ')]
            formatted_editors_gen = [self._format_single_author_genitive(e) for e in editors]
            formatted_editor = ', '.join(formatted_editors_gen)

            if 'за заг. наук. ред.' in note:
                parts.append(f"/ за заг. наук. ред. {formatted_editor}")
            elif 'за ред.' in note:
                parts.append(f"/ за ред. {formatted_editor}")
            else:
                # По умолчанию
                parts.append(f"/ за ред. {formatted_editor}")
        elif editor and not authors:
            # Если нет автора, может быть в другом формате (для сборников)
            editors = [e.strip() for e in editor.split(' and ')]
            formatted_editors_gen = [self._format_single_author_genitive(e) for e in editors]
            formatted_editor = ', '.join(formatted_editors_gen)
            parts.append(f"/ за ред. {formatted_editor}")

        # Издание и примечание
        edition = entry.get('edition', '')

        # Собираем часть с местом, издательством и годом
        publisher_parts = []

        # Издание с примечанием
        if edition:
            edition_text = self._format_edition(edition, is_english)
            # Проверяем примечание на наличие доп. информации
            if note and ('переробл.' in note or 'допов.' in note):
                # Извлекаем текст примечания без информации о редакторе
                note_text = note
                note_text = note_text.replace('за заг. наук. ред.', '').replace('за ред.', '').strip()
                if note_text:
                    edition_text = f"{edition_text}, {note_text}"
            publisher_parts.append(edition_text)

        # Место издания
        address = entry.get('address', '')
        if address:
            publisher_parts.append(address)

        # Издательство
        publisher = entry.get('publisher', '')
        if publisher:
            if address:
                publisher_parts.append(f": {publisher}")
            else:
                publisher_parts.append(publisher)

        # Год
        year = entry.get('year', '')
        if year:
            publisher_parts.append(f", {year}")

        if publisher_parts:
            pub_text = ' '.join(publisher_parts).replace(' ,', ',').replace('  ', ' ')
            parts.append(pub_text)

        # Страницы
        pages = entry.get('pages', '')
        if not pages and 'pagetotal' in entry:
            pages = entry.get('pagetotal', '')

        if pages:
            # Определяем единицу измерения
            page_unit = "p." if is_english else "с."
            # Если это общее количество страниц
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

    def _format_article(self, entry: Dict) -> str:
        """Форматирует статью в журнале согласно Д.13.3 DSTU 8302:2015"""
        parts = []

        # Определяем язык
        is_english = self._is_english(entry)

        # Авторы
        authors = entry.get('author', '')
        if authors:
            formatted_authors, author_count = self._format_authors(authors, max_authors=4)
            # Для статей с 4+ авторами можно использовать формат "Название / Авторы"
            if author_count >= 4:
                # Используем формат с авторами в начале
                parts.append(formatted_authors)
            else:
                parts.append(formatted_authors)

        # Название статьи
        title = self._clean_text(entry.get('title', ''))
        if title:
            title = title.replace('{', '').replace('}', '')
            parts.append(title)

        # Журнал
        journal = entry.get('journal', '')
        if journal:
            journal = self._clean_text(journal)
            parts.append(journal)

        # Год, том, номер
        year = entry.get('year', '')
        volume = entry.get('volume', '')
        number = entry.get('number', '')

        issue_parts = []
        if year:
            issue_parts.append(year)

        if volume:
            if is_english:
                vol_text = f"Vol. {volume}" if not volume.startswith('Vol') else volume
            else:
                vol_text = f"Т. {volume}" if not volume.startswith('Т') else volume
            issue_parts.append(vol_text)

        if number:
            # Заменяем -- на – в номере
            number = number.replace('--', '–')
            if is_english:
                num_text = f"No {number}" if not number.startswith('No') else number
            else:
                num_text = f"№ {number}" if not number.startswith('№') else number
            issue_parts.append(num_text)

        if issue_parts:
            # ВАЖНО: используем точку после года, затем запятую между томом и номером
            if len(issue_parts) == 1:
                parts.append(issue_parts[0])
            elif len(issue_parts) == 2:
                # Год и том/номер
                parts.append(f"{issue_parts[0]}. {issue_parts[1]}")
            else:
                # Год, том и номер
                parts.append(f"{issue_parts[0]}. {issue_parts[1]}, {issue_parts[2]}")

        # Страницы
        pages = entry.get('pages', '')
        if pages:
            # Заменяем дефис на тире
            pages = pages.replace('--', '–').replace('-', '–')
            page_prefix = "P." if is_english else "С."
            parts.append(f"{page_prefix} {pages}")

        # URL
        url = entry.get('url', '')
        if url:
            url_part = f"URL: {url}"
            urldate = entry.get('urldate', '') or entry.get('note', '')
            if urldate:
                date_formatted = self._format_access_date(urldate)
                url_part += f" (дата звернення: {date_formatted})"
            parts.append(url_part)

        # DOI
        doi = entry.get('doi', '')
        if doi:
            doi_part = f"DOI: https://doi.org/{doi}"
            # Если есть URL с датой обращения, добавляем к DOI
            if url and urldate:
                date_formatted = self._format_access_date(urldate)
                doi_part += f" (дата звернення: {date_formatted})"
            parts.append(doi_part)

        return self._finalize_entry(parts)

    def _format_conference(self, entry: Dict) -> str:
        """Форматирует материалы конференции согласно Д.13.4 DSTU 8302:2015"""
        parts = []

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

            # Проверяем наличие детальной даты в note
            note = entry.get('note', '')
            year = entry.get('year', '')

            # Формат: "Название конференции, дата, место"
            # Если в note есть дата и место, используем её
            if note and ('р.' in note or 'р,' in note):
                # note содержит "21–22 листопада 2024 р., Кременчук"
                conf_text = f"{booktitle}, {note}"
                parts.append(conf_text)
            else:
                # Используем year и address
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

        # Страницы
        pages = entry.get('pages', '')
        if pages:
            pages = pages.replace('--', '–').replace('-', '–')
            parts.append(f"С. {pages}")

        # URL
        url = entry.get('url', '')
        if url:
            url_part = f"URL: {url}"
            urldate = entry.get('urldate', '') or entry.get('note', '')
            if urldate:
                date_formatted = self._format_access_date(urldate)
                url_part += f" (дата звернення: {date_formatted})"
            parts.append(url_part)

        # DOI
        doi = entry.get('doi', '')
        if doi:
            doi_part = f"DOI: https://doi.org/{doi}"
            if url and urldate:
                date_formatted = self._format_access_date(urldate)
                doi_part += f" (дата звернення: {date_formatted})"
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

        # Название
        title = self._clean_text(entry.get('title', ''))
        if title:
            title = title.replace('{', '').replace('}', '')
            parts.append(title)

        # Тип работы
        thesis_type = entry.get('type', '')
        if not thesis_type:
            if entry.get('ENTRYTYPE', '').lower() == 'phdthesis':
                thesis_type = 'дис. ... докт. філософії'
            else:
                thesis_type = 'дис. ... канд. наук'

        parts.append(f": {thesis_type}")

        # Место и университет
        school = entry.get('school', '')
        address = entry.get('address', '')
        year = entry.get('year', '')

        school_parts = []
        if address:
            school_parts.append(address + ':')
        if school:
            school_parts.append(school)
        if year:
            school_parts.append(year)

        if school_parts:
            parts.append(' '.join(school_parts))

        # Страницы
        pages = entry.get('pages', '')
        if not pages and 'pagetotal' in entry:
            pages = entry.get('pagetotal', '')

        if pages:
            if pages.replace('-', '').isdigit():
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
            # Перевіряємо чи потрібна точка після URL
            # Якщо title закінчується на ?.!, точка НЕ потрібна
            need_dot = True
            if title and title.rstrip().endswith(('?', '!', '.')):
                need_dot = False

            # Точка ПІСЛЯ URL, ПЕРЕД скобкой с датой (якщо потрібна)
            if need_dot:
                url_part = f"{url}."
            else:
                url_part = url

            urldate = entry.get('urldate', '') or entry.get('note', '')
            if urldate:
                date_formatted = self._format_access_date(urldate)
                url_part += f" (дата звернення: {date_formatted})"
            parts.append(url_part)

        # Финализируем без добавления лишней точки, т.к. URL уже с точкой
        if not parts:
            return ""

        # Объединяем части
        result_parts = []
        for i, part in enumerate(parts):
            if i == 0:
                result_parts.append(part)
            else:
                # Если предыдущая часть заканчивается точкой/вопросом/восклицанием, не дублируем точку
                if result_parts[-1].endswith(('.', '?', '!')):
                    result_parts.append(' ' + part)
                else:
                    result_parts.append('. ' + part)

        result = ''.join(result_parts)

        # Убираем двойную точку перед URL если она есть
        result = result.replace('.. http', '. http')
        result = result.replace('?. http', '? http')
        result = result.replace('!. http', '! http')

        # Добавляем финальную точку если её нет
        if not result.endswith('.'):
            result += '.'

        return result

    def _format_misc(self, entry: Dict) -> str:
        """Форматирует прочие записи"""
        # Если есть URL, форматируем как online
        if 'url' in entry:
            return self._format_online(entry)
        else:
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

        # Номер отчета
        number = entry.get('number', '')
        if number:
            parts.append(number)

        # Организация
        institution = entry.get('institution', '')
        address = entry.get('address', '')
        year = entry.get('year', '')

        inst_parts = []
        if address:
            inst_parts.append(address)
        if institution:
            inst_parts.append(f": {institution}" if address else institution)
        if year:
            inst_parts.append(f", {year}")

        if inst_parts:
            parts.append(''.join(inst_parts).replace(' ,', ','))

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

    def _format_inbook(self, entry: Dict) -> str:
        """Форматирует часть книги согласно Д.13.1 DSTU 8302:2015"""
        parts = []

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

            # Редактор книги
            editor = entry.get('editor', '')
            if editor:
                formatted_editor, _ = self._format_authors(editor)
                parts.append(f"{booktitle} / за ред. {formatted_editor}")
            else:
                parts.append(booktitle)

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
            parts.append(f"С. {pages}")

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
        """
        Определяет, является ли запись англоязычной.
        Проверяет автора и название на наличие кириллических символов.
        """
        # Проверяем автора
        author = entry.get('author', '')
        title = entry.get('title', '')

        # Если есть кириллица, это не английский
        cyrillic_pattern = re.compile('[а-яА-ЯіїєґІЇЄҐ]')

        if cyrillic_pattern.search(author) or cyrillic_pattern.search(title):
            return False

        # Если только латиница, вероятно английский
        return True

    def _clean_text(self, text: str) -> str:
        """
        Очищает текст от специальных символов LaTeX и лишних пробелов.
        Сохраняет украинские и русские буквы.
        """
        if not text:
            return ""

        # Убираем LaTeX команды
        text = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', text)
        text = re.sub(r'\\[a-zA-Z]+', '', text)

        # Убираем фигурные скобки (но оставляем их содержимое)
        text = text.replace('{', '').replace('}', '')

        # Заменяем LaTeX кавычки на обычные
        text = text.replace('``', '"').replace("''", '"')
        text = text.replace('`', "'")

        # Убираем множественные пробелы
        text = ' '.join(text.split())

        return text.strip()

    def _format_edition(self, edition: str, is_english: bool = False) -> str:
        """Форматирует номер издания в зависимости от языка"""
        edition = edition.lower().replace('edition', '').strip()

        # Преобразуем числительные
        number_map = {
            'first': '1', '1st': '1',
            'second': '2', '2nd': '2',
            'third': '3', '3rd': '3',
            'fourth': '4', '4th': '4',
            'fifth': '5', '5th': '5',
            'sixth': '6', '6th': '6',
            'seventh': '7', '7th': '7',
            'eighth': '8', '8th': '8',
            'ninth': '9', '9th': '9',
            'tenth': '10', '10th': '10',
        }

        edition_lower = edition.lower()
        edition_num = None

        for key, value in number_map.items():
            if key in edition_lower:
                edition_num = value
                break

        # Если уже число
        if not edition_num and edition.isdigit():
            edition_num = edition

        if edition_num:
            if is_english:
                # Для английского: 2nd ed., 3rd ed., 7th ed.
                if edition_num == '1':
                    return "1st ed."
                elif edition_num == '2':
                    return "2nd ed."
                elif edition_num == '3':
                    return "3rd ed."
                else:
                    return f"{edition_num}th ed."
            else:
                # Для украинского/русского: 2-ге вид., 3-тє вид.
                # Для 3 використовуємо "тє" замість "ге"
                if edition_num == '3':
                    return "3-тє вид."
                else:
                    return f"{edition_num}-ге вид."

        return edition

    def _format_access_date(self, date_string: str) -> str:
        """
        Форматирует дату обращения к ресурсу.
        Принимает различные форматы и возвращает DD.MM.YYYY
        """
        if not date_string:
            return ""

        # Убираем "дата звернення:" если есть
        date_string = date_string.replace('дата звернення:', '').strip()
        date_string = date_string.replace('accessed:', '').strip()

        # Если уже в нужном формате
        if re.match(r'\d{2}\.\d{2}\.\d{4}', date_string):
            return date_string

        # Формат YYYY-MM-DD
        match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_string)
        if match:
            return f"{match.group(3)}.{match.group(2)}.{match.group(1)}"

        # Формат DD/MM/YYYY или DD-MM-YYYY
        match = re.search(r'(\d{2})[-/](\d{2})[-/](\d{4})', date_string)
        if match:
            return f"{match.group(1)}.{match.group(2)}.{match.group(3)}"

        # Возвращаем как есть, если не распознали
        return date_string

    def convert_file_to_list(self, filepath: str) -> List[str]:
        """
        Конвертирует BibTeX файл в список отформатированных строк DSTU.

        Args:
            filepath: Путь к .bib файлу

        Returns:
            Список строк в формате DSTU 8302:2015
        """
        entries = self.parse_bibtex_file(filepath)
        return self.convert_entries(entries)

    def convert_string_to_list(self, bibtex_string: str) -> List[str]:
        """
        Конвертирует строку BibTeX в список отформатированных строк DSTU.

        Args:
            bibtex_string: Строка с BibTeX записями

        Returns:
            Список строк в формате DSTU 8302:2015
        """
        entries = self.parse_bibtex_string(bibtex_string)
        return self.convert_entries(entries)

    def convert_file_to_string(self, filepath: str, numbered: bool = True) -> str:
        """
        Конвертирует BibTeX файл в одну строку с библиографическим списком.

        Args:
            filepath: Путь к .bib файлу
            numbered: Нумеровать ли записи

        Returns:
            Отформатированная строка со списком литературы
        """
        entries = self.convert_file_to_list(filepath)
        return self._format_bibliography_list(entries, numbered)

    def convert_string_to_formatted_string(self, bibtex_string: str, numbered: bool = True) -> str:
        """
        Конвертирует строку BibTeX в отформатированный библиографический список.

        Args:
            bibtex_string: Строка с BibTeX записями
            numbered: Нумеровать ли записи

        Returns:
            Отформатированная строка со списком литературы
        """
        entries = self.convert_string_to_list(bibtex_string)
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


# Пример использования
if __name__ == "__main__":
    converter = BibTeXToDSTUConverter()

    # Пример BibTeX записи
    sample_bibtex = """
    @book{example2018,
        author = {Іваненко, О. І. and Петренко, М. П.},
        title = {Основи програмування},
        publisher = {Наукова думка},
        year = {2018},
        address = {Київ},
        pages = {245}
    }
    
    @article{smith2020,
        author = {Smith, J. and Doe, A.},
        title = {Machine Learning Applications},
        journal = {Journal of AI},
        year = {2020},
        volume = {15},
        number = {3},
        pages = {123--145},
        doi = {10.1234/jai.2020.123}
    }
    """

    # Конвертируем
    result = converter.convert_string_to_formatted_string(sample_bibtex)
    print("Список літератури згідно ДСТУ 8302:2015:\n")
    print(result)
