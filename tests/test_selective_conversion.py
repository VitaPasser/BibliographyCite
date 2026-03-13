"""
Тесты для функциональности выборочной конвертации по ID
"""
import pytest
from bibliographycite import BibTeXToDSTUConverter


class TestSelectiveConversion:
    """Тестирование выборочной конвертации записей по ID"""

    def setup_method(self):
        """Подготовка к каждому тесту"""
        self.converter = BibTeXToDSTUConverter()
        self.sample_bibtex = """
        @book{book1,
            author = {Иванов, И. И.},
            title = {Первая книга},
            year = {2020},
            publisher = {Наука}
        }
        
        @book{book2,
            author = {Петров, П. П.},
            title = {Вторая книга},
            year = {2021},
            publisher = {Техника}
        }
        
        @article{article1,
            author = {Сидоров, С. С.},
            title = {Статья первая},
            journal = {Журнал науки},
            year = {2022},
            pages = {10--20}
        }
        """

    def test_get_entry_ids_from_string(self):
        """Тест получения списка ID из строки"""
        ids = self.converter.get_entry_ids_from_string(self.sample_bibtex)
        expected_ids = ['book1', 'book2', 'article1']
        assert ids == expected_ids

    def test_convert_string_with_selected_ids_single(self):
        """Тест конвертации одной записи по ID"""
        selected_ids = ['book1']
        result = self.converter.convert_string_to_list(self.sample_bibtex, selected_ids=selected_ids)

        assert len(result) == 1
        assert 'Иванов И. И.' in result[0]
        assert 'Первая книга' in result[0]
        assert 'Наука' in result[0]

    def test_convert_string_with_selected_ids_multiple(self):
        """Тест конвертации нескольких записей по ID"""
        selected_ids = ['book1', 'article1']
        result = self.converter.convert_string_to_list(self.sample_bibtex, selected_ids=selected_ids)

        assert len(result) == 2
        # Проверяем, что получили нужные записи
        book_found = any('Первая книга' in entry for entry in result)
        article_found = any('Статья первая' in entry for entry in result)
        assert book_found
        assert article_found

    def test_convert_string_with_nonexistent_ids(self):
        """Тест с несуществующими ID"""
        selected_ids = ['nonexistent1', 'nonexistent2']
        result = self.converter.convert_string_to_list(self.sample_bibtex, selected_ids=selected_ids)

        assert len(result) == 0

    def test_convert_string_with_mixed_ids(self):
        """Тест с смешанными ID (существующие и несуществующие)"""
        selected_ids = ['book1', 'nonexistent', 'article1']
        result = self.converter.convert_string_to_list(self.sample_bibtex, selected_ids=selected_ids)

        assert len(result) == 2
        book_found = any('Первая книга' in entry for entry in result)
        article_found = any('Статья первая' in entry for entry in result)
        assert book_found
        assert article_found

    def test_convert_string_with_case_insensitive_ids(self):
        """Тест с ID разного регистра"""
        selected_ids = ['BOOK1', 'Article1']  # разные регистры
        result = self.converter.convert_string_to_list(self.sample_bibtex, selected_ids=selected_ids)

        assert len(result) == 2

    def test_convert_string_to_formatted_string_with_ids(self):
        """Тест получения отформатированной строки с выбранными ID"""
        selected_ids = ['book1', 'book2']
        result = self.converter.convert_string_to_formatted_string(
            self.sample_bibtex,
            numbered=True,
            selected_ids=selected_ids
        )

        lines = result.split('\n')
        assert len([line for line in lines if line.strip()]) == 2  # 2 записи
        assert '1.' in result
        assert '2.' in result

    def test_convert_string_with_empty_selected_ids(self):
        """Тест с пустым списком ID"""
        selected_ids = []
        result = self.converter.convert_string_to_list(self.sample_bibtex, selected_ids=selected_ids)

        assert len(result) == 3  # Должны вернуться все записи

    def test_convert_string_with_none_selected_ids(self):
        """Тест с None в качестве selected_ids"""
        result = self.converter.convert_string_to_list(self.sample_bibtex, selected_ids=None)

        assert len(result) == 3  # Должны вернуться все записи

    def test_get_ids_from_empty_string(self):
        """Тест получения ID из пустой строки"""
        ids = self.converter.get_entry_ids_from_string("")
        assert ids == []

    def test_filter_entries_by_id_with_whitespace(self):
        """Тест фильтрации с пробелами в ID"""
        selected_ids = [' book1 ', '  article1  ']  # ID с пробелами
        result = self.converter.convert_string_to_list(self.sample_bibtex, selected_ids=selected_ids)

        assert len(result) == 2

    def test_convert_string_with_selected_ids_preserves_selected_order(self):
        """Порядок результата должен следовать порядку первого упоминания в selected_ids"""
        selected_ids = ['article1', 'book2', 'book1']
        result = self.converter.convert_string_to_list(self.sample_bibtex, selected_ids=selected_ids)

        assert len(result) == 3
        assert 'Статья первая' in result[0]
        assert 'Вторая книга' in result[1]
        assert 'Первая книга' in result[2]

    def test_convert_string_with_selected_ids_uses_first_mention_for_duplicates(self):
        """Дубликаты selected_ids не должны менять порядок и не дублируют запись"""
        selected_ids = ['book2', 'book1', 'book2', 'book1']
        result = self.converter.convert_string_to_list(self.sample_bibtex, selected_ids=selected_ids)

        assert len(result) == 2
        assert 'Вторая книга' in result[0]
        assert 'Первая книга' in result[1]
