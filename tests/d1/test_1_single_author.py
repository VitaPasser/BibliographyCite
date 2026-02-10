import unittest
from bibliographycite import BibTeXToDSTUConverter


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
