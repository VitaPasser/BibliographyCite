import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D11_BiblioIndexes(unittest.TestCase):
    """Д.11: Бібліографічні покажчики (2 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d11_punkt_1(self):
        """Д.11.1: Боротьба з злочинністю"""
        bibtex = """@book{borotba2017,
            title = {Боротьба з злочинністю: нагальна проблема сучасності},
            type = {бібліогр. покажч. Вип. 3},
            note = {уклад.: О. В. Куріпта, відп. за вип. Н. М. Щур; Запорізький національний університет},
            year = {2017},
            address = {Запоріжжя},
            pages = {60}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Боротьба з злочинністю: нагальна проблема сучасності : бібліогр. покажч. Вип. 3 / уклад.: О. В. Куріпта, відп. за вип. Н. М. Щур; Запорізький національний університет. Запоріжжя, 2017. 60 с."
        self.assertEqual(result, expected)

    def test_d11_punkt_2(self):
        """Д.11.2: Валерій Степанович Ситніков"""
        bibtex = """@book{sytnikov2024,
            title = {Валерій Степанович Ситніков},
            type = {біобібліогр. покажчик},
            note = {уклад. : Т. Ю. Гнатюк ; відп. за вип. С. Г. Банокіна ; Нац. ун-т «Одес. політехніка»; Наук.техн. б-ка},
            year = {2024},
            address = {Одеса},
            pages = {93}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Валерій Степанович Ситніков : біобібліогр. покажчик / уклад. : Т. Ю. Гнатюк ; відп. за вип. С. Г. Банокіна ; Нац. ун-т «Одес. політехніка»; Наук.техн. б-ка. Одеса, 2024. 93 с."
        self.assertEqual(result, expected)
