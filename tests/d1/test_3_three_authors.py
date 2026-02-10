import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D1_3_ThreeAuthors(unittest.TestCase):
    """Д.1.3: Три автори (3 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_3_punkt_1(self):
        """Д.1.3.1: Тарнавська Г. Я., Марценюк Н. С., Герасимова Т. М."""
        bibtex = """@book{tarnavska2017,
            author = {Тарнавська, Г. Я. and Марценюк, Н. С. and Герасимова, Т. М.},
            title = {Фінанси},
            type = {навч. посіб.},
            publisher = {Магнолія 2006},
            year = {2017},
            address = {Львів},
            pages = {412}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Тарнавська Г. Я., Марценюк Н. С., Герасимова Т. М. Фінанси : навч. посіб. Львів : Магнолія 2006, 2017. 412 с."
        self.assertEqual(result, expected)

    def test_d1_3_punkt_2(self):
        """Д.1.3.2: Пустовенко В. В., Максименко І. Л., Яким А. С."""
        bibtex = """@book{pustovenko2017,
            author = {Пустовенко, В. В. and Максименко, І. Л. and Яким, А. С.},
            title = {Безпека життєдіяльності},
            type = {монографія},
            publisher = {ХНПУ},
            year = {2017},
            address = {Харків},
            pages = {348}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Пустовенко В. В., Максименко І. Л., Яким А. С. Безпека життєдіяльності : монографія. Харків : ХНПУ, 2017. 348 с."
        self.assertEqual(result, expected)

    def test_d1_3_punkt_3(self):
        """Д.1.3.3: Бутенко М. П., Качур В. П., Петренко С. В."""
        bibtex = """@book{butenko2017_3,
            author = {Бутенко, М. П. and Качур, В. П. and Петренко, С. В.},
            title = {Психологія},
            type = {навч. посіб.},
            editor = {Дутко, М. П.},
            note = {за ред.},
            publisher = {ЦУЛ},
            year = {2017},
            address = {Київ},
            pages = {332}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Бутенко М. П., Качур В. П., Петренко С. В. Психологія : навч. посіб. / ред. М. П. Дутко. Київ : ЦУЛ, 2017. 332 с."
        self.assertEqual(result, expected)
