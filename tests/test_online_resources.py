import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D12_OnlineResources(unittest.TestCase):
    """Д.12: Електронні ресурси (4 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d12_punkt_1(self):
        """Д.12.1: Зінченко Т."""
        bibtex = """@online{zinchenko2025,
            author = {Зінченко, Т.},
            title = {Про Soft Skills в окремо взятій європейській країні},
            url = {https://dou.ua/lenta/articles/soft-skills-eu/},
            urldate = {2025-01-06}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Зінченко Т. Про Soft Skills в окремо взятій європейській країні. https://dou.ua/lenta/articles/soft-skills-eu/. (дата звернення: 06.01.2025)."
        self.assertEqual(result, expected)

    def test_d12_punkt_2(self):
        """Д.12.2: Why Are Soft Skills So Hard?"""
        bibtex = """@online{softskills2025,
            title = {Why Are Soft Skills So Hard?},
            url = {https://trainingindustry.com/articles/leadership/why-are-soft-skills-so-hard/},
            urldate = {2025-02-05}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Why Are Soft Skills So Hard? https://trainingindustry.com/articles/leadership/why-are-soft-skills-so-hard/ (дата звернення: 05.02.2025)."
        self.assertEqual(result, expected)

    def test_d12_punkt_3(self):
        """Д.12.3: Хміль А. А."""
        bibtex = """@article{khmil2017,
            author = {Хміль, А. А.},
            title = {Функції державної служби за законодавством України},
            journal = {Юридичний науковий електронний журнал},
            year = {2017},
            number = {5},
            pages = {115--118},
            url = {http://lsej.org.ua/5_2017/32.pdf},
            urldate = {2022-12-04}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Хміль А. А. Функції державної служби за законодавством України // Юридичний науковий електронний журнал. 2017. № 5. С. 115–118. URL: http://lsej.org.ua/5_2017/32.pdf (дата звернення 04.12.2022)."
        self.assertEqual(result, expected)

    def test_d12_punkt_4(self):
        """Д.12.4: Хміль І. О."""
        bibtex = """@article{khmil_i2016,
            author = {Хміль, І. О.},
            title = {Шляхи подолання правового нігілізму в Україні},
            journal = {Вісник Запорізького національного університету. Юридичні науки},
            year = {2016},
            number = {3},
            pages = {20--27},
            address = {Запоріжжя},
            url = {http://ebooks.znu.edu.ua/files/Fakhovivydannya/vznu/juridichni/VestUr2015v3/5.pdf},
            urldate = {2017-11-15}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Хміль І. О. Шляхи подолання правового нігілізму в Україні. Вісник Запорізького національного університету. Юридичні науки. Запоріжжя, 2016. № 3. С. 20–27. – URL: http://ebooks.znu.edu.ua/files/Fakhovivydannya/vznu/juridichni/VestUr2015v3/5.pdf. (дата звернення: 15.11.2017)."
        self.assertEqual(result, expected)
