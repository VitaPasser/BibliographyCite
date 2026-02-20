import unittest
from bibliographycite import BibTeXToDSTUConverter


class TestDSTU_D1_6_NoAuthor(unittest.TestCase):
    """Д.1.6: Без автора (8 пунктів)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_6_punkt_1(self):
        """Д.1.6.1: 30 років історичному факультету"""
        bibtex = """@book{istfak2016,
            title = {30 років історичному факультету: історія та сьогодення (1986-2016)},
            type = {ювіл. вип.},
            editor = {Черепаня, В. В.},
            editortype = {заг. ред.},
            publisher = {ЗНУ},
            year = {2016},
            address = {Запоріжжя},
            pages = {340}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "30 років історичному факультету: історія та сьогодення (1986-2016) : ювіл. вип. / заг. ред. В. В. Черепаня. Запоріжжя : ЗНУ, 2016. 340 с."
        self.assertEqual(result, expected)

    def test_d1_6_punkt_2(self):
        """Д.1.6.2: Етнографія"""
        bibtex = """@book{etnografiya2018,
            title = {Етнографія},
            type = {конспект лекцій},
            editor = {Гарапко, В. І. and Гарапко, А. І.},
            editortype = {заг. ред. and уклад.},
            publisher = {ЦУЛ},
            year = {2018},
            address = {Київ},
            pages = {320}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Етнографія : конспект лекцій / заг. ред. В. І. Гарапко, уклад. А. І. Гарапко. Київ : ЦУЛ, 2018. 320 с."
        self.assertEqual(result, expected)

    def test_d1_6_punkt_3(self):
        """Д.1.6.3: Міжнародні відносини"""
        bibtex = """@book{mizhnarodn2016,
            title = {Міжнародні відносини},
            type = {монографія},
            editor = {Березовський, М. А.},
            publisher = {ЦУЛ},
            year = {2016},
            address = {Київ},
            pages = {162}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Міжнародні відносини : монографія / ред. М. А. Березовський. Київ : ЦУЛ, 2016. 162 с."
        self.assertEqual(result, expected)

    def test_d1_6_punkt_4(self):
        """Д.1.6.4: Міжнародні економічні відносини"""
        bibtex = """@book{mizhekonomichni2015,
            title = {Міжнародні економічні відносини},
            type = {навч. посіб.},
            editor = {Бедрій, П. О. and Петренко, О. О.},
            editortype = {за ред.},
            publisher = {ОНУ},
            year = {2015},
            address = {Одеса},
            pages = {306}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Міжнародні економічні відносини : навч. посіб. / ред. : П. О. Бедрій, О. О. Петренко. Одеса : ОНУ, 2015. 306 с."
        self.assertEqual(result, expected)

    def test_d1_6_punkt_5(self):
        """Д.1.6.5: Науково-практичний коментар Цивільного кодексу"""
        bibtex = """@book{tsyvilnyy2016,
            title = {Науково-практичний коментар Цивільного кодексу України},
            editor = {Тарнавський, Т. А.},
            editortype = {за заг. ред.},
            publisher = {ЦУЛ},
            year = {2016},
            address = {Київ},
            pages = {186}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Науково-практичний коментар Цивільного кодексу України / заг. ред. Т. А. Тарнавський. Київ : ЦУЛ, 2016. 186 с."
        self.assertEqual(result, expected)

    def test_d1_6_punkt_6(self):
        """Д.1.6.6: Підготовка фахівців у ВНЗ"""
        bibtex = """@book{pidgotovka2018,
            title = {Підготовка фахівців у ВНЗ в умовах реформування вищої освіти},
            type = {матеріали Всеукр. наук.-практ. конф., м. Мукачево, 4-5 жовт. 2018 р.},
            publisher = {МДУ},
            year = {2018},
            address = {Мукачево},
            pages = {226}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Підготовка фахівців у ВНЗ в умовах реформування вищої освіти : матеріали Всеукр. наук.-практ. конф., м. Мукачево, 4-5 жовт. 2018 р. Мукачево : МДУ, 2018. 226 с."
        self.assertEqual(result, expected)

    def test_d1_6_punkt_7(self):
        """Д.1.6.7: Освіта в Україні"""
        bibtex = """@book{osvita2017,
            title = {Освіта в Україні: виклики модернізації},
            type = {зб. наук. пр.},
            editor = {Марценюк, П. М. and others},
            editortype = {редкол. all},
            publisher = {Ін-т всесвітньої історії НАН України},
            year = {2017},
            address = {Київ},
            pages = {319}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Освіта в Україні: виклики модернізації : зб. наук. пр. / редкол. : П. М. Марценюк (відп. ред.) та ін. Київ : Ін-т всесвітньої історії НАН України, 2017. 319 с."
        self.assertEqual(result, expected)

    def test_d1_6_punkt_8(self):
        """Д.1.6.8: Товарознавство"""
        bibtex = """@book{tovaroznavstvo2014,
            title = {Товарознавство},
            note = {упоряд. В. Олексик},
            year = {2014},
            address = {Київ},
            pages = {804}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Товарознавство / упоряд. В. Олексик. Київ, 2014. 804 с."
        self.assertEqual(result, expected)
