import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D8_Preprints(unittest.TestCase):
    """Д.8: Препринти (1 пункт)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d8_punkt_1(self):
        """Д.8.1: Марченко М. І., Кополович А. Д."""
        bibtex = """@techreport{marchenko2006,
            author = {Марченко, М. І. and Кополович, А. Д.},
            title = {Про точність визначення радіоактивних відходів гамма-методами},
            institution = {Ін-т з проблем безпеки АЕС НАН України},
            year = {2006},
            address = {Чорнобиль},
            pages = {7, [1]},
            note = {Препринт. НАН України, Ін-т проблем безпеки АЕС; 06-1}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Марченко М. І., Кополович А. Д. Про точність визначення радіоактивних відходів гамма-методами. Чорнобиль : Ін-т з проблем безпеки АЕС НАН України, 2006. 7, [1] с. (Препринт. НАН України, Ін-т проблем безпеки АЕС; 06-1)."
        self.assertEqual(result, expected)
