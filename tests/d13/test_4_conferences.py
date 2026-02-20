import unittest
from bibliographycite import BibTeXToDSTUConverter


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
            editortype = {відпов. за вип.},
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
