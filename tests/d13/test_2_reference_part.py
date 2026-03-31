import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D13_2_ReferencePart(unittest.TestCase):
    """Д.13.2: Частина довідкового видання (3 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d13_2_punkt_1(self):
        """Д.13.2.1: Павлик І. М."""
        bibtex = """@inbook{pavlyk2007,
            author = {Павлик, І. М.},
            title = {Право інтелектуальної власності},
            booktitle = {Великий енциклопедичний юридичний словник},
            editor = {Шемшученко, Ю. С.},
            editortype = {ред.},
            year = {2007},
            address = {Київ},
            pages = {683}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Павлик І. М. Право інтелектуальної власності. Великий енциклопедичний юридичний словник / ред. Ю. С. Шемшученко. Київ, 2007. С. 683."
        self.assertEqual(result, expected)

    def test_d13_2_punkt_2(self):
        """Д.13.2.2: Дичківська І. М."""
        bibtex = """@inbook{dychkivska_i2014,
            author = {Дичківська, І. М.},
            title = {Інноваційні педагогічні технології},
            booktitle = {Основи педагогіки освіти : словник термінів},
            editor = {Дмитрук, Т. О.},
            year = {2014},
            address = {Київ},
            pages = {54--55}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Дичківська І. М. Інноваційні педагогічні технології. Основи педагогіки освіти : словник термінів / ред. Т. О. Дмитрук. Київ, 2014. С. 54-55."
        self.assertEqual(result, expected)

    def test_d13_2_punkt_3(self):
        """Д.13.2.3: Попович Н. І."""
        bibtex = """@article{popovych2003,
            author = {Попович, Н. І.},
            title = {Початкова освіта},
            journal = {Педагогічна енциклопедія},
            year = {2003},
            address = {Київ},
            volume = {5},
            pages = {699}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Попович Н. І. Початкова освіта. Педагогічна енциклопедія. Київ, 2003. Т. 5. С. 699."
        self.assertEqual(result, expected)
