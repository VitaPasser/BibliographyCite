import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D5_LegalDocuments(unittest.TestCase):
    """Д.5: Законодавчі та нормативні документи (7 пунктів)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d5_punkt_1(self):
        """Д.5.1: Конституція України"""
        bibtex = """@book{konstytutsia2017,
            title = {Конституція України},
            note = {станом на 1 жовтня 2017 р.},
            author = {Верховна Рада України},
            publisher = {Право},
            year = {2017},
            address = {Київ},
            pages = {93}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Конституція України : станом на 1 жовтня 2017 р. / Верховна Рада України. Київ : Право, 2017. 93 с."
        self.assertEqual(result, expected)

    def test_d5_punkt_2(self):
        """Д.5.2: Про вищу освіту"""
        bibtex = """@misc{vyshcha_osvita2024,
            title = {Про вищу освіту: Закон України № 1556-VII, редакція від 17.11.2024},
            url = {https://zakon.rada.gov.ua/laws/show/1556-18#Text},
            urldate = {2024-12-12}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Про вищу освіту: Закон України № 1556-VII, редакція від 17.11.2024. URL: https://zakon.rada.gov.ua/laws/show/1556-18#Text (дата звернення: 12.12.2024)."
        self.assertEqual(result, expected)

    def test_d5_punkt_3(self):
        """Д.5.3: Податковий кодекс України"""
        bibtex = """@article{podatkovyy2011,
            title = {Податковий кодекс України : Закон України від 19.05.2011 № 3393-VI},
            journal = {Відомості Верховної Ради України},
            year = {2011},
            number = {48–49},
            pages = {536},
            note = {Ст.}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Податковий кодекс України : Закон України від 19.05.2011 № 3393-VI. Відомості Верховної Ради України. 2011. № 48–49. Ст. 536."
        self.assertEqual(result, expected)

    def test_d5_punkt_4(self):
        """Д.5.4: Питання соціального забезпечення"""
        bibtex = """@article{sotsialne2018,
            title = {Питання соціального забезпечення : Постанова Кабінету Міністрів України від 28.12.2017 № 1060},
            journal = {Офіційний вісник України},
            year = {2018},
            number = {5},
            pages = {430--443}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Питання соціального забезпечення : Постанова Кабінету Міністрів України від 28.12.2017 № 1060. Офіційний вісник України. 2018. № 5. С. 430–443."
        self.assertEqual(result, expected)

    def test_d5_punkt_5(self):
        """Д.5.5: Про інформування громадськості"""
        bibtex = """@article{informuvannya2018,
            title = {Про інформування громадськості з питань євроатлантичної інтеграції України на 2019-2020 роки : Указ Президента України від 21.02.2018 № 43/2018},
            journal = {Урядовий кур'єр},
            year = {2018},
            month = {23 лют.},
            number = {35},
            pages = {10}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Про інформування громадськості з питань євроатлантичної інтеграції України на 2019-2020 роки : Указ Президента України від 21.02.2018 № 43/2018. Урядовий кур'єр. 2018. 23 лют. (№ 35). С. 10."
        self.assertEqual(result, expected)

    def test_d5_punkt_6(self):
        """Д.5.6: Про затвердження Вимог"""
        bibtex = """@article{vymohy2018,
            title = {Про затвердження Вимог до оформлення кандидатської дисертації : наказ Міністерства освіти і науки від 12.01.2018 № 50},
            journal = {Офіційний вісник України},
            year = {2018},
            number = {25},
            pages = {139--141}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Про затвердження Вимог до оформлення кандидатської дисертації : наказ Міністерства освіти і науки від 12.01.2018 № 50. Офіційний вісник України. 2018. № 25. С. 139–141."
        self.assertEqual(result, expected)

    def test_d5_punkt_7(self):
        """Д.5.7: Інструкція щодо порядку оформлення"""
        bibtex = """@article{instruktsia2006,
            title = {Інструкція щодо порядку оформлення і ведення особових справ отримувачів усіх видів соціальної допомоги : затв. наказом М-ва. праці та соц. політики від 19.09.2006 № 156},
            journal = {Баланс-бюджет},
            year = {2006},
            month = {19 верес.},
            number = {18},
            pages = {15--16}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Інструкція щодо порядку оформлення і ведення особових справ отримувачів усіх видів соціальної допомоги : затв. наказом М-ва. праці та соц. політики від 19.09.2006 № 156. Баланс-бюджет. 2006. 19 верес. (№ 18). С. 15–16."
        self.assertEqual(result, expected)
