import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D1_4_FourAuthors(unittest.TestCase):
    """Д.1.4: Чотири автори (2 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_4_punkt_1(self):
        """Д.1.4.1: Інновації"""
        bibtex = """@book{innovatsii2016,
            title = {Інновації},
            type = {навч. посіб.},
            author = {Гуревич, Д. Т. and Чекан, О. С. and Грибан, О. М. and Макарова, В. В.},
            publisher = {ЗНУ},
            year = {2016},
            address = {Запоріжжя},
            pages = {389}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Інновації : навч. посіб. / Гуревич Д. Т., Чекан О. С., Грибан О. М., Макарова В. В. Запоріжжя : ЗНУ, 2016. 389 с."
        self.assertEqual(result, expected)

    def test_d1_4_punkt_2(self):
        """Д.1.4.2: Моделювання програмного забезпечення"""
        bibtex = """@book{modelyuvannya2023,
            title = {Моделювання програмного забезпечення},
            type = {навч.-метод. посібник},
            author = {Манаков, С. Ю. and Трофименко, О. Г. and Лобода, Ю. Г. and Дика, А. І.},
            publisher = {Фенікс},
            year = {2023},
            address = {Одеса},
            pages = {145},
            url = {http://dspace.onua.edu.ua/handle/11300/25952},
            urldate = {2024-12-12}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Моделювання програмного забезпечення : навч.-метод. посібник / С. Ю. Манаков, О. Г. Трофименко, Ю. Г. Лобода, А. І. Дика. Одеса : Фенікс, 2023. 145 с. URL: http://dspace.onua.edu.ua/handle/11300/25952 (дата звернення: 12.12.2024)."
        self.assertEqual(result, expected)
