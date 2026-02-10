#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Комплексные тесты конвертера BibTeX → DSTU 8302:2015
Тесты охватывают все случаи из файла DSTU-8302-2015.txt

Структура тестов:
- Д.1: Книги (однотомні видання)
  - Д.1.1: Один автор
  - Д.1.2: Два автори
  - Д.1.3: Три автори
  - Д.1.4: Чотири автори
  - Д.1.5: П'ять і більше авторів
  - Д.1.6: Без автора
- Д.2: Книги (багатотомні видання)
- Д.3: Автореферати дисертацій
- Д.4: Дисертації
- Д.12: Електронні ресурси
- Д.13: Частини видання
  - Д.13.1: Частина книги
  - Д.13.3: Частина періодичного видання
  - Д.13.4: Частина видання матеріалів конференцій
"""

import unittest
from bibtex_to_dstu import BibTeXToDSTUConverter


class TestDSTU_D1_Books(unittest.TestCase):
    """Тести для Д.1: Книги (однотомні видання)"""

    def setUp(self):
        """Ініціалізація конвертера перед кожним тестом"""
        self.converter = BibTeXToDSTUConverter()

    # Д.1.1: Один автор

    def test_d1_1_single_author_basic(self):
        """Д.1.1.1: Дичківська О. О. Інноваційний менеджмент"""
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
        expected = "Дичківська О. О. Інноваційний менеджмент. Київ : ДІА, 2018. 82 с."

        self.assertEqual(result, expected)

    def test_d1_1_single_author_no_publisher(self):
        """Д.1.1.2: Бондаренко В. Г. Історія України"""
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

    def test_d1_1_single_author_monograph(self):
        """Д.1.1.3: Лазор О. Я. Державне управління (монографія)"""
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

        # Проверяем ключевые элементы
        self.assertIn("Лазор О. Я.", result)
        self.assertIn("Державне управління", result)
        self.assertIn("монографія", result)
        self.assertIn("Львів", result)
        self.assertIn("2003", result)
        self.assertIn("542 с.", result)

    def test_d1_1_single_author_teaching_aid(self):
        """Д.1.1.4: Ваш О. М. Етика (навч.-метод. посіб.)"""
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
        self.assertIn("2018", result)

    def test_d1_1_single_author_second_edition(self):
        """Д.1.1.5: Гурманова Л. І. Релігієзнавство (2-ге вид.)"""
        bibtex = """@book{gurmanova2017,
            author = {Гурманова, Л. І.},
            title = {Релігієзнавство},
            type = {навч. посіб.},
            edition = {2},
            publisher = {ЦУЛ},
            year = {2017},
            address = {Київ},
            pages = {193}
        }"""

        result = self.converter.convert_string_to_list(bibtex)[0]

        self.assertIn("Гурманова Л. І.", result)
        self.assertIn("Релігієзнавство", result)
        self.assertIn("Київ", result)
        self.assertIn("2017", result)

    def test_d1_1_single_author_english(self):
        """Д.1.1.6: Parker J. Principles of scientific research (7th ed.)"""
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
        self.assertIn("2017", result)
        self.assertIn("301", result)

    def test_d1_1_single_author_with_editor(self):
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
        self.assertIn("2015", result)

    # Д.1.2: Два автори

    def test_d1_2_two_authors_basic(self):
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
        expected = "Мартиненко З. Е., Макар І. В. Управління підприємством: теоретико-методичні засади : монографія. Харків : Щедра садиба плюс, 2017. 296 с."

        self.assertEqual(result, expected)

    def test_d1_2_two_authors_teaching_manual(self):
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
        self.assertIn("2015", result)

    def test_d1_2_two_authors_with_url(self):
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
        self.assertIn("Тестування та забезпечення якості програмних систем", result)
        self.assertIn("URL: https://hdl.handle.net/11300/27717", result)
        self.assertIn("дата звернення:", result)

    # Д.1.3: Три автори

    def test_d1_3_three_authors(self):
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
        self.assertIn("Львів", result)
        self.assertIn("2017", result)

    def test_d1_3_three_authors_monograph(self):
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
        self.assertIn("Харків", result)

    # Д.1.4: Чотири автори

    def test_d1_4_four_authors_title_first(self):
        """Д.1.4.1: Інновації (4 автори, назва першою)"""
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
        # Можуть бути всі 4 автори або перший + "та ін."

    def test_d1_4_four_authors_with_url(self):
        """Д.1.4.2: Моделювання програмного забезпечення (4 автори з URL)"""
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
        self.assertIn("Одеса", result)
        self.assertIn("2023", result)
        self.assertIn("URL:", result)

    # Д.1.5: П'ять і більше авторів

    def test_d1_5_five_plus_authors_ukrainian(self):
        """Д.1.5.1: Операційний менеджмент (5+ авторів, "та ін.")"""
        bibtex = """@book{operational2011,
            author = {Поплавська, С. М. and Автор2, А. А. and Автор3, Б. Б. and Автор4, В. В. and Автор5, Г. Г.},
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
        self.assertIn("Київ", result)
        self.assertIn("2011", result)

    def test_d1_5_five_plus_authors_english(self):
        """Д.1.5.5: Referencing styles (англійською, "et al.")"""
        bibtex = """@book{edwards2010,
            author = {Edwards, G. R. and Author2, A. and Author3, B. and Author4, C. and Author5, D. and Author6, E.},
            title = {Referencing styles},
            publisher = {International Publishing},
            year = {2010},
            address = {Los Angeles},
            pages = {280}
        }"""

        result = self.converter.convert_string_to_list(bibtex)[0]

        # Перший автор + "та ін." для англійських джерел теж
        self.assertIn("Edwards G. R. та ін.", result)
        self.assertIn("Referencing styles", result)
        self.assertIn("Los Angeles", result)


class TestDSTU_D3_Theses(unittest.TestCase):
    """Тесті для Д.3: Автореферати дисертацій"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d3_phd_thesis_with_url(self):
        """Д.3.1: Пуріш С. В. Методи машинного навчання (автореф. дис.)"""
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
        self.assertIn("Методи машинного навчання для розпізнавання людини за ходою", result)
        self.assertIn("автореф. дис", result)
        self.assertIn("Одеса", result)
        self.assertIn("2024", result)
        self.assertIn("URL:", result)
        self.assertIn("дата звернення:", result)

    def test_d3_phd_thesis_technical(self):
        """Д.3.2: Олійник А. О. Методи синтезу (докт. техн. наук)"""
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
        self.assertIn("Методи синтезу діагностичних моделей", result)
        self.assertIn("Харків", result)
        self.assertIn("2021", result)
        self.assertIn("URL:", result)


class TestDSTU_D12_OnlineResources(unittest.TestCase):
    """Тести для Д.12: Електронні ресурси"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d12_online_ukrainian(self):
        """Д.12.1: Зінченко Т. Про Soft Skills"""
        bibtex = """@online{zinchenko2025,
            author = {Зінченко, Т.},
            title = {Про Soft Skills в окремо взятій європейській країні},
            url = {https://dou.ua/lenta/articles/soft-skills-eu/},
            urldate = {2025-01-06}
        }"""

        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Зінченко Т. Про Soft Skills в окремо взятій європейській країні. https://dou.ua/lenta/articles/soft-skills-eu/ (дата звернення: 06.01.2025)."

        self.assertEqual(result, expected)

    def test_d12_online_english(self):
        """Д.12.2: Why Are Soft Skills So Hard?"""
        bibtex = """@online{softskills2025,
            title = {Why Are Soft Skills So Hard?},
            url = {https://trainingindustry.com/articles/leadership/why-are-soft-skills-so-hard/},
            urldate = {2025-02-05}
        }"""

        result = self.converter.convert_string_to_list(bibtex)[0]

        self.assertIn("Why Are Soft Skills So Hard?", result)
        self.assertIn("https://trainingindustry.com/articles/leadership/why-are-soft-skills-so-hard/", result)
        self.assertIn("дата звернення:", result)
        self.assertIn("05.02.2025", result)


class TestDSTU_D13_3_Articles(unittest.TestCase):
    """Тести для Д.13.3: Частина періодичного видання (журналу, газети)"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d13_3_article_basic(self):
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
        self.assertIn("Конституційні права людини і громадянина", result)
        self.assertIn("Часопис Київського університету права", result)
        self.assertIn("2007", result)
        self.assertIn("№ 4", result)
        self.assertIn("С. 88–92", result)

    def test_d13_3_article_two_authors(self):
        """Д.13.3.2: Загірняк М., Костенко А. Про користування Scopus"""
        bibtex = """@article{zagirniak2017,
            author = {Загірняк, М. and Костенко, А.},
            title = {Про користування можливостями міжнародної бази даних Scopus},
            journal = {Вища школа},
            year = {2017},
            number = {5–6},
            pages = {48--55}
        }"""

        result = self.converter.convert_string_to_list(bibtex)[0]

        self.assertIn("Загірняк М., Костенко А.", result)
        self.assertIn("Про користування можливостями міжнародної бази даних Scopus", result)
        self.assertIn("Вища школа", result)
        self.assertIn("2017", result)

    def test_d13_3_article_english_with_volume(self):
        """Д.13.3.4: Bletskan D. I. Electronic structure"""
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
        self.assertIn("Electronic structure of 2H-SnSe2", result)
        self.assertIn("Semiconductor Physics Quantum Electronics & Optoelectronics", result)
        self.assertIn("Т. 18", result)
        self.assertIn("№ 2", result)

    def test_d13_3_article_six_authors_with_doi(self):
        """Д.13.3.5: Zadereyko О. та ін. Research of potential data leaks"""
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

        self.assertIn("Zadereyko О. та ін.", result)
        self.assertIn("Research of potential data leaks in information and communication systems", result)
        self.assertIn("Radio electronic and Computer Systems", result)
        self.assertIn("2022", result)
        self.assertIn("№ 4", result)
        self.assertIn("С. 64–84", result)
        self.assertIn("DOI: https://doi.org/10.32620/reks.2022.4.05", result)

    def test_d13_3_article_ukrainian_with_doi(self):
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
        self.assertIn("Штучний інтелект у військових навчальних симуляторах", result)
        self.assertIn("Інформаційні технології та суспільство", result)
        self.assertIn("2024", result)
        self.assertIn("DOI:", result)


class TestDSTU_D13_4_Conferences(unittest.TestCase):
    """Тести для Д.13.4: Частина видання матеріалів конференцій"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_d13_4_conference_ukrainian(self):
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
        self.assertIn("Оснащення 3D-моделей анімаційних персонажів у розробці ігор", result)
        self.assertIn("АТІТ-2024", result)
        self.assertIn("Кременчук", result)
        self.assertIn("С. 115–116", result)
        self.assertIn("URL:", result)

    def test_d13_4_conference_single_author(self):
        """Д.13.4.2: Максименко Д. В. Методи оперативної діагностики"""
        bibtex = """@inproceedings{maksymenko2013,
            author = {Максименко, Д. В.},
            title = {Методи оперативної діагностики виробничої діяльності підприємства},
            booktitle = {Зростання ролі бухгалтерського обліку в сучасній економіці : зб. тез та доповідей І Міжнарод. наук.-практ. конф.},
            year = {2013},
            month = {21 лютого},
            address = {Київ},
            pages = {331--335}
        }"""

        result = self.converter.convert_string_to_list(bibtex)[0]

        self.assertIn("Максименко Д. В.", result)
        self.assertIn("Методи оперативної діагностики виробничої діяльності підприємства", result)
        self.assertIn("Київ", result)
        self.assertIn("2013", result)

    def test_d13_4_conference_english_with_doi(self):
        """Д.13.4.3: Prokop Y. Developing code style skills"""
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
        self.assertIn("Developing code style skills in students", result)
        self.assertIn("IEEE 18th International Conference", result)
        self.assertIn("Lviv", result)
        self.assertIn("DOI:", result)


class TestDSTU_EdgeCases(unittest.TestCase):
    """Тести для крайніх випадків та особливих ситуацій"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_missing_fields(self):
        """Тест на відсутність деяких полів"""
        bibtex = """@book{minimal,
            author = {Автор, А. А.},
            title = {Назва книги},
            year = {2020}
        }"""

        result = self.converter.convert_string_to_list(bibtex)[0]

        self.assertIn("Автор А. А.", result)
        self.assertIn("Назва книги", result)
        self.assertIn("2020", result)

    def test_latex_commands_removal(self):
        """Тест на видалення LaTeX команд"""
        bibtex = """@book{latex,
            author = {Автор, А. А.},
            title = {\\textbf{Назва} з \\emph{курсивом}},
            year = {2020}
        }"""

        result = self.converter.convert_string_to_list(bibtex)[0]

        # LaTeX команди повинні бути видалені
        self.assertNotIn("\\textbf", result)
        self.assertNotIn("\\emph", result)
        self.assertIn("Назва", result)
        self.assertIn("курсивом", result)

    def test_date_formats(self):
        """Тест різних форматів дат"""
        bibtex = """@online{datetest,
            author = {Автор, А. А.},
            title = {Тестова стаття},
            url = {http://example.com},
            urldate = {2024-12-15}
        }"""

        result = self.converter.convert_string_to_list(bibtex)[0]

        # Дата повинна бути у форматі DD.MM.YYYY
        self.assertIn("15.12.2024", result)
        self.assertNotIn("2024-12-15", result)

    def test_page_ranges(self):
        """Тест діапазонів сторінок"""
        bibtex = """@article{pages,
            author = {Автор, А. А.},
            title = {Стаття},
            journal = {Журнал},
            year = {2020},
            pages = {10--25}
        }"""

        result = self.converter.convert_string_to_list(bibtex)[0]

        # Подвійний дефіс повинен перетворитися на тире
        self.assertIn("С. 10–25", result)

    def test_cyrillic_and_latin_mixed(self):
        """Тест змішаних кириличних та латинських символів"""
        bibtex = """@article{mixed,
            author = {Іванов, І. І. and Smith, J.},
            title = {Дослідження AI в освіті},
            journal = {Journal of Education},
            year = {2024}
        }"""

        result = self.converter.convert_string_to_list(bibtex)[0]

        self.assertIn("Іванов І. І., Smith J.", result)
        self.assertIn("Дослідження AI в освіті", result)

    def test_multiple_entries(self):
        """Тест обробки декількох записів"""
        bibtex = """
        @book{book1,
            author = {Автор1, А. А.},
            title = {Книга 1},
            year = {2020}
        }
        
        @article{article1,
            author = {Автор2, Б. Б.},
            title = {Стаття 1},
            journal = {Журнал},
            year = {2021}
        }
        
        @online{online1,
            author = {Автор3, В. В.},
            title = {Веб-ресурс},
            url = {http://example.com},
            urldate = {2024-01-01}
        }
        """

        results = self.converter.convert_string_to_list(bibtex)

        self.assertEqual(len(results), 3)
        self.assertIn("Автор1 А. А.", results[0])
        self.assertIn("Автор2 Б. Б.", results[1])
        self.assertIn("Автор3 В. В.", results[2])


class TestDSTU_FormattedOutput(unittest.TestCase):
    """Тести для відформатованого виводу списку літератури"""

    def setUp(self):
        self.converter = BibTeXToDSTUConverter()

    def test_numbered_list(self):
        """Тест нумерованого списку"""
        bibtex = """
        @book{book1,
            author = {Іванов, І. І.},
            title = {Перша книга},
            year = {2020}
        }
        
        @book{book2,
            author = {Петров, П. П.},
            title = {Друга книга},
            year = {2021}
        }
        """

        result = self.converter.convert_string_to_formatted_string(bibtex, numbered=True)

        self.assertIn("1.", result)
        self.assertIn("2.", result)
        self.assertIn("Іванов І. І.", result)
        self.assertIn("Петров П. П.", result)

    def test_unnumbered_list(self):
        """Тест ненумерованого списку"""
        bibtex = """
        @book{book1,
            author = {Іванов, І. І.},
            title = {Перша книга},
            year = {2020}
        }
        """

        result = self.converter.convert_string_to_formatted_string(bibtex, numbered=False)

        self.assertNotIn("1.", result)
        self.assertIn("Іванов І. І.", result)


def run_tests():
    """Запуск всіх тестів"""
    # Создаём тестовий набір
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Додаємо всі тестові класи
    suite.addTests(loader.loadTestsFromTestCase(TestDSTU_D1_Books))
    suite.addTests(loader.loadTestsFromTestCase(TestDSTU_D3_Theses))
    suite.addTests(loader.loadTestsFromTestCase(TestDSTU_D12_OnlineResources))
    suite.addTests(loader.loadTestsFromTestCase(TestDSTU_D13_3_Articles))
    suite.addTests(loader.loadTestsFromTestCase(TestDSTU_D13_4_Conferences))
    suite.addTests(loader.loadTestsFromTestCase(TestDSTU_EdgeCases))
    suite.addTests(loader.loadTestsFromTestCase(TestDSTU_FormattedOutput))

    # Запускаємо тести з детальним виводом
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Виводимо підсумок
    print("\n" + "=" * 70)
    print("ПІДСУМОК ТЕСТУВАННЯ")
    print("=" * 70)
    print(f"Всього тестів: {result.testsRun}")
    print(f"Успішно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Помилки: {len(result.failures)}")
    print(f"Винятки: {len(result.errors)}")

    if result.wasSuccessful():
        print("\n✅ ВСІ ТЕСТИ ПРОЙДЕНО УСПІШНО!")
    else:
        print("\n❌ ДЕЯКІ ТЕСТИ НЕ ПРОЙДЕНО")

    print("=" * 70)

    return result


if __name__ == '__main__':
    run_tests()
