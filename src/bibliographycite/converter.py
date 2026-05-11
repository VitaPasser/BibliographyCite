"""
Конвертер BibTeX у формат DSTU 8302:2015
"""
from typing import List, Dict, Optional

import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bparser import BibTexParser

from .formaters.text.article import format_article
from .formaters.text.book import format_book
from .formaters.text.conference import format_conference
from .formaters.text.inbook import format_inbook
from .formaters.text.misc import format_misc
from .formaters.text.online import format_online
from .formaters.text.techreport import format_techreport
from .formaters.text.thesis import format_thesis
from .utils.finalize_entry import finalize_entry


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
        return finalize_entry(parts)

    def _convert_entry(self, entry: Dict) -> Optional[str]:
        """Конвертує одну запис в формат DSTU"""
        entry_type = entry.get('ENTRYTYPE', '').lower()

        converters = {
            'book': format_book,
            'inbook': format_inbook,
            'article': format_article,
            'inproceedings': format_conference,
            'conference': format_conference,
            'phdthesis': format_thesis,
            'mastersthesis': format_thesis,
            'online': format_online,
            'misc': format_misc,
            'techreport': format_techreport,
            'incollection': format_inbook,
        }

        converter = converters.get(entry_type)
        if converter:
            return converter(entry)
        else:
            return format_inbook(entry)

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
