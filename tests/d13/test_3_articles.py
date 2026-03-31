import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D13_3_Articles(unittest.TestCase):
    """Д.13.3: Частина періодичного видання (8 пунктів)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d13_3_punkt_1(self):
        """Д.13.3.1: Кучеренко О. О."""
        bibtex = """@article{kucherenko2007,
            author = {Кучеренко, О. О.},
            title = {Конституційні права людини і громадянина},
            journal = {Часопис Київського університету права},
            year = {2007},
            number = {4},
            pages = {88--92}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Кучеренко О. О. Конституційні права людини і громадянина. Часопис Київського університету права. 2007. № 4. С. 88-92."
        self.assertEqual(result, expected)

    def test_d13_3_punkt_2(self):
        """Д.13.3.2: Загірняк М., Костенко А."""
        bibtex = """@article{zagirniak2017,
            author = {Загірняк, М. and Костенко, А.},
            title = {Про користування можливостями міжнародної бази даних Scopus},
            journal = {Вища школа},
            year = {2017},
            number = {5--6},
            pages = {48--55}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Загірняк М., Костенко А. Про користування можливостями міжнародної бази даних Scopus. Вища школа. 2017. № 5-6. С. 48-55."
        self.assertEqual(result, expected)

    def test_d13_3_punkt_3(self):
        """Д.13.3.3: Коваль Л., Коваль П."""
        bibtex = """@article{koval2017,
            author = {Коваль, Л. and Коваль, П.},
            title = {Переваги дистанційної роботи},
            journal = {Урядовий кур'єр},
            year = {2017},
            month = {1 листоп.},
            number = {205},
            pages = {5}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Коваль Л., Коваль П. Переваги дистанційної роботи. Урядовий кур'єр. 2017. 1 листоп. (№ 205). С. 5."
        self.assertEqual(result, expected)

    def test_d13_3_punkt_4(self):
        """Д.13.3.4: Bletskan D. I. et al."""
        bibtex = """@article{bletskan2017,
            author = {Bletskan, D. I. and Glukhov, K. E. and Frolova, V. V.},
            title = {Electronic structure of 2H-SnSe2},
            journal = {Semiconductor Physics Quantum Electronics & Optoelectronics},
            year = {2017},
            volume = {18},
            number = {2},
            pages = {109--118}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Bletskan D. I., Glukhov K. E., Frolova V. V. Electronic structure of 2H-SnSe2. Semiconductor Physics Quantum Electronics & Optoelectronics. 2017. Vol. 18, No 2. P. 109-118."
        self.assertEqual(result, expected)

    def test_d13_3_punkt_5(self):
        """Д.13.3.5: Zadereyko О., Trofymenko O. et al."""
        bibtex = """@article{zadereyko2022,
            author = {Zadereyko, О. and Trofymenko, O. and Prokop, Y. and Loginova, N. and Dyka, A. and Kukharenko, S.},
            title = {Research of potential data leaks in information and communication systems},
            journal = {Radio electronic and Computer Systems},
            year = {2022},
            number = {4},
            pages = {64--84},
            doi = {10.32620/reks.2022.4.05},
            urldate = {2022-11-03}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Zadereyko О., Trofymenko O., Prokop Y., Loginova N., Dyka A., Kukharenko S. Research of potential data leaks in information and communication systems / Radio electronic and Computer Systems. 2022. No 4. P. 64-84. DOI: https://doi.org/10.32620/reks.2022.4.05 (дата звернення: 03.11.2022)."
        self.assertEqual(result, expected)

    def test_d13_3_punkt_6(self):
        """Д.13.3.6: Трофименко О. Г., Дика А. І. et al. (5+ авторів)"""
        bibtex = """@article{trofymenko2024ai,
            author = {Трофименко, О. Г. and Дика, А. І. and Логінова, Н. І. and Задерейко, О. В. and Струк, Н. О.},
            title = {Штучний інтелект у військових навчальних симуляторах},
            journal = {Інформаційні технології та суспільство},
            year = {2024},
            number = {2(13)},
            pages = {89--95},
            doi = {10.32689/maup.it.2024.2.13},
            urldate = {2024-10-03}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Трофименко О. Г., Дика А. І., Логінова Н. І., Задерейко О. В., Струк Н. О. Штучний інтелект у військових навчальних симуляторах. Інформаційні технології та суспільство. 2024. № 2(13). C. 89-95. maup.it.2024.2.13 (дата звернення: 03.10.2024). DOI: https://doi.org/10.32689/"
        self.assertEqual(result, expected)

    def test_d13_3_punkt_7(self):
        """Д.13.3.7: Research of potential data leaks (назва спочатку, 6 авторів)"""
        bibtex = """@article{research2022,
            title = {Research of potential data leaks in information and communication systems},
            author = {Zadereyko, O. and Trofymenko, O. and Prokop, Y. and Loginova, N. and Dyka, A. and Kukharenko, S.},
            journal = {Radio electronic and Computer Systems},
            year = {2022},
            number = {4},
            pages = {64--84},
            doi = {10.32620/reks.2022.4.05},
            urldate = {2022-11-03}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Research of potential data leaks in information and communication systems / O. Zadereyko, O. Trofymenko, Y. Prokop, N. Loginova, A.Dyka, S. Kukharenko. Radio electronic and Computer Systems. 2022. No 4. P. 64-84. DOI: https://doi.org/10.32620/reks.2022.4.05 (дата звернення: 03.11.2022)."
        self.assertEqual(result, expected)

    def test_d13_3_punkt_8(self):
        """Д.13.3.8: Штучний інтелект (назва спочатку, 5 авторів)"""
        bibtex = """@article{ai2024,
            title = {Штучний інтелект у військових навчальних симуляторах},
            author = {Трофименко, O. Г. and Дика, А. І. and Логінова, Н. І. and Задерейко, О. В. and Струк, Н. О.},
            journal = {Інформаційні технології та суспільство},
            year = {2024},
            number = {2(13)},
            pages = {89--95},
            doi = {10.32689/maup.it.2024.2.13},
            urldate = {2024-10-03}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Штучний інтелект у військових навчальних симуляторах / O. Г. Трофименко, А. І. Дика, Н. І. Логінова, О. В. Задерейко, Н. О. Струк. Інформаційні технології та суспільство. 2024. № 2(13). C. 89-95. DOI: https://doi.org/10.32689/maup.it.2024.2.13 (дата звернення: 03.10.2024)."
        self.assertEqual(result, expected)
