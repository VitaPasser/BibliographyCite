import unittest
from bibliographycite import BibTeXToDSTUConverter


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
