import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D7_Patents(unittest.TestCase):
    """Д.7: Патенти та авторські свідоцтва (3 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d7_punkt_1(self):
        """Д.7.1: Зернозбиральний комбайн"""
        bibtex = """@misc{patent25742,
            title = {Зернозбиральний комбайн: пат. 25742 Україна: МПК6С09К11/00, G01Т1/28, G21НЗ/00},
            note = {№ 200701472; заявл. 12.02.07; опубл. 27.08.07, Бюл. № 13. 4 с.}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Зернозбиральний комбайн: пат. 25742 Україна: МПК6С09К11/00, G01Т1/28, G21НЗ/00. № 200701472; заявл. 12.02.07; опубл. 27.08.07, Бюл. № 13. 4 с."
        self.assertEqual(result, expected)

    def test_d7_punkt_2(self):
        """Д.7.2: Спосіб лікування гіперактивності"""
        bibtex = """@misc{patent76509,
            title = {Спосіб лікування гіперактивності у дітей: пат. 76509 Україна},
            note = {№ 2004042416; заявл. 01.04.2004; опубл. 01.08.2006, Бюл. № 8 (кн. 1). 120 с.}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Спосіб лікування гіперактивності у дітей: пат. 76509 Україна. № 2004042416; заявл. 01.04.2004; опубл. 01.08.2006, Бюл. № 8 (кн. 1). 120 с."
        self.assertEqual(result, expected)

    def test_d7_punkt_3(self):
        """Д.7.3: Комп'ютерна програма «Black Sea Hanter»"""
        bibtex = """@misc{blacksea2024,
            title = {А.с. № 129198 від 21.08.2024. Комп'ютерна програма «Black Sea Hanter»},
            author = {Струк, Н. О. and Дика, А. І. and Задерейко, О. В. and Логінова, Н. І. and Трофименко, О. Г.},
            url = {https://sis.nipo.gov.ua/uk/search/detail/1821799/},
            urldate = {2024-12-12}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "А.с. № 129198 від 21.08.2024. Комп'ютерна програма «Black Sea Hanter» / Н. О. Струк, А. І. Дика, О. В. Задерейко, Н. І Логінова., О. Г. Трофименко https://sis.nipo.gov.ua/uk/search/detail/1821799/ (дата звернення: 12.12.2024)."
        self.assertEqual(result, expected)
