import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D1_2_TwoAuthors(unittest.TestCase):
    """Д.1.2: Два автори (6 пунктів)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_2_punkt_1(self):
        """Д.1.2.1: Мартиненко З. Е., Макар І. В."""
        bibtex = """@book{martynenko2017,
            author = {Мартиненко, З. Е. and Макар, І. В.},
            title = {Управління підприємством: теоретико-методичні засади},
            type = {монографія},
            publisher = {Щедра садиба плюс},
            year = {2017},
            address = {Харків},
            pages = {296}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Мартиненко З. Е., Макар І. В. Управління підприємством: теоретико-методичні засади : монографія. Харків : Щедра садиба плюс, 2017. 296 с."
        self.assertEqual(result, expected)

    def test_d1_2_punkt_2(self):
        """Д.1.2.2: Палеха В. І., Карпова П. В."""
        bibtex = """@book{palekha2015,
            author = {Палеха, В. І. and Карпова, П. В.},
            title = {Менеджмент організацій},
            type = {навч. посіб.},
            publisher = {ЗНУ},
            year = {2015},
            address = {Запоріжжя},
            pages = {120}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Палеха В. І., Карпова П. В. Менеджмент організацій : навч. посіб. Запоріжжя : ЗНУ, 2015. 120 с."
        self.assertEqual(result, expected)

    def test_d1_2_punkt_3(self):
        """Д.1.2.3: Білоус С. І., Корнійчук В. П."""
        bibtex = """@book{bilous2016,
            author = {Білоус, С. І. and Корнійчук, В. П.},
            title = {Філософія освіти},
            type = {навч.-метод. посіб.},
            year = {2016},
            address = {Переяслав-Хмельницький},
            pages = {176}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Білоус С. І., Корнійчук В. П. Філософія освіти : навч.-метод. посіб. Переяслав-Хмельницький, 2016. 176 с."
        self.assertEqual(result, expected)

    def test_d1_2_punkt_4(self):
        """Д.1.2.4: Трофименко О. Г., Дика А. І."""
        bibtex = """@book{trofymenko2024,
            author = {Трофименко, О. Г. and Дика, А. І.},
            title = {Тестування та забезпечення якості програмних систем},
            type = {навч. посібник [Електронне видання]},
            publisher = {Фенікс},
            year = {2024},
            address = {Одеса},
            pages = {195},
            url = {https://hdl.handle.net/11300/27717},
            urldate = {2022-11-03}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Трофименко О. Г., Дика А. І. Тестування та забезпечення якості програмних систем : навч. посібник [Електронне видання] Одеса : Фенікс, 2024. 195 с. URL: https://hdl.handle.net/11300/27717 (дата звернення: 03.11.2022)."
        self.assertEqual(result, expected)

    def test_d1_2_punkt_5(self):
        """Д.1.2.5: Вердіна С. А., Волков А. А."""
        bibtex = """@book{verdina2017,
            author = {Вердіна, С. А. and Волков, А. А.},
            title = {Контролінг},
            type = {навч. посіб.},
            edition = {3},
            note = {переробл. та допов.},
            year = {2017},
            address = {Херсон},
            pages = {212}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Вердіна С. А., Волков А. А. Контролінг : навч. посіб. 3-тє вид., переробл. та допов. Херсон, 2017. 212 с."
        self.assertEqual(result, expected)

    def test_d1_2_punkt_6(self):
        """Д.1.2.6: Бутенко М. П., Качур В. П."""
        bibtex = """@book{butenko2017,
            author = {Бутенко Микола Петрович and Качур, В. П.},
            title = {Психологія},
            type = {навч. посіб.},
            editor = {Дутко, М. П.},
            publisher = {ЦУЛ},
            year = {2017},
            address = {Київ},
            pages = {332}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Бутенко М. П., Качур В. П. Психологія : навч. посіб. / ред. М. П. Дутко. Київ : ЦУЛ, 2017. 332 с."
        self.assertEqual(result, expected)
