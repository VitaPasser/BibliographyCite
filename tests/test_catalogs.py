import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D10_Catalogs(unittest.TestCase):
    """Д.10: Каталоги (2 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d10_punkt_1(self):
        """Д.10.1: Історична спадщина України"""
        bibtex = """@book{istorychna2000,
            title = {Історична спадщина України},
            type = {кат. вист.},
            note = {Харків. держ. наук. б-ка ім. В. Г. Короленка; уклад.: Л. І. Петров, О. В. Олійник},
            year = {2000},
            address = {Харків},
            pages = {64}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Історична спадщина України : кат. вист. / Харків. держ. наук. б-ка ім. В. Г. Короленка; уклад.: Л. І. Петров, О. В. Олійник. Харків, 2000. 64 с."
        self.assertEqual(result, expected)

    def test_d10_punkt_2(self):
        """Д.10.2: Пам'ятки історії та мистецтва"""
        bibtex = """@book{pamyatky2003,
            title = {Пам'ятки історії та мистецтва Закарпатської області},
            type = {кат.-довід.},
            note = {авт.упоряд.: М. Петрик та ін.; Упр. культури Закарпат. облдержадмін., Закарпат. іст. музей},
            year = {2003},
            address = {Ужгород},
            pages = {160}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Пам'ятки історії та мистецтва Закарпатської області : кат.-довід. / авт.упоряд.: М. Петрик та ін.; Упр. культури Закарпат. облдержадмін., Закарпат. іст. музей. Ужгород, 2003. 160 с."
        self.assertEqual(result, expected)
