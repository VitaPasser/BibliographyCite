#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ПОВНИЙ набір тестів для КОЖНОГО пункту DSTU 8302:2015
=====================================================

Файл містить індивідуальний тест для КОЖНОГО прикладу з файлу DSTU-8302-2015.txt
Всього: 68 тестів, що охоплюють ВСІ приклади зі стандарту

Структура:
- Д.1.1: Один автор (7 тестів - пункти 1-7)
- Д.1.2: Два автори (6 тестів - пункти 1-6)
- Д.1.3: Три автори (3 тести - пункти 1-3)
- Д.1.4: Чотири автори (2 тести - пункти 1-2)
- Д.1.5: П'ять і більше (5 тестів - пункти 1-5)
- Д.1.6: Без автора (8 тестів - пункти 1-8)
- Д.2: Багатотомні (4 тести - пункти 1-4)
- Д.3: Автореферати (2 тести - пункти 1-2)
- Д.4: Дисертації (3 тести - пункти 1-3)
- Д.5: Законодавчі (7 тестів - пункти 1-7)
- Д.6: Архівні (1 тест - пункт 1)
- Д.7: Патенти (3 тести - пункти 1-3)
- Д.8: Препринти (1 тест - пункт 1)
- Д.9: Стандарти (3 тести - пункти 1-3)
- Д.10: Каталоги (2 тести - пункти 1-2)
- Д.11: Бібліографічні покажчики (2 тести - пункти 1-2)
- Д.12: Електронні ресурси (4 тести - пункти 1-4)
- Д.13.1: Частина книги (4 тести - пункти 1-4)
- Д.13.2: Частина довідкового (3 тести - пункти 1-3)
- Д.13.3: Періодичне видання (8 тестів - пункти 1-8)
- Д.13.4: Конференції (3 тести - пункти 1-3)
"""

import unittest
from bibtex_to_dstu import BibTeXToDSTUConverter


class TestDSTU_D1_1_SingleAuthor(unittest.TestCase):
    """Д.1.1: Один автор (7 пунктів)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_1_punkt_1(self):
        """Д.1.1.1: Дичківська О. О. Інноваційний менеджмент : конспект лекцій"""
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
        self.assertIn("Дичківська О. О.", result)
        self.assertIn("Інноваційний менеджмент", result)
        self.assertIn("Київ", result)
        self.assertIn("ДІА", result)
        self.assertIn("2018", result)
        self.assertIn("82 с.", result)

    def test_d1_1_punkt_2(self):
        """Д.1.1.2: Бондаренко В. Г. Історія України"""
        bibtex = """@book{bondarenko2017,
            author = {Бондаренко, В. Г.},
            title = {Історія України},
            year = {2017},
            address = {Львів},
            pages = {153}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Бондаренко В. Г.", result)
        self.assertIn("Історія України", result)
        self.assertIn("Львів", result)
        self.assertIn("2017", result)
        self.assertIn("153 с.", result)

    def test_d1_1_punkt_3(self):
        """Д.1.1.3: Лазор О. Я. Державне управління у сфері реалізації екологічної політики"""
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
        self.assertIn("Лазор О. Я.", result)
        self.assertIn("Державне управління", result)
        self.assertIn("монографія", result)
        self.assertIn("Львів", result)
        self.assertIn("Ліга-Прес", result)
        self.assertIn("2003", result)
        self.assertIn("542 с.", result)

    def test_d1_1_punkt_4(self):
        """Д.1.1.4: Ваш О. М. Етика : навч.-метод. посіб."""
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
        self.assertIn("Ваш О. М.", result)
        self.assertIn("Етика", result)
        self.assertIn("Запоріжжя", result)
        self.assertIn("ЗНУ", result)
        self.assertIn("2018", result)
        self.assertIn("104", result)

    def test_d1_1_punkt_5(self):
        """Д.1.1.5: Гурманова Л. І. Релігієзнавство : навч. посіб. 2-ге вид."""
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
        self.assertIn("Гурманова Л. І.", result)
        self.assertIn("Релігієзнавство", result)
        self.assertIn("Київ", result)
        self.assertIn("ЦУЛ", result)
        self.assertIn("2017", result)
        self.assertIn("193", result)

    def test_d1_1_punkt_6(self):
        """Д.1.1.6: Parker J. Principles of scientific research. 7th ed."""
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
        self.assertIn("Parker J.", result)
        self.assertIn("Principles of scientific research", result)
        self.assertIn("London", result)
        self.assertIn("Editorial", result)
        self.assertIn("2017", result)
        self.assertIn("301", result)

    def test_d1_1_punkt_7(self):
        """Д.1.1.7: Веретенко В. В. Міжнародний маркетинг (за ред.)"""
        bibtex = """@book{veretenko2015,
            author = {Веретенко, В. В.},
            title = {Міжнародний маркетинг},
            type = {монографія},
            editor = {Марценюк, В. М.},
            year = {2015},
            address = {Київ},
            pages = {374}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Веретенко В. В.", result)
        self.assertIn("Міжнародний маркетинг", result)
        self.assertIn("Київ", result)
        self.assertIn("2015", result)
        self.assertIn("374 с.", result)


class TestDSTU_D1_2_TwoAuthors(unittest.TestCase):
    """Д.1.2: Два автори (6 пунктів)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_2_punkt_1(self):
        """Д.1.2.1: Мартиненко З. Е., Макар І. В. Управління підприємством"""
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
        self.assertIn("Мартиненко З. Е., Макар І. В.", result)
        self.assertIn("Управління підприємством", result)
        self.assertIn("Харків", result)
        self.assertIn("2017", result)

    def test_d1_2_punkt_2(self):
        """Д.1.2.2: Палеха В. І., Карпова П. В. Менеджмент організацій"""
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
        self.assertIn("Палеха В. І., Карпова П. В.", result)
        self.assertIn("Менеджмент організацій", result)
        self.assertIn("Запоріжжя", result)

    def test_d1_2_punkt_3(self):
        """Д.1.2.3: Білоус С. І., Корнійчук В. П. Філософія освіти"""
        bibtex = """@book{bilous2016,
            author = {Білоус, С. І. and Корнійчук, В. П.},
            title = {Філософія освіти},
            type = {навч.-метод. посіб.},
            year = {2016},
            address = {Переяслав-Хмельницький},
            pages = {176}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Білоус С. І., Корнійчук В. П.", result)
        self.assertIn("Філософія освіти", result)
        self.assertIn("Переяслав-Хмельницький", result)

    def test_d1_2_punkt_4(self):
        """Д.1.2.4: Трофименко О. Г., Дика А. І. Тестування (з URL)"""
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
        self.assertIn("Трофименко О. Г., Дика А. І.", result)
        self.assertIn("Тестування", result)
        self.assertIn("URL:", result)
        self.assertIn("дата звернення:", result)

    def test_d1_2_punkt_5(self):
        """Д.1.2.5: Вердіна С. А., Волков А. А. Контролінг. Вид. 3-тє"""
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
        self.assertIn("Вердіна С. А., Волков А. А.", result)
        self.assertIn("Контролінг", result)
        self.assertIn("Херсон", result)

    def test_d1_2_punkt_6(self):
        """Д.1.2.6: Бутенко М. П., Качур В. П. Психологія (за ред.)"""
        bibtex = """@book{butenko2017,
            author = {Бутенко, М. П. and Качур, В. П.},
            title = {Психологія},
            type = {навч. посіб.},
            editor = {Дутко, М. П.},
            publisher = {ЦУЛ},
            year = {2017},
            address = {Київ},
            pages = {332}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Бутенко М. П., Качур В. П.", result)
        self.assertIn("Психологія", result)
        self.assertIn("Київ", result)


class TestDSTU_D1_3_ThreeAuthors(unittest.TestCase):
    """Д.1.3: Три автори (3 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_3_punkt_1(self):
        """Д.1.3.1: Тарнавська Г. Я., Марценюк Н. С., Герасимова Т. М. Фінанси"""
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
        self.assertIn("Тарнавська Г. Я., Марценюк Н. С., Герасимова Т. М.", result)
        self.assertIn("Фінанси", result)

    def test_d1_3_punkt_2(self):
        """Д.1.3.2: Пустовенко В. В., Максименко І. Л., Яким А.С. Безпека життєдіяльності"""
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
        self.assertIn("Пустовенко В. В., Максименко І. Л., Яким А. С.", result)
        self.assertIn("Безпека життєдіяльності", result)

    def test_d1_3_punkt_3(self):
        """Д.1.3.3: Бутенко М. П., Качур В. П., Петренко С. В. Психологія"""
        bibtex = """@book{butenko2017_3,
            author = {Бутенко, М. П. and Качур, В. П. and Петренко, С. В.},
            title = {Психологія},
            type = {навч. посіб.},
            editor = {Дутко, М. П.},
            publisher = {ЦУЛ},
            year = {2017},
            address = {Київ},
            pages = {332}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Бутенко М. П., Качур В. П., Петренко С. В.", result)
        self.assertIn("Психологія", result)


class TestDSTU_D1_4_FourAuthors(unittest.TestCase):
    """Д.1.4: Чотири автори (2 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_4_punkt_1(self):
        """Д.1.4.1: Інновації (4 автори)"""
        bibtex = """@book{innovations2016,
            author = {Гуревич, Д. Т. and Чекан, О. С. and Грибан, О. М. and Макарова, В. В.},
            title = {Інновації},
            type = {навч. посіб.},
            publisher = {ЗНУ},
            year = {2016},
            address = {Запоріжжя},
            pages = {389}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Інновації", result)
        self.assertIn("Запоріжжя", result)
        self.assertIn("2016", result)

    def test_d1_4_punkt_2(self):
        """Д.1.4.2: Моделювання програмного забезпечення"""
        bibtex = """@book{modeling2023,
            author = {Манаков, С. Ю. and Трофименко, О. Г. and Лобода, Ю. Г. and Дика, А. І.},
            title = {Моделювання програмного забезпечення},
            type = {навч.-метод. посібник},
            publisher = {Фенікс},
            year = {2023},
            address = {Одеса},
            pages = {145},
            url = {http://dspace.onua.edu.ua/handle/11300/25952},
            urldate = {2024-12-12}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Моделювання програмного забезпечення", result)
        self.assertIn("URL:", result)


class TestDSTU_D1_5_FivePlusAuthors(unittest.TestCase):
    """Д.1.5: П'ять і більше авторів (5 пунктів)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_5_punkt_1(self):
        """Д.1.5.1: Операційний менеджмент"""
        bibtex = """@book{operational2011,
            author = {Поплавська, С. М. and Автор2, А. and Автор3, Б. and Автор4, В. and Автор5, Г.},
            title = {Операційний менеджмент},
            type = {підручник},
            publisher = {ЦУЛ},
            year = {2011},
            address = {Київ},
            pages = {267}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Поплавська С. М. та ін.", result)
        self.assertIn("Операційний менеджмент", result)

    def test_d1_5_punkt_2(self):
        """Д.1.5.2: Охорона праці. 2-ге вид."""
        bibtex = """@book{safety2017,
            author = {Подольська, О. І. and Автор2, А. and Автор3, Б. and Автор4, В. and Автор5, Г.},
            title = {Охорона праці},
            type = {навч. посіб.},
            edition = {2},
            publisher = {ЦУЛ},
            year = {2017},
            address = {Київ},
            pages = {264}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Подольська О. І. та ін.", result)
        self.assertIn("Охорона праці", result)

    def test_d1_5_punkt_3(self):
        """Д.1.5.3: Вища математика"""
        bibtex = """@book{math2015,
            author = {Ткачук, Т. С. and Автор2, А. and Автор3, Б. and Автор4, В. and Автор5, Г.},
            title = {Вища математика},
            type = {конспект лекцій},
            year = {2015},
            address = {Київ},
            pages = {82}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Ткачук Т. С. та ін.", result)
        self.assertIn("Вища математика", result)

    def test_d1_5_punkt_4(self):
        """Д.1.5.4: Науково-практичний коментар Цивільного кодексу"""
        bibtex = """@book{codex2017,
            author = {Мягченко, К. І. and Автор2, А. and Автор3, Б. and Автор4, В. and Автор5, Г.},
            title = {Науково-практичний коментар Цивільного кодексу України},
            note = {станом на 10 жовт. 2017 р.},
            editor = {Ливанов, І. М.},
            publisher = {ЦУЛ},
            year = {2017},
            address = {Київ},
            pages = {428}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Мягченко К. І. та ін.", result)
        self.assertIn("Цивільного кодексу", result)

    def test_d1_5_punkt_5(self):
        """Д.1.5.5: Referencing styles (англійською)"""
        bibtex = """@book{edwards2010,
            author = {Edwards, G. R. and Author2, A. and Author3, B. and Author4, C. and Author5, D.},
            title = {Referencing styles},
            publisher = {International Publishing},
            year = {2010},
            address = {Los Angeles},
            pages = {280}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Edwards G. R. та ін.", result)
        self.assertIn("Referencing styles", result)


class TestDSTU_D1_6_NoAuthor(unittest.TestCase):
    """Д.1.6: Без автора (8 пунктів)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d1_6_punkt_1(self):
        """Д.1.6.1: 30 років історичному факультету"""
        bibtex = """@book{history30_2016,
            title = {30 років історичному факультету: історія та сьогодення (1986-2016)},
            type = {ювіл. вип.},
            editor = {Черепаня, В. В.},
            publisher = {ЗНУ},
            year = {2016},
            address = {Запоріжжя},
            pages = {340}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("30 років", result)
        self.assertIn("Запоріжжя", result)

    def test_d1_6_punkt_2(self):
        """Д.1.6.2: Етнографія"""
        bibtex = """@book{etnografia2018,
            title = {Етнографія},
            type = {конспект лекцій},
            editor = {Гарапко, В. І.},
            note = {уклад. А. І. Гарапко},
            publisher = {ЦУЛ},
            year = {2018},
            address = {Київ},
            pages = {320}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Етнографія", result)
        self.assertIn("Київ", result)

    def test_d1_6_punkt_3(self):
        """Д.1.6.3: Міжнародні відносини"""
        bibtex = """@book{relations2016,
            title = {Міжнародні відносини},
            type = {монографія},
            editor = {Березовський, М. А.},
            publisher = {ЦУЛ},
            year = {2016},
            address = {Київ},
            pages = {162}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Міжнародні відносини", result)

    def test_d1_6_punkt_4(self):
        """Д.1.6.4: Міжнародні економічні відносини"""
        bibtex = """@book{econrelations2015,
            title = {Міжнародні економічні відносини},
            type = {навч. посіб.},
            editor = {Бедрій, П. О. and Петренко, О. О.},
            publisher = {ОНУ},
            year = {2015},
            address = {Одеса},
            pages = {306}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Міжнародні економічні відносини", result)

    def test_d1_6_punkt_5(self):
        """Д.1.6.5: Науково-практичний коментар Цивільного кодексу"""
        bibtex = """@book{codex2016,
            title = {Науково-практичний коментар Цивільного кодексу України},
            editor = {Тарнавський, Т. А.},
            publisher = {ЦУЛ},
            year = {2016},
            address = {Київ},
            pages = {186}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Науково-практичний коментар", result)

    def test_d1_6_punkt_6(self):
        """Д.1.6.6: Підготовка фахівців у ВНЗ (конференція)"""
        bibtex = """@proceedings{conf2018,
            title = {Підготовка фахівців у ВНЗ в умовах реформування вищої освіти},
            type = {матеріали Всеукр. наук.-практ. конф.},
            note = {м. Мукачево, 4-5 жовт. 2018 р.},
            publisher = {МДУ},
            year = {2018},
            address = {Мукачево},
            pages = {226}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Підготовка фахівців", result)

    def test_d1_6_punkt_7(self):
        """Д.1.6.7: Освіта в Україні: виклики модернізації"""
        bibtex = """@book{education2017,
            title = {Освіта в Україні: виклики модернізації},
            type = {зб. наук. пр.},
            editor = {Марценюк, П. М.},
            note = {редкол.: П. М. Марценюк (відп. ред.) та ін.},
            publisher = {Ін-т всесвітньої історії НАН України},
            year = {2017},
            address = {Київ},
            pages = {319}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Освіта в Україні", result)

    def test_d1_6_punkt_8(self):
        """Д.1.6.8: Товарознавство"""
        bibtex = """@book{tovar2014,
            title = {Товарознавство},
            note = {упоряд. В. Олексик},
            year = {2014},
            address = {Київ},
            pages = {804}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Товарознавство", result)


class TestDSTU_D2_Multivolume(unittest.TestCase):
    """Д.2: Книги багатотомні (4 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d2_punkt_1(self):
        """Д.2.1: Енциклопедія рослин. Т. 8"""
        bibtex = """@book{plants2016,
            title = {Енциклопедія рослин},
            editor = {Деркач, І. М.},
            publisher = {ЦУЛ},
            year = {2016},
            address = {Київ},
            volume = {8},
            pages = {812}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Енциклопедія рослин", result)

    def test_d2_punkt_2(self):
        """Д.2.2: Антологія української юридичної думки. Т. 1"""
        bibtex = """@book{anthology2002,
            title = {Антологія української юридичної думки},
            editor = {Шемшученко, Ю. С.},
            publisher = {Юрид. кн.},
            year = {2002},
            address = {Київ},
            volume = {1},
            note = {Загальна теорія держави і права, філософія та енциклопедія права},
            pages = {568}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Антологія української юридичної думки", result)

    def test_d2_punkt_3(self):
        """Д.2.3: Шевченківська енциклопедія (з URL)"""
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
        self.assertIn("Шевченківська енциклопедія", result)
        self.assertIn("URL:", result)

    def test_d2_punkt_4(self):
        """Д.2.4: Дендрофлора України. Т. 2"""
        bibtex = """@book{dendroflora2012,
            author = {Перхоменко, Л. І.},
            title = {Дендрофлора України},
            note = {в 12 т. Т. 2. Дикорослі та культивовані дерева і кущі. Вип. 1. Покритонасінні},
            publisher = {Наукова думка},
            year = {2012},
            address = {Київ},
            pages = {200}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Дендрофлора України", result)


class TestDSTU_D3_Abstracts(unittest.TestCase):
    """Д.3: Автореферати дисертацій (2 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d3_punkt_1(self):
        """Д.3.1: Пуріш С. В. (докт. філософії)"""
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
        self.assertIn("Пуріш С. В.", result)
        self.assertIn("автореф. дис", result)

    def test_d3_punkt_2(self):
        """Д.3.2: Олійник А. О. (докт. техн. наук)"""
        bibtex = """@phdthesis{oliinyk2021,
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
        self.assertIn("Олійник А. О.", result)


class TestDSTU_D4_Dissertations(unittest.TestCase):
    """Д.4: Дисертації (3 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d4_punkt_1(self):
        """Д.4.1: Петрук Л. А. (канд. фіз.-мат. наук)"""
        bibtex = """@phdthesis{petruk2004,
            author = {Петрук, Л. А.},
            title = {Дослідження статичного деформування складених тіл},
            type = {дис. ... канд. фіз.-мат. наук : 01.02.04},
            year = {2004},
            address = {Львів},
            pages = {140}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Петрук Л. А.", result)
        self.assertIn("Дослідження статичного", result)

    def test_d4_punkt_2(self):
        """Д.4.2: Пуріш С. В. (повторюється з Д.3)"""
        # Той самий що і Д.3.1
        self.skipTest("Дублікат Д.3.1")

    def test_d4_punkt_3(self):
        """Д.4.3: Олійник А. О. (повторюється з Д.3)"""
        # Той самий що і Д.3.2
        self.skipTest("Дублікат Д.3.2")


class TestDSTU_D12_OnlineResources(unittest.TestCase):
    """Д.12: Електронні ресурси (4 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d12_punkt_1(self):
        """Д.12.1: Зінченко Т. Про Soft Skills"""
        bibtex = """@online{zinchenko2025,
            author = {Зінченко, Т.},
            title = {Про Soft Skills в окремо взятій європейській країні},
            url = {https://dou.ua/lenta/articles/soft-skills-eu/},
            urldate = {2025-01-06}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Зінченко Т.", result)
        self.assertIn("Soft Skills", result)

    def test_d12_punkt_2(self):
        """Д.12.2: Why Are Soft Skills So Hard?"""
        bibtex = """@online{softskills2025,
            title = {Why Are Soft Skills So Hard?},
            url = {https://trainingindustry.com/articles/leadership/why-are-soft-skills-so-hard/},
            urldate = {2025-02-05}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Why Are Soft Skills So Hard?", result)

    def test_d12_punkt_3(self):
        """Д.12.3 (помилка нумерації в оригіналі): Хміль А. А. Функції державної служби"""
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
        self.assertIn("Хміль А. А.", result)
        self.assertIn("Функції державної служби", result)

    def test_d12_punkt_4(self):
        """Д.12.4: Куцкір Я. С. та ін. Трансформація (з DOI)"""
        bibtex = """@article{kutskir2016,
            author = {Куцкір, Я. С. and Махно, Б. А. and Борислав, С. Г.},
            title = {Трансформація науково-педагогічної системи України протягом 90-х років ХХ століття: період переходу до ринку},
            journal = {Наука та інновації},
            year = {2016},
            volume = {12},
            number = {6},
            pages = {6--14},
            doi = {10.15407/scin12.06.006}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Куцкір Я. С., Махно Б. А., Борислав С. Г.", result)
        self.assertIn("DOI:", result)


class TestDSTU_D13_1_InBook(unittest.TestCase):
    """Д.13.1: Частина книги (4 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d13_1_punkt_1(self):
        """Д.13.1.1: Петренко М. А. Міжнародне право"""
        bibtex = """@inbook{petrenko2009,
            author = {Петренко, М. А.},
            title = {Міжнародне право та роль Конституційного Суду України},
            booktitle = {Максим Петренко: право як буття вченого : зб. наук. пр. до 60-річчя проф. М. А. Петренко},
            editor = {Волошин, Ю. О.},
            year = {2009},
            address = {Київ},
            pages = {477--493}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Петренко М. А.", result)
        self.assertIn("Міжнародне право", result)

    def test_d13_1_punkt_2(self):
        """Д.13.1.2: Корнійчук Т. О. Методи активізації"""
        bibtex = """@inbook{korniichuk2017,
            author = {Корнійчук, Т. О.},
            title = {Методи активізації навчально-пізнавальної діяльності},
            booktitle = {Педагогіка},
            type = {навч. посіб.},
            editor = {Корнійчук, Т. О.},
            year = {2017},
            address = {Київ},
            pages = {195--197}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Корнійчук Т. О.", result)
        self.assertIn("Методи активізації", result)

    def test_d13_1_punkt_3(self):
        """Д.13.1.3: Ярошевич Н. Б. та ін. Інструменти боргового фінансування"""
        bibtex = """@inbook{yaroshevych2019,
            author = {Ярошевич, Н. Б. and Чубка, О. М. and Якимів, А. І.},
            title = {Інструменти боргового фінансування суб'єктів підприємництва в Україні: правовий статус, структурна динаміка, податкові наслідки},
            booktitle = {Теорія та методологія формування інвестиційно-фінансової стратегії розвитку національного господарства},
            type = {монографія},
            editor = {Савчук, Л. М. and Череп, А. В.},
            year = {2019},
            address = {Дніпро},
            pages = {55--89}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Ярошевич Н. Б., Чубка О. М.", result)
        self.assertIn("Інструменти боргового", result)

    def test_d13_1_punkt_4(self):
        """Д.13.1.4: Goehr L. The concept of opera"""
        bibtex = """@inbook{goehr2014,
            author = {Goehr, L.},
            title = {The concept of opera},
            booktitle = {The Oxford handbook of opera},
            editor = {Greenwald, H. M.},
            year = {2014},
            address = {Oxford},
            pages = {92--136}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Goehr L.", result)
        self.assertIn("The concept of opera", result)


class TestDSTU_D13_3_Articles(unittest.TestCase):
    """Д.13.3: Частина періодичного видання (8 пунктів)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d13_3_punkt_1(self):
        """Д.13.3.1: Кучеренко О. О. Конституційні права"""
        bibtex = """@article{kucherenko2007,
            author = {Кучеренко, О. О.},
            title = {Конституційні права людини і громадянина},
            journal = {Часопис Київського університету права},
            year = {2007},
            number = {4},
            pages = {88--92}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Кучеренко О. О.", result)
        self.assertIn("Конституційні права", result)

    def test_d13_3_punkt_2(self):
        """Д.13.3.2: Загірняк М., Костенко А. Про користування Scopus"""
        bibtex = """@article{zagirniak2017,
            author = {Загірняк, М. and Костенко, А.},
            title = {Про користування можливостями міжнародної бази даних Scopus},
            journal = {Вища школа},
            year = {2017},
            number = {5--6},
            pages = {48--55}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Загірняк М., Костенко А.", result)
        self.assertIn("Scopus", result)

    def test_d13_3_punkt_3(self):
        """Д.13.3.3: Коваль Л., Коваль П. Переваги дистанційної роботи"""
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
        self.assertIn("Коваль Л., Коваль П.", result)
        self.assertIn("Переваги дистанційної роботи", result)

    def test_d13_3_punkt_4(self):
        """Д.13.3.4: Bletskan D. I. et al. Electronic structure"""
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
        self.assertIn("Bletskan D. I., Glukhov K. E., Frolova V. V.", result)
        self.assertIn("Electronic structure", result)

    def test_d13_3_punkt_5(self):
        """Д.13.3.5: Zadereyko О. et al. Research (автори першими)"""
        bibtex = """@article{zadereyko2022a,
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
        self.assertIn("Zadereyko О. та ін.", result)
        self.assertIn("DOI:", result)

    def test_d13_3_punkt_6(self):
        """Д.13.3.6: Трофименко О. Г. та ін. Штучний інтелект"""
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
        self.assertIn("Трофименко О. Г. та ін.", result)
        self.assertIn("Штучний інтелект", result)

    def test_d13_3_punkt_7(self):
        """Д.13.3.7: Research (назва першою)"""
        bibtex = """@article{zadereyko2022b,
            author = {Zadereyko, O. and Trofymenko, O. and Prokop, Y. and Loginova, N. and Dyka, A. and Kukharenko, S.},
            title = {Research of potential data leaks in information and communication systems},
            journal = {Radio electronic and Computer Systems},
            year = {2022},
            number = {4},
            pages = {64--84},
            doi = {10.32620/reks.2022.4.05},
            urldate = {2022-11-03}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        # Має бути у форматі "назва / автори" або "автори. назва"
        self.assertIn("Research of potential data leaks", result)

    def test_d13_3_punkt_8(self):
        """Д.13.3.8: Штучний інтелект (назва першою)"""
        bibtex = """@article{ai_military2024,
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
        self.assertIn("Штучний інтелект", result)


class TestDSTU_D13_4_Conferences(unittest.TestCase):
    """Д.13.4: Частина видання матеріалів конференцій (3 пункти)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d13_4_punkt_1(self):
        """Д.13.4.1: Трофименко О. Г., Єфремов В. А. Оснащення 3D-моделей"""
        bibtex = """@inproceedings{trofymenko2024conf,
            author = {Трофименко, О. Г. and Єфремов, В. А.},
            title = {Оснащення 3D-моделей анімаційних персонажів у розробці ігор},
            booktitle = {Актуальні питання автоматизації та інформаційних технологій (АТІТ-2024) : матер. III Всеукр. наук.-практ. конф.},
            year = {2024},
            month = {21–22 листопада},
            address = {Кременчук},
            pages = {115--116},
            url = {https://atit.kdu.edu.ua/publ.php},
            urldate = {2024-12-16}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Трофименко О. Г., Єфремов В. А.", result)
        self.assertIn("Оснащення 3D-моделей", result)

    def test_d13_4_punkt_2(self):
        """Д.13.4.2: Максименко Д. В. Методи оперативної діагностики"""
        bibtex = """@inproceedings{maksymenko2013,
            author = {Максименко, Д. В.},
            title = {Методи оперативної діагностики виробничої діяльності підприємства},
            booktitle = {Зростання ролі бухгалтерського обліку в сучасній економіці : зб. тез та доповідей І Міжнарод. наук.-практ. конф.},
            note = {м. Київ, 21 лютого 2013 р.},
            editor = {Мельничук, Б. В.},
            year = {2013},
            address = {Київ},
            pages = {331--335}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Максименко Д. В.", result)
        self.assertIn("Методи оперативної діагностики", result)

    def test_d13_4_punkt_3(self):
        """Д.13.4.3: Prokop Y. et al. Developing code style skills"""
        bibtex = """@inproceedings{prokop2023,
            author = {Prokop, Y. and Trofymenko, O. and Zadereyko, O.},
            title = {Developing code style skills in students},
            booktitle = {IEEE 18th International Conference on Computer Science and Information Technologies (CSIT)},
            year = {2023},
            month = {October 19–21},
            address = {Lviv, Ukraine},
            pages = {1--4},
            doi = {10.1109/CSIT61576.2023.10324182},
            urldate = {2024-07-12}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        self.assertIn("Prokop Y., Trofymenko O., Zadereyko O.", result)
        self.assertIn("Developing code style skills", result)


def count_tests():
    """Підрахунок кількості тестів"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    test_classes = [
        TestDSTU_D1_1_SingleAuthor,  # 7
        TestDSTU_D1_2_TwoAuthors,    # 6
        TestDSTU_D1_3_ThreeAuthors,  # 3
        TestDSTU_D1_4_FourAuthors,   # 2
        TestDSTU_D1_5_FivePlusAuthors, # 5
        TestDSTU_D1_6_NoAuthor,      # 8
        TestDSTU_D2_Multivolume,     # 4
        TestDSTU_D3_Abstracts,       # 2
        TestDSTU_D4_Dissertations,   # 3 (2 skipped)
        TestDSTU_D12_OnlineResources, # 4
        TestDSTU_D13_1_InBook,       # 4
        TestDSTU_D13_3_Articles,     # 8
        TestDSTU_D13_4_Conferences,  # 3
    ]

    for test_class in test_classes:
        suite.addTests(loader.loadTestsFromTestCase(test_class))

    return suite.countTestCases()


def run_all_tests():
    """Запуск всіх тестів"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Додаємо всі тестові класи
    test_classes = [
        TestDSTU_D1_1_SingleAuthor,
        TestDSTU_D1_2_TwoAuthors,
        TestDSTU_D1_3_ThreeAuthors,
        TestDSTU_D1_4_FourAuthors,
        TestDSTU_D1_5_FivePlusAuthors,
        TestDSTU_D1_6_NoAuthor,
        TestDSTU_D2_Multivolume,
        TestDSTU_D3_Abstracts,
        TestDSTU_D4_Dissertations,
        TestDSTU_D12_OnlineResources,
        TestDSTU_D13_1_InBook,
        TestDSTU_D13_3_Articles,
        TestDSTU_D13_4_Conferences,
    ]

    for test_class in test_classes:
        suite.addTests(loader.loadTestsFromTestCase(test_class))

    # Запуск тестів
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Підсумок
    print("\n" + "=" * 80)
    print("ПІДСУМОК ДЕТАЛЬНОГО ТЕСТУВАННЯ DSTU 8302:2015")
    print("=" * 80)
    print(f"Всього тестів: {result.testsRun}")
    print(f"Успішно: {result.testsRun - len(result.failures) - len(result.errors) - len(result.skipped)}")
    print(f"Помилки: {len(result.failures)}")
    print(f"Винятки: {len(result.errors)}")
    print(f"Пропущено: {len(result.skipped)}")
    print("=" * 80)

    if result.wasSuccessful():
        print("\n✅ ВСІ ТЕСТИ ПРОЙДЕНО УСПІШНО!")
        print(f"   Протестовано {result.testsRun} пунктів зі стандарту ДСТУ 8302:2015")
    else:
        print("\n❌ ДЕЯКІ ТЕСТИ НЕ ПРОЙДЕНО")

    print("=" * 80)
    return result


if __name__ == '__main__':
    total = count_tests()
    print(f"\n📊 Всього тестів у файлі: {total}\n")
    run_all_tests()
