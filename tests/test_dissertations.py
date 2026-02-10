import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D4_Dissertations(unittest.TestCase):
    """Д.4: Дисертації (3 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d4_punkt_1(self):
        """Д.4.1: Петрук Л. А."""
        bibtex = """@phdthesis{petruk2004,
            author = {Петрук, Л. А.},
            title = {Дослідження статичного деформування складених тіл},
            type = {дис. ... канд. фіз.-мат. наук : 01.02.04},
            year = {2004},
            address = {Львів},
            pages = {140}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Петрук Л. А. Дослідження статичного деформування складених тіл : дис. ... канд. фіз.-мат. наук : 01.02.04. Львів, 2004. 140 с."
        self.assertEqual(result, expected)

    def test_d4_punkt_2(self):
        """Д.4.2: Пуріш С. В. (повторюється з Д.3, але як дисертація)"""
        bibtex = """@phdthesis{purish2024_dis,
            author = {Пуріш, С. В.},
            title = {Методи машинного навчання для розпізнавання людини за ходою},
            type = {автореф. дис… докт. філософії},
            school = {Національний університет «Одеська політехніка»},
            year = {2024},
            address = {Одеса},
            pages = {21},
            url = {https://op.edu.ua/sites/default/files/publicFiles/dissphd/ anotaciya_purish.pdf},
            urldate = {2024-12-20}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Пуріш С. В. Методи машинного навчання для розпізнавання людини за ходою : автореф. дис… докт. філософії. Одеса: Національний університет «Одеська політехніка», 2024. 21 с. URL: https://op.edu.ua/sites/default/files/publicFiles/dissphd/ anotaciya_purish.pdf (дата звернення: 20.12.2024)."
        self.assertEqual(result, expected)

    def test_d4_punkt_3(self):
        """Д.4.3: Олійник А. О. (повторюється з Д.3)"""
        bibtex = """@phdthesis{oliynyk2021_dis,
            author = {Олійник, А. О.},
            title = {Методи синтезу діагностичних моделей на основі обчислювального інтелекту},
            type = {автореф. дис… докт. техн. наук},
            school = {ХНУРЕ},
            year = {2021},
            address = {Харків},
            pages = {44},
            url = {https://nure.ua/wp-content/uploads/2021/Disertation/aref_oliinyk_06.pdf},
            urldate = {2023-09-12}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Олійник А. О. Методи синтезу діагностичних моделей на основі обчислювального інтелекту : автореф. дис… докт. техн. наук. Харків: ХНУРЕ, 2021. 44 c. URL: https://nure.ua/wp-content/uploads/2021/Disertation/aref_oliinyk_06.pdf (дата звернення: 12.09.2023)."
        self.assertEqual(result, expected)
