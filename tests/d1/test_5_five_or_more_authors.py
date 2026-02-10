import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D1_5_FiveOrMoreAuthors(unittest.TestCase):
    """Д.1.5: П'ять і більше авторів (5 пунктів)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_5_punkt_1(self):
        """Д.1.5.1: Операційний менеджмент"""
        bibtex = """@book{operational2011,
            title = {Операційний менеджмент},
            type = {підручник},
            author = {Поплавська, С. М. and others},
            publisher = {ЦУЛ},
            year = {2011},
            address = {Київ},
            pages = {267}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Операційний менеджмент : підручник / С. М. Поплавська та ін. Київ : ЦУЛ, 2011. 267 с."
        self.assertEqual(result, expected)

    def test_d1_5_punkt_2(self):
        """Д.1.5.2: Охорона праці"""
        bibtex = """@book{ohorona2017,
            title = {Охорона праці},
            type = {навч. посіб.},
            author = {Подольська, О. І. and others},
            edition = {2},
            publisher = {ЦУЛ},
            year = {2017},
            address = {Київ},
            pages = {264}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Охорона праці : навч. посіб. / О. І. Подольська та ін. 2-ге вид. Київ : ЦУЛ, 2017. 264 с."
        self.assertEqual(result, expected)

    def test_d1_5_punkt_3(self):
        """Д.1.5.3: Вища математика"""
        bibtex = """@book{vyshcha2015,
            title = {Вища математика},
            type = {конспект лекцій},
            author = {Ткачук, Т. С. and others},
            year = {2015},
            address = {Київ},
            pages = {82}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Вища математика : конспект лекцій / Ткачук Т.С. та ін. Київ, 2015. 82 с."
        self.assertEqual(result, expected)

    def test_d1_5_punkt_4(self):
        """Д.1.5.4: Науково-практичний коментар"""
        bibtex = """@book{komentar2017,
            title = {Науково-практичний коментар Цивільного кодексу України},
            note = {станом на 10 жовт. 2017 р.},
            author = {Мягченко, К. І. and others},
            editor = {Ливанов, І. М.},
            publisher = {ЦУЛ},
            year = {2017},
            address = {Київ},
            pages = {428}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Науково-практичний коментар Цивільного кодексу України : станом на 10 жовт. 2017 р. / К. І. Мягченко та ін. ; за заг. ред. І. М. Ливанова. Київ : ЦУЛ, 2017. 428 с."
        self.assertEqual(result, expected)

    def test_d1_5_punkt_5(self):
        """Д.1.5.5: Referencing styles"""
        bibtex = """@book{referencing2010,
            title = {Referencing styles},
            author = {Edwards, G. R. and others},
            publisher = {International Publishing},
            year = {2010},
            address = {Los Angeles},
            pages = {280}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Referencing styles / G. R. Edwards et al. Los Angeles : International Publishing, 2010. 280 p."
        self.assertEqual(result, expected)
