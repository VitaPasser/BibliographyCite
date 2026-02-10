#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ПОВНИЙ набір тестів з ТОЧНОЮ відповідністю DSTU 8302:2015
===========================================================

КОЖЕН ПУНКТ зі стандарту має окремий тест з assertEqual!

Структура:
- Д.1.1: 7 пунктів (тести 1-7)
- Д.1.2: 6 пунктів (тести 8-13)
- Д.1.3: 3 пункти (тести 14-16)
- Д.1.4: 2 пункти (тести 17-18)
- Д.1.5: 5 пунктів (тести 19-23)
- Д.1.6: 8 пунктів (тести 24-31)
- Д.2: 4 пункти (тести 32-35)
- Д.3: 2 пункти (тести 36-37)
- Д.4: 3 пункти (тести 38-40)
- Д.5: 7 пунктів (тести 41-47)
- Д.6: 1 пункт (тест 48)
- Д.7: 3 пункти (тести 49-51)
- Д.8: 1 пункт (тест 52)
- Д.9: 3 пункти (тести 53-55)
- Д.10: 2 пункти (тести 56-57)
- Д.11: 2 пункти (тести 58-59)
- Д.12: 4 пункти (тести 60-63)
- Д.13.1: 4 пункти (тести 64-67)
- Д.13.2: 3 пункти (тести 68-70)
- Д.13.3: 8 пунктів (тести 71-78)
- Д.13.4: 3 пункти (тести 79-81)

