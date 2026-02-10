import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D6_ArchivalDocuments(unittest.TestCase):
    """Д.6: Архівні документи (1 пункт)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d6_punkt_1(self):
        """Д.6.1: Лист Голови Спілки «Первоцвіт»"""
        bibtex = """@misc{pervotsvit1989,
            title = {Лист Голови Спілки «Первоцвіт» Г. Ф. Петренка на ім'я Голови Ради Міністрів УРСР В. А. Поповича щодо реєстрації Статуту Спілки та сторінки Статуту. 14 грудня 1989 р.},
            note = {ЦДАГО України (Центр. держ. архів громад. Об'єднань України). Ф. 1. Оп. 32. Спр. 2612. Арк. 63, 64 зв., 71}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Лист Голови Спілки «Первоцвіт» Г. Ф. Петренка на ім'я Голови Ради Міністрів УРСР В. А. Поповича щодо реєстрації Статуту Спілки та сторінки Статуту. 14 грудня 1989 р. ЦДАГО України (Центр. держ. архів громад. Об'єднань України). Ф. 1. Оп. 32. Спр. 2612. Арк. 63, 64 зв., 71."
        self.assertEqual(result, expected)
