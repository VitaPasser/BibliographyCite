import unittest
from bibliographycite import BibTeXToDSTUConverter


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
            editortype = {упоряд. та відп. ред.},
            year = {2009},
            address = {Київ},
            pages = {477--493}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Петренко М. А. Міжнародне право та роль Конституційного Суду України. Максим Петренко: право як буття вченого : зб. наук. пр. до 60-річчя проф. М. А. Петренко / упоряд. та відп. ред. Ю. О. Волошин. Київ, 2009. С. 477–493."
        self.assertEqual(result, expected)

    def test_d13_1_punkt_2(self):
        """Д.13.1.2: Корнійчук Т. О."""
        bibtex = """@inbook{korniichuk2017,
            author = {Корнійчук, Т. О.},
            title = {Методи активізації навчально-пізнавальної діяльності},
            booktitle = {Педагогіка : навч. посіб.},
            editor = {Корнійчук, Т. О.},
            editortype = {заг. ред.},
            year = {2017},
            address = {Київ},
            pages = {195--197}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Корнійчук Т. О. Методи активізації навчально-пізнавальної діяльності. Педагогіка : навч. посіб. / заг. ред. Т. О. Корнійчук. Київ, 2017. С. 195–197."
        self.assertEqual(result, expected)

    def test_d13_1_punkt_3(self):
        """Д.13.1.3: Ярошевич Н. Б., Чубка О. М. Якимів А. І."""
        bibtex = """@inbook{yaroshevych2019,
            author = {Ярошевич, Н. Б. and Чубка, О. М. and Якимів, А. І.},
            title = {Інструменти боргового фінансування суб'єктів підприємництва в Україні: правовий статус, структурна динаміка, податкові наслідки},
            booktitle = {Теорія та методологія формування інвестиційно-фінансової стратегії розвитку національного господарства : монографія},
            editor = {Савчук, Л. М. and Череп, А. В.},
            year = {2019},
            address = {Дніпро},
            pages = {55--89}
        }"""
        result = self.converter.convert_string_to_list(bibtex)[0]
        expected = "Ярошевич Н. Б., Чубка О. М., Якимів А. І. Інструменти боргового фінансування суб'єктів підприємництва в Україні: правовий статус, структурна динаміка, податкові наслідки. Теорія та методологія формування інвестиційно-фінансової стратегії розвитку національного господарства : монографія / ред. Л. М. Савчук, А. В. Череп. Дніпро, 2019. С. 55–89."
        self.assertEqual(result, expected)

    def test_d13_1_punkt_4(self):
        """Д.13.1.4: Goehr L."""
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
        expected = "Goehr L. The concept of opera. The Oxford handbook of opera / ed. by H. M. Greenwald. Oxford, 2014. P. 92–136."
        self.assertEqual(result, expected)