ВСЬОГО: 81 тест - ПОВНЕ покриття стандарту!
"""

import unittest
from bibtex_to_dstu import BibTeXToDSTUConverter


class TestDSTU_D1_1_SingleAuthor(unittest.TestCase):
    """Д.1.1: Один автор (7 пунктів)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_1_punkt_1(self):
        """Д.1.1.1: Дичківська О. О."""
        bibtex = """@book{dychkivska2018,
            author = {Дичківська, О. О.},
            title = {Інноваційний менеджмент},
            subtitle = {конспект лекцій},
            publisher = {ДІА},
            year = {2018},
            address = {Київ},
            pages = {82}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Дичківська О. О. Інноваційний менеджмент : конспект лекцій. Київ : ДІА, 2018. 82 с."
        self.assertEqual(result, expected)

    def test_d1_1_punkt_2(self):
        """Д.1.1.2: Бондаренко В. Г."""
        bibtex = """@book{bondarenko2017,
            author = {Бондаренко, В. Г.},
            title = {Історія України},
            year = {2017},
            address = {Львів},
            pages = {153}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Бондаренко В. Г. Історія України. Львів, 2017. 153 с."
        self.assertEqual(result, expected)

    def test_d1_1_punkt_3(self):
        """Д.1.1.3: Лазор О. Я."""
        bibtex = """@book{lazor2003,
            author = {Лазор, О. Я.},
            title = {Державне управління у сфері реалізації екологічної політики в Україні: організаційно-правові засади},
            type = {монографія},
            publisher = {Ліга-Прес},
            year = {2003},
            address = {Львів},
            pages = {542}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Лазор О. Я. Державне управління у сфері реалізації екологічної політики в Україні: організаційно-правові засади : монографія. Львів : Ліга-Прес, 2003. 542 с."
        self.assertEqual(result, expected)

    def test_d1_1_punkt_4(self):
        """Д.1.1.4: Ваш О. М."""
        bibtex = """@book{vash2018,
            author = {Ваш, О. М.},
            title = {Етика},
            type = {навч.-метод. посіб.},
            publisher = {ЗНУ},
            year = {2018},
            address = {Запоріжжя},
            pages = {104}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Ваш О. М. Етика : навч.-метод. посіб. Запоріжжя : ЗНУ, 2018. 104 с."
        self.assertEqual(result, expected)

    def test_d1_1_punkt_5(self):
        """Д.1.1.5: Гурманова Л. І."""
        bibtex = """@book{gurmanova2017,
            author = {Гурманова, Л. І.},
            title = {Релігієзнавство},
            type = {навч. посіб.},
            edition = {2},
            note = {переробл. та допов.},
            publisher = {ЦУЛ},
            year = {2017},
            address = {Київ},
            pages = {193}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Гурманова Л. І. Релігієзнавство : навч. посіб. 2-ге вид., переробл. та допов. Київ : ЦУЛ, 2017. 193 с."
        self.assertEqual(result, expected)

    def test_d1_1_punkt_6(self):
        """Д.1.1.6: Parker J."""
        bibtex = """@book{parker2017,
            author = {Parker, J.},
            title = {Principles of scientific research},
            edition = {7},
            publisher = {Editorial},
            year = {2017},
            address = {London},
            pages = {301}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Parker J. Principles of scientific research. 7th ed. London : Editorial, 2017. 301 p."
        self.assertEqual(result, expected)

    def test_d1_1_punkt_7(self):
        """Д.1.1.7: Веретенко В. В."""
        bibtex = """@book{veretenko2015,
            author = {Веретенко, В. В.},
            title = {Міжнародний маркетинг},
            type = {монографія},
            editor = {Марценюк, В. М.},
            note = {за заг. наук. ред.},
            year = {2015},
            address = {Київ},
            pages = {374}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Веретенко В. В. Міжнародний маркетинг : монографія / за заг. наук. ред. В. М. Марценюка. Київ, 2015. 374 с."
        self.assertEqual(result, expected)


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
            author = {Бутенко, М. П. and Качур, В. П.},
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
        expected = "Бутенко М. П., Качур В. П. Психологія : навч. посіб. / за ред. М. П. Дутко. Київ : ЦУЛ, 2017. 332 с."
        self.assertEqual(result, expected)


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
        expected = "Бутенко М. П., Качур В. П., Петренко С. В. Психологія : навч. посіб. / за ред. М. П. Дутко. Київ : ЦУЛ, 2017. 332 с."
        self.assertEqual(result, expected)


class TestDSTU_D1_4_FourAuthors(unittest.TestCase):
    """Д.1.4: Чотири автори (2 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_4_punkt_1(self):
        """Д.1.4.1: Інновації"""
        bibtex = """@book{innovatsii2016,
            title = {Інновації},
            type = {навч. посіб.},
            author = {Гуревич, Д. Т. and Чекан, О. С. and Грибан, О. М. and Макарова, В. В.},
            publisher = {ЗНУ},
            year = {2016},
            address = {Запоріжжя},
            pages = {389}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Інновації : навч. посіб. / Гуревич Д. Т., Чекан О. С., Грибан О. М., Макарова В. В. Запоріжжя : ЗНУ, 2016. 389 с."
        self.assertEqual(result, expected)

    def test_d1_4_punkt_2(self):
        """Д.1.4.2: Моделювання програмного забезпечення"""
        bibtex = """@book{modelyuvannya2023,
            title = {Моделювання програмного забезпечення},
            type = {навч.-метод. посібник},
            author = {Манаков, С. Ю. and Трофименко, О. Г. and Лобода, Ю. Г. and Дика, А. І.},
            publisher = {Фенікс},
            year = {2023},
            address = {Одеса},
            pages = {145},
            url = {http://dspace.onua.edu.ua/handle/11300/25952},
            urldate = {2024-12-12}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Моделювання програмного забезпечення : навч.-метод. посібник / С. Ю. Манаков, О. Г. Трофименко, Ю. Г. Лобода, А. І. Дика. Одеса : Фенікс, 2023. 145 с. URL: http://dspace.onua.edu.ua/handle/11300/25952 (дата звернення: 12.12.2024)."
        self.assertEqual(result, expected)


class TestDSTU_D1_5_FiveOrMoreAuthors(unittest.TestCase):
    """Д.1.5: П'ять і більше авторів (5 пунктів)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_5_punkt_1(self):
        """Д.1.5.1: Операційний менеджмент"""
        bibtex = """@book{operational2011,
            title = {Операційний менеджмент},
            type = {підручник},
            author = {Поплавська, С. М. and others},
            publisher = {ЦУЛ},
            year = {2011},
            address = {Київ},
            pages = {267}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Операційний менеджмент : підручник / С. М. Поплавська та ін. Київ : ЦУЛ, 2011. 267 с."
        self.assertEqual(result, expected)

    def test_d1_5_punkt_2(self):
        """Д.1.5.2: Охорона праці"""
        bibtex = """@book{ohorona2017,
            title = {Охорона праці},
            type = {навч. посіб.},
            author = {Подольська, О. І. and others},
            edition = {2},
            publisher = {ЦУЛ},
            year = {2017},
            address = {Київ},
            pages = {264}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Охорона праці : навч. посіб. / О. І. Подольська та ін. 2-ге вид. Київ : ЦУЛ, 2017. 264 с."
        self.assertEqual(result, expected)

    def test_d1_5_punkt_3(self):
        """Д.1.5.3: Вища математика"""
        bibtex = """@book{vyshcha2015,
            title = {Вища математика},
            type = {конспект лекцій},
            author = {Ткачук, Т. С. and others},
            year = {2015},
            address = {Київ},
            pages = {82}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Вища математика : конспект лекцій / Ткачук Т.С. та ін. Київ, 2015. 82 с."
        self.assertEqual(result, expected)

    def test_d1_5_punkt_4(self):
        """Д.1.5.4: Науково-практичний коментар"""
        bibtex = """@book{komentar2017,
            title = {Науково-практичний коментар Цивільного кодексу України},
            note = {станом на 10 жовт. 2017 р.},
            author = {Мягченко, К. І. and others},
            editor = {Ливанов, І. М.},
            publisher = {ЦУЛ},
            year = {2017},
            address = {Київ},
            pages = {428}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Науково-практичний коментар Цивільного кодексу України : станом на 10 жовт. 2017 р. / К. І. Мягченко та ін. ; за заг. ред. І. М. Ливанова. Київ : ЦУЛ, 2017. 428 с."
        self.assertEqual(result, expected)

    def test_d1_5_punkt_5(self):
        """Д.1.5.5: Referencing styles"""
        bibtex = """@book{referencing2010,
            title = {Referencing styles},
            author = {Edwards, G. R. and others},
            publisher = {International Publishing},
            year = {2010},
            address = {Los Angeles},
            pages = {280}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Referencing styles / G. R. Edwards et al. Los Angeles : International Publishing, 2010. 280 p."
        self.assertEqual(result, expected)


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
            note = {під заг. ред.},
            publisher = {ЗНУ},
            year = {2016},
            address = {Запоріжжя},
            pages = {340}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "30 років історичному факультету: історія та сьогодення (1986-2016) : ювіл. вип. / під заг. ред. В. В. Черепані. Запоріжжя : ЗНУ, 2016. 340 с."
        self.assertEqual(result, expected)

    def test_d1_6_punkt_2(self):
        """Д.1.6.2: Етнографія"""
        bibtex = """@book{etnografiya2018,
            title = {Етнографія},
            type = {конспект лекцій},
            editor = {Гарапко, В. І.},
            note = {за заг. ред.; уклад. А. І. Гарапко},
            publisher = {ЦУЛ},
            year = {2018},
            address = {Київ},
            pages = {320}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Етнографія : конспект лекцій / за заг. ред. В. І. Гарапка; уклад. А. І. Гарапко. Київ : ЦУЛ, 2018. 320 с."
        self.assertEqual(result, expected)

    def test_d1_6_punkt_3(self):
        """Д.1.6.3: Міжнародні відносини"""
        bibtex = """@book{mizhnarodn2016,
            title = {Міжнародні відносини},
            type = {монографія},
            editor = {Березовський, М. А.},
            note = {за ред.},
            publisher = {ЦУЛ},
            year = {2016},
            address = {Київ},
            pages = {162}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Міжнародні відносини : монографія / за ред. М. А. Березовського. Київ : ЦУЛ, 2016. 162 с."
        self.assertEqual(result, expected)

    def test_d1_6_punkt_4(self):
        """Д.1.6.4: Міжнародні економічні відносини"""
        bibtex = """@book{mizhekonomichni2015,
            title = {Міжнародні економічні відносини},
            type = {навч. посіб.},
            editor = {Бедрій, П. О. and Петренко, О. О.},
            note = {за ред.},
            publisher = {ОНУ},
            year = {2015},
            address = {Одеса},
            pages = {306}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Міжнародні економічні відносини : навч. посіб. / за ред. : П. О. Бедрія, О. О. Петренка. Одеса : ОНУ, 2015. 306 с."
        self.assertEqual(result, expected)

    def test_d1_6_punkt_5(self):
        """Д.1.6.5: Науково-практичний коментар Цивільного кодексу"""
        bibtex = """@book{tsyvilnyy2016,
            title = {Науково-практичний коментар Цивільного кодексу України},
            editor = {Тарнавський, Т. А.},
            note = {за заг. ред.},
            publisher = {ЦУЛ},
            year = {2016},
            address = {Київ},
            pages = {186}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Науково-практичний коментар Цивільного кодексу України / за заг. ред. Т. А. Тарнавського. Київ : ЦУЛ, 2016. 186 с."
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
            note = {редкол.; відп. ред.},
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


class TestDSTU_D2_MultiVolume(unittest.TestCase):
    """Д.2: Книги (багатотомні видання) (4 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d2_punkt_1(self):
        """Д.2.1: Енциклопедія рослин"""
        bibtex = """@book{encyclopedia2016,
            title = {Енциклопедія рослин},
            editor = {Деркач, І. М. and others},
            note = {редкол.},
            publisher = {ЦУЛ},
            year = {2016},
            address = {Київ},
            volume = {8},
            pages = {812}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Енциклопедія рослин / редкол.: І. М. Деркач та ін. Київ : ЦУЛ, 2016. Т. 8. 812 с."
        self.assertEqual(result, expected)

    def test_d2_punkt_2(self):
        """Д.2.2: Антологія української юридичної думки"""
        bibtex = """@book{antologiya2002,
            title = {Антологія української юридичної думки},
            note = {Ін-т держави і права ім. В. М. Корецького НАНУ},
            editor = {Шемшученко, Ю. С.},
            publisher = {Юрид. кн.},
            year = {2002},
            address = {Київ},
            volume = {1},
            subtitle = {Загальна теорія держави і права, філософія та енциклопедія права},
            pages = {568}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Антологія української юридичної думки / Ін-т держави і права ім. В. М. Корецького НАНУ ; за заг. ред. Ю. С. Шемшученка. Київ : Юрид. кн., 2002. Т. 1 : Загальна теорія держави і права, філософія та енциклопедія права. 568 с."
        self.assertEqual(result, expected)

    def test_d2_punkt_3(self):
        """Д.2.3: Шевченківська енциклопедія"""
        bibtex = """@book{shevchenko2015,
            title = {Шевченківська енциклопедія},
            note = {у 6 т.},
            editor = {Жулинський, М. Г.},
            publisher = {Ін-т літератури ім. Т. Г. Шевченка},
            year = {2015},
            address = {Київ},
            volume = {6},
            pages = {697--699},
            url = {http://surl.li/nlzvlb},
            urldate = {2025-01-05}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Шевченківська енциклопедія : у 6 т. / голов. ред. М. Г. Жулинський. Київ: Ін-т літератури ім. Т. Г. Шевченка, 2015. Т. 6. С. 697–699. URL: http://surl.li/nlzvlb (дата звернення: 05.01.2025)."
        self.assertEqual(result, expected)

    def test_d2_punkt_4(self):
        """Д.2.4: Дендрофлора України"""
        bibtex = """@book{dendroflora2012,
            title = {Дендрофлора України. в 12 т. Т. 2. Дикорослі та культивовані дерева і кущі. Вип. 1. Покритонасінні},
            author = {Перхоменко, Л. І.},
            publisher = {Наукова думка},
            year = {2012},
            address = {Київ},
            pages = {200}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Дендрофлора України. в 12 т. Т. 2. Дикорослі та культивовані дерева і кущі. Вип. 1. Покритонасінні / Л. І. Перхоменко. Київ : Наукова думка, 2012. 200 с."
        self.assertEqual(result, expected)


class TestDSTU_D3_Dissertation(unittest.TestCase):
    """Д.3: Автореферати дисертацій (2 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d3_punkt_1(self):
        """Д.3.1: Пуріш С. В."""
        bibtex = """@phdthesis{purish2024,
            author = {Пуріш, С. В.},
            title = {Методи машинного навчання для розпізнавання людини за ходою},
            type = {автореф. дис… докт. філософії},
            school = {Національний університет «Одеська політехніка»},
            year = {2024},
            address = {Одеса},
            pages = {21},
            url = {https://op.edu.ua/sites/default/files/publicFiles/dissphd/anotaciya_purish.pdf},
            urldate = {2024-12-20}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Пуріш С. В. Методи машинного навчання для розпізнавання людини за ходою : автореф. дис… докт. філософії. Одеса: Національний університет «Одеська політехніка», 2024. 21 с. URL: https://op.edu.ua/sites/default/files/publicFiles/dissphd/anotaciya_purish.pdf (дата звернення: 20.12.2024)."
        self.assertEqual(result, expected)

    def test_d3_punkt_2(self):
        """Д.3.2: Олійник А. О."""
        bibtex = """@phdthesis{oliynyk2021,
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


class TestDSTU_D13_1_BookPart(unittest.TestCase):
    """Д.13.1: Частина книги (4 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d13_1_punkt_1(self):
        """Д.13.1.1: Петренко М. А."""
        bibtex = """@inbook{petrenko2009,
            author = {Петренко, М. А.},
            title = {Міжнародне право та роль Конституційного Суду України},
            booktitle = {Максим Петренко: право як буття вченого : зб. наук. пр. до 60-річчя проф. М. А. Петренко},
            editor = {Волошин, Ю. О.},
            note = {упоряд. та відп. ред.},
            year = {2009},
            address = {Київ},
            pages = {477--493}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Петренко М. А. Міжнародне право та роль Конституційного Суду України Максим Петренко: право як буття вченого : зб. наук. пр. до 60-річчя проф. М. А. Петренко / упоряд. та відп. ред. Ю. О. Волошин. Київ, 2009. С. 477–493."
        self.assertEqual(result, expected)

    def test_d13_1_punkt_2(self):
        """Д.13.1.2: Корнійчук Т. О."""
        bibtex = """@inbook{korniichuk2017,
            author = {Корнійчук, Т. О.},
            title = {Методи активізації навчально-пізнавальної діяльності},
            booktitle = {Педагогіка : навч. посіб.},
            editor = {Корнійчук, Т. О.},
            note = {за заг. ред.},
            year = {2017},
            address = {Київ},
            pages = {195--197}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Корнійчук Т. О. Методи активізації навчально-пізнавальної діяльності. Педагогіка : навч. посіб. / за заг. ред. Т. О. Корнійчука. Київ, 2017. С. 195–197."
        self.assertEqual(result, expected)

    def test_d13_1_punkt_3(self):
        """Д.13.1.3: Ярошевич Н. Б., Чубка О. М. Якимів А. І."""
        bibtex = """@inbook{yaroshevych2019,
            author = {Ярошевич, Н. Б. and Чубка, О. М. and Якимів, А. І.},
            title = {Інструменти боргового фінансування суб'єктів підприємництва в Україні: правовий статус, структурна динаміка, податкові наслідки},
            booktitle = {Теорія та методологія формування інвестиційно-фінансової стратегії розвитку національного господарства : монографія},
            editor = {Савчук, Л. М. and Череп, А. В.},
            note = {за ред.},
            year = {2019},
            address = {Дніпро},
            pages = {55--89}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Ярошевич Н. Б., Чубка О. М. Якимів А. І. Інструменти боргового фінансування суб'єктів підприємництва в Україні: правовий статус, структурна динаміка, податкові наслідки. Теорія та методологія формування інвестиційно-фінансової стратегії розвитку національного господарства : монографія / за ред. Л. М. Савчук, А. В. Череп. Дніпро, 2019. С. 55–89."
        self.assertEqual(result, expected)

    def test_d13_1_punkt_4(self):
        """Д.13.1.4: Goehr L."""
        bibtex = """@inbook{goehr2014,
            author = {Goehr, L.},
            title = {The concept of opera},
            booktitle = {The Oxford handbook of opera},
            editor = {Greenwald, H. M.},
            note = {ed. by},
            year = {2014},
            address = {Oxford},
            pages = {92--136}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Goehr L. The concept of opera. The Oxford handbook of opera / ed. by H. M. Greenwald. Oxford, 2014. P. 92–136."
        self.assertEqual(result, expected)


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
            note = {ред.},
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
            note = {за ред.},
            year = {2014},
            address = {Київ},
            pages = {54--55}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Дичківська І. М. Інноваційні педагогічні технології. Основи педагогіки освіти : словник термінів / за ред.: Т. О. Дмитрука. Київ, 2014. С. 54–55."
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
        expected = "Попович Н. І. Початкова освіта // Педагогічна енциклопедія. Київ, 2003. Т. 5. С. 699."
        self.assertEqual(result, expected)


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
        expected = "Кучеренко О. О. Конституційні права людини і громадянина. Часопис Київського університету права. 2007. № 4. С. 88–92."
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
        expected = "Загірняк М., Костенко А. Про користування можливостями міжнародної бази даних Scopus. Вища школа. 2017. № 5–6. С. 48–55."
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
        expected = "Bletskan D. I., Glukhov K. E., Frolova V. V. Electronic structure of 2H-SnSe2. Semiconductor Physics Quantum Electronics & Optoelectronics. 2017. Vol. 18, No 2. P. 109–118."
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
        expected = "Zadereyko О., Trofymenko O., Prokop Y., Loginova N., Dyka A., Kukharenko S. Research of potential data leaks in information and communication systems / Radio electronic and Computer Systems. 2022. No 4. P. 64–84. DOI: https://doi.org/10.32620/reks.2022.4.05 (дата звернення: 03.11.2022)."
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
        expected = "Трофименко О. Г., Дика А. І., Логінова Н. І., Задерейко О. В., Струк Н. О. Штучний інтелект у військових навчальних симуляторах. Інформаційні технології та суспільство. 2024. № 2(13). C. 89–95. maup.it.2024.2.13 (дата звернення: 03.10.2024). DOI: https://doi.org/10.32689/"
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
        expected = "Research of potential data leaks in information and communication systems / O. Zadereyko, O. Trofymenko, Y. Prokop, N. Loginova, A.Dyka, S. Kukharenko. Radio electronic and Computer Systems. 2022. No 4. P. 64–84. DOI: https://doi.org/10.32620/reks.2022.4.05 (дата звернення: 03.11.2022)."
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
        expected = "Штучний інтелект у військових навчальних симуляторах / O. Г. Трофименко, А. І. Дика, Н. І. Логінова, О. В. Задерейко, Н. О. Струк. Інформаційні технології та суспільство. 2024. № 2(13). C. 89–95. DOI: https://doi.org/10.32689/maup.it.2024.2.13 (дата звернення: 03.10.2024)."
        self.assertEqual(result, expected)


class TestDSTU_D13_4_Conferences(unittest.TestCase):
    """Д.13.4: Частина видання матеріалів конференцій (3 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d13_4_punkt_1(self):
        """Д.13.4.1: Трофименко О. Г., Єфремов В. А."""
        bibtex = """@inproceedings{trofymenko2024conf,
            author = {Трофименко, О. Г. and Єфремов, В. А.},
            title = {Оснащення 3D-моделей анімаційних персонажів у розробці ігор},
            booktitle = {Актуальні питання автоматизації та інформаційних технологій (АТІТ-2024) : матер. III Всеукр. наук.-практ. конф.},
            note = {21–22 листопада 2024 р., Кременчук},
            year = {2024},
            pages = {115--116},
            url = {https://atit.kdu.edu.ua/publ.php},
            urldate = {2024-12-16}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Трофименко О. Г., Єфремов В. А. Оснащення 3D-моделей анімаційних персонажів у розробці ігор. Актуальні питання автоматизації та інформаційних технологій (АТІТ-2024) : матер. III Всеукр. наук.-практ. конф., 21–22 листопада 2024 р., Кременчук. С. 115–116. URL: https://atit.kdu.edu.ua/publ.php (дата звернення: 16.12.2024)."
        self.assertEqual(result, expected)

    def test_d13_4_punkt_2(self):
        """Д.13.4.2: Максименко Д. В."""
        bibtex = """@inproceedings{maksymenko2013,
            author = {Максименко, Д. В.},
            title = {Методи оперативної діагностики виробничої діяльності підприємства},
            booktitle = {Зростання ролі бухгалтерського обліку в сучасній економіці : зб. тез та доповідей І Міжнарод. наук.-практ. конф. (м. Київ, 21 лютого 2013 р.)},
            editor = {Мельничук, Б. В.},
            note = {відпов. за вип.},
            year = {2013},
            address = {Київ},
            pages = {331--335}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Максименко Д. В. Методи оперативної діагностики виробничої діяльності підприємства. Зростання ролі бухгалтерського обліку в сучасній економіці : зб. тез та доповідей І Міжнарод. наук.-практ. конф. (м. Київ, 21 лютого 2013 р.) / відпов. за вип. Мельничук Б. В. Київ, 2013. С.331–335."
        self.assertEqual(result, expected)

    def test_d13_4_punkt_3(self):
        """Д.13.4.3: Prokop Y., Trofymenko O., Zadereyko O."""
        bibtex = """@inproceedings{prokop2023,
            author = {Prokop, Y. and Trofymenko, O. and Zadereyko, O.},
            title = {Developing code style skills in students},
            booktitle = {IEEE 18th International Conference on Computer Science and Information Technologies (CSIT)},
            note = {October 19–21, 2023, Lviv, Ukraine},
            year = {2023},
            pages = {1--4},
            doi = {10.1109/CSIT61576.2023.10324182},
            urldate = {2024-07-12}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Prokop Y., Trofymenko O., Zadereyko O. Developing code style skills in students. IEEE 18th International Conference on Computer Science and Information Technologies (CSIT). October 19–21, 2023, Lviv, Ukraine. P. 1–4. DOI: https://doi.org/10.1109/CSIT61576.2023.10324182. (дата звернення: 12.07.2024)."
        self.assertEqual(result, expected)


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


class TestDSTU_D6_ArchivalDocuments(unittest.TestCase):
    """Д.6: Архівні документи (1 пункт)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d6_punkt_1(self):
        """Д.6.1: Лист Голови Спілки «Первоцвіт»"""
        bibtex = """@misc{pervotsvit1989,
            title = {Лист Голови Спілки «Первоцвіт» Г. Ф. Петренка на ім'я Голови Ради Міністрів УРСР В. А. Поповича щодо реєстрації Статуту Спілки та сторінки Статуту. 14 грудня 1989 р.},
            note = {ЦДАГО України (Центр. держ. архів громад. Об'єднань України). Ф. 1. Оп. 32. Спр. 2612. Арк. 63, 64 зв., 71}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Лист Голови Спілки «Первоцвіт» Г. Ф. Петренка на ім'я Голови Ради Міністрів УРСР В. А. Поповича щодо реєстрації Статуту Спілки та сторінки Статуту. 14 грудня 1989 р. ЦДАГО України (Центр. держ. архів громад. Об'єднань України). Ф. 1. Оп. 32. Спр. 2612. Арк. 63, 64 зв., 71."
        self.assertEqual(result, expected)


class TestDSTU_D7_Patents(unittest.TestCase):
    """Д.7: Патенти та авторські свідоцтва (3 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d7_punkt_1(self):
        """Д.7.1: Зернозбиральний комбайн"""
        bibtex = """@misc{patent25742,
            title = {Зернозбиральний комбайн: пат. 25742 Україна: МПК6С09К11/00, G01Т1/28, G21НЗ/00},
            note = {№ 200701472; заявл. 12.02.07; опубл. 27.08.07, Бюл. № 13. 4 с.}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Зернозбиральний комбайн: пат. 25742 Україна: МПК6С09К11/00, G01Т1/28, G21НЗ/00. № 200701472; заявл. 12.02.07; опубл. 27.08.07, Бюл. № 13. 4 с."
        self.assertEqual(result, expected)

    def test_d7_punkt_2(self):
        """Д.7.2: Спосіб лікування гіперактивності"""
        bibtex = """@misc{patent76509,
            title = {Спосіб лікування гіперактивності у дітей: пат. 76509 Україна},
            note = {№ 2004042416; заявл. 01.04.2004; опубл. 01.08.2006, Бюл. № 8 (кн. 1). 120 с.}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Спосіб лікування гіперактивності у дітей: пат. 76509 Україна. № 2004042416; заявл. 01.04.2004; опубл. 01.08.2006, Бюл. № 8 (кн. 1). 120 с."
        self.assertEqual(result, expected)

    def test_d7_punkt_3(self):
        """Д.7.3: Комп'ютерна програма «Black Sea Hanter»"""
        bibtex = """@misc{blacksea2024,
            title = {А.с. № 129198 від 21.08.2024. Комп'ютерна програма «Black Sea Hanter»},
            author = {Струк, Н. О. and Дика, А. І. and Задерейко, О. В. and Логінова, Н. І. and Трофименко, О. Г.},
            url = {https://sis.nipo.gov.ua/uk/search/detail/1821799/},
            urldate = {2024-12-12}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "А.с. № 129198 від 21.08.2024. Комп'ютерна програма «Black Sea Hanter» / Н. О. Струк, А. І. Дика, О. В. Задерейко, Н. І Логінова., О. Г. Трофименко https://sis.nipo.gov.ua/uk/search/detail/1821799/ (дата звернення: 12.12.2024)."
        self.assertEqual(result, expected)


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


class TestDSTU_D9_Standards(unittest.TestCase):
    """Д.9: Стандарти (3 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d9_punkt_1(self):
        """Д.9.1: ДСТУ 7152:2010"""
        bibtex = """@techreport{dstu7152,
            title = {ДСТУ 7152:2010. Видання. Оформлення публікацій у журналах і збірниках},
            note = {[Чинний від 2010-02-18]. Вид. офіц.},
            year = {2010},
            address = {Київ},
            pages = {16},
            series = {Інформація та документація}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "ДСТУ 7152:2010. Видання. Оформлення публікацій у журналах і збірниках. [Чинний від 2010-02-18]. Вид. офіц. Київ, 2010. 16 с. (Інформація та документація)."
        self.assertEqual(result, expected)

    def test_d9_punkt_2(self):
        """Д.9.2: ДСТУ ISO 6107-1:2004"""
        bibtex = """@techreport{dstu_iso6107,
            title = {ДСТУ ISO 6107-1:2004. Якість води. Словник термінів. Частина 1 (ISO 6107-1:1996, IDТ)},
            note = {[Чинний від 2005-04-01]. Вид. офіц.},
            publisher = {Держспоживстандарт України},
            year = {2006},
            address = {Київ},
            pages = {181}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "ДСТУ ISO 6107-1:2004. Якість води. Словник термінів. Частина 1 (ISO 6107-1:1996, IDТ). [Чинний від 2005-04-01]. Вид. офіц. Київ : Держспоживстандарт України, 2006. 181 с."
        self.assertEqual(result, expected)

    def test_d9_punkt_3(self):
        """Д.9.3: ДСТУ 3582:2013"""
        bibtex = """@techreport{dstu3582,
            title = {ДСТУ 3582:2013. Бібліографічний опис. Скорочення слів і словосполучень українською мовою. Загальні вимоги та правила (ISO 4: 1984, NEQ; ISO 832:1994, NEQ)},
            note = {[На заміну ДСТУ3582-97; чинний від 2013-08-22]. 3 Вид. офіц.},
            publisher = {Мінекономрозвитку України},
            year = {2014},
            address = {Київ},
            pages = {15},
            series = {Інформація та документація}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "ДСТУ 3582:2013. Бібліографічний опис. Скорочення слів і словосполучень українською мовою. Загальні вимоги та правила (ISO 4: 1984, NEQ; ISO 832:1994, NEQ). [На заміну ДСТУ3582-97; чинний від 2013-08-22]. 3 Вид. офіц. Київ : Мінекономрозвитку України, 2014. 15 с. (Інформація та документація)."
        self.assertEqual(result, expected)


class TestDSTU_D10_Catalogs(unittest.TestCase):
    """Д.10: Каталоги (2 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d10_punkt_1(self):
        """Д.10.1: Історична спадщина України"""
        bibtex = """@book{istorychna2000,
            title = {Історична спадщина України},
            type = {кат. вист.},
            note = {Харків. держ. наук. б-ка ім. В. Г. Короленка; уклад.: Л. І. Петров, О. В. Олійник},
            year = {2000},
            address = {Харків},
            pages = {64}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Історична спадщина України : кат. вист. / Харків. держ. наук. б-ка ім. В. Г. Короленка; уклад.: Л. І. Петров, О. В. Олійник. Харків, 2000. 64 с."
        self.assertEqual(result, expected)

    def test_d10_punkt_2(self):
        """Д.10.2: Пам'ятки історії та мистецтва"""
        bibtex = """@book{pamyatky2003,
            title = {Пам'ятки історії та мистецтва Закарпатської області},
            type = {кат.-довід.},
            note = {авт.упоряд.: М. Петрик та ін.; Упр. культури Закарпат. облдержадмін., Закарпат. іст. музей},
            year = {2003},
            address = {Ужгород},
            pages = {160}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Пам'ятки історії та мистецтва Закарпатської області : кат.-довід. / авт.упоряд.: М. Петрик та ін.; Упр. культури Закарпат. облдержадмін., Закарпат. іст. музей. Ужгород, 2003. 160 с."
        self.assertEqual(result, expected)


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


def run_all_tests():
    """Запуск ВСІХ тестів з точною відповідністю"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Всі тестові класи
    test_classes = [
        TestDSTU_D1_1_SingleAuthor,      # 7 тестів
        TestDSTU_D1_2_TwoAuthors,         # 6 тестів
        TestDSTU_D1_3_ThreeAuthors,       # 3 тести
        TestDSTU_D1_4_FourAuthors,        # 2 тести
        TestDSTU_D1_5_FiveOrMoreAuthors,  # 5 тестів
        TestDSTU_D1_6_NoAuthor,           # 8 тестів
        TestDSTU_D2_MultiVolume,          # 4 тести
        TestDSTU_D3_Dissertation,         # 2 тести
        TestDSTU_D4_Dissertations,        # 3 тести
        TestDSTU_D5_LegalDocuments,       # 7 тестів
        TestDSTU_D6_ArchivalDocuments,    # 1 тест
        TestDSTU_D7_Patents,              # 3 тести
        TestDSTU_D8_Preprints,            # 1 тест
        TestDSTU_D9_Standards,            # 3 тести
        TestDSTU_D10_Catalogs,            # 2 тести
        TestDSTU_D11_BiblioIndexes,       # 2 тести
        TestDSTU_D12_OnlineResources,     # 4 тести
        TestDSTU_D13_1_BookPart,          # 4 тести
        TestDSTU_D13_2_ReferencePart,     # 3 тести
        TestDSTU_D13_3_Articles,          # 8 тестів
        TestDSTU_D13_4_Conferences,       # 3 тести
    ]

    for test_class in test_classes:
        suite.addTests(loader.loadTestsFromTestCase(test_class))

    # Запуск
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Підсумок
    print("\n" + "=" * 80)
    print("ПОВНИЙ ПІДСУМОК ТЕСТУВАННЯ З ТОЧНОЮ ВІДПОВІДНІСТЮ")
    print("=" * 80)
    print(f"Всього тестів: {result.testsRun}")
    print(f"Успішно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Помилки: {len(result.failures)}")
    print(f"Винятки: {len(result.errors)}")
    print("=" * 80)
    print("\n📊 ПОКРИТТЯ СТАНДАРТУ:")
    print("   Д.1: Книги (всі підрозділи) - 31 тест")
    print("   Д.2: Багатотомні - 4 тести")
    print("   Д.3: Автореферати - 2 тести")
    print("   Д.4: Дисертації - 3 тести")
    print("   Д.5: Законодавчі - 7 тестів")
    print("   Д.6: Архівні - 1 тест")
    print("   Д.7: Патенти - 3 тести")
    print("   Д.8: Препринти - 1 тест")
    print("   Д.9: Стандарти - 3 тести")
    print("   Д.10: Каталоги - 2 тести")
    print("   Д.11: Бібліографічні покажчики - 2 тести")
    print("   Д.12: Електронні ресурси - 4 тести")
    print("   Д.13: Частини видань - 18 тестів")
    print("   " + "-" * 76)
    print("   ВСЬОГО: 81 тест - 100% ПОКРИТТЯ!")
    print("=" * 80)

    if result.wasSuccessful():
        print("\n✅ ВСІ 81 ТЕСТ ПРОЙДЕНО!")
    else:
        print(f"\n⚠️  {len(result.failures) + len(result.errors)} тестів потребують доопрацювання конвертера")

    print("=" * 80)
    return result


if __name__ == '__main__':
    print("\n📋 ПОВНИЙ набір тестів для ВСІХ пунктів DSTU 8302:2015\n")
    print("Тестів: 81 (7+6+3+2+5+8+4+2+3+7+1+3+1+3+2+2+4+4+3+8+3)")
    print("Розділи: Д.1.1-Д.1.6, Д.2-Д.11, Д.12, Д.13.1-Д.13.4")
    print("Покриття: 100% всіх пунктів стандарту!\n")
    run_all_tests()
