import unittest
from bibliographycite import BibTeXToDSTUConverter


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
