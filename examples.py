"""
Расширенные примеры использования BibTeX to DSTU 8302:2015 конвертера
"""

from bibtex_to_dstu import BibTeXToDSTUConverter


def example_book():
    """Пример конвертации книги"""
    print("=" * 80)
    print("ПРИМЕР 1: Книга с одним автором")
    print("=" * 80)

    converter = BibTeXToDSTUConverter()

    bibtex = """
    @book{dychkivska2018,
        author = {Дичківська, О. О.},
        title = {Інноваційний менеджмент},
        subtitle = {конспект лекцій},
        publisher = {ДІА},
        year = {2018},
        address = {Київ},
        pages = {82}
    }
    """

    result = converter.convert_string_to_list(bibtex)
    print("Результат:")
    print(result[0])
    print()


def example_article():
    """Пример конвертации статьи"""
    print("=" * 80)
    print("ПРИМЕР 2: Статья в журнале с URL")
    print("=" * 80)

    converter = BibTeXToDSTUConverter()

    bibtex = """
    @article{khmil2017,
        author = {Хміль, А. А.},
        title = {Функції державної служби за законодавством України},
        journal = {Юридичний науковий електронний журнал},
        year = {2017},
        number = {5},
        pages = {115--118},
        url = {http://lsej.org.ua/5_2017/32.pdf},
        urldate = {2022-12-04}
    }
    """

    result = converter.convert_string_to_list(bibtex)
    print("Результат:")
    print(result[0])
    print()


def example_conference():
    """Пример конвертации материалов конференции"""
    print("=" * 80)
    print("ПРИМЕР 3: Материалы конференции")
    print("=" * 80)

    converter = BibTeXToDSTUConverter()

    bibtex = """
    @inproceedings{trofymenko2024,
        author = {Трофименко, О. Г. and Єфремов, В. А.},
        title = {Оснащення 3D-моделей анімаційних персонажів у розробці ігор},
        booktitle = {Актуальні питання автоматизації та інформаційних технологій (АТІТ-2024) : матер. III Всеукр. наук.-практ. конф.},
        year = {2024},
        month = {21–22 листопада},
        address = {Кременчук},
        pages = {115--116},
        url = {https://atit.kdu.edu.ua/publ.php},
        urldate = {2024-12-16}
    }
    """

    result = converter.convert_string_to_list(bibtex)
    print("Результат:")
    print(result[0])
    print()


def example_thesis():
    """Пример конвертации диссертации"""
    print("=" * 80)
    print("ПРИМЕР 4: Диссертация (автореферат)")
    print("=" * 80)

    converter = BibTeXToDSTUConverter()

    bibtex = """
    @phdthesis{purish2024,
        author = {Пуріш, С. В.},
        title = {Методи машинного навчання для розпізнавання людини за ходою},
        type = {автореф. дис… докт. філософії},
        school = {Національний університет «Одеська політехніка»},
        year = {2024},
        address = {Одеса},
        pages = {21},
        url = {https://op.edu.ua/sites/default/files/publicFiles/dissphd/anotaciya_purish.pdf},
        urldate = {2024-12-20}
    }
    """

    result = converter.convert_string_to_list(bibtex)
    print("Результат:")
    print(result[0])
    print()


def example_online():
    """Пример конвертации электронного ресурса"""
    print("=" * 80)
    print("ПРИМЕР 5: Электронный ресурс")
    print("=" * 80)

    converter = BibTeXToDSTUConverter()

    bibtex = """
    @online{zinchenko2025,
        author = {Зінченко, Т.},
        title = {Про Soft Skills в окремо взятій європейській країні},
        url = {https://dou.ua/lenta/articles/soft-skills-eu/},
        urldate = {2025-01-06}
    }
    """

    result = converter.convert_string_to_list(bibtex)
    print("Результат:")
    print(result[0])
    print()


def example_multiple_authors():
    """Пример с разным количеством авторов"""
    print("=" * 80)
    print("ПРИМЕР 6: Различное количество авторов")
    print("=" * 80)

    converter = BibTeXToDSTUConverter()

    # 2 автора
    bibtex_2 = """
    @book{two_authors,
        author = {Мартиненко, З. Е. and Макар, І. В.},
        title = {Управління підприємством},
        publisher = {Щедра садиба плюс},
        year = {2017},
        address = {Харків}
    }
    """

    # 3 автора
    bibtex_3 = """
    @book{three_authors,
        author = {Тарнавська, Г. Я. and Марценюк, Н. С. and Герасимова, Т. М.},
        title = {Фінанси},
        publisher = {Магнолія 2006},
        year = {2017},
        address = {Львів}
    }
    """

    # 5+ авторов
    bibtex_many = """
    @article{many_authors,
        author = {Zadereyko, О. and Trofymenko, O. and Prokop, Y. and Loginova, N. and Dyka, A. and Kukharenko, S.},
        title = {Research of potential data leaks in information and communication systems},
        journal = {Radio electronic and Computer Systems},
        year = {2022},
        number = {4},
        pages = {64--84}
    }
    """

    print("2 автора:")
    print(converter.convert_string_to_list(bibtex_2)[0])
    print()

    print("3 автора:")
    print(converter.convert_string_to_list(bibtex_3)[0])
    print()

    print("5+ авторов:")
    print(converter.convert_string_to_list(bibtex_many)[0])
    print()


def example_with_doi():
    """Пример статьи с DOI"""
    print("=" * 80)
    print("ПРИМЕР 7: Статья с DOI")
    print("=" * 80)

    converter = BibTeXToDSTUConverter()

    bibtex = """
    @article{example_doi,
        author = {Smith, J. and Doe, A.},
        title = {Machine Learning Applications},
        journal = {Journal of AI},
        year = {2020},
        volume = {15},
        number = {3},
        pages = {123--145},
        doi = {10.1234/jai.2020.123}
    }
    """

    result = converter.convert_string_to_list(bibtex)
    print("Результат:")
    print(result[0])
    print()


def example_bibliography_list():
    """Пример создания полного списка литературы"""
    print("=" * 80)
    print("ПРИМЕР 8: Полный список литературы")
    print("=" * 80)

    converter = BibTeXToDSTUConverter()

    bibtex = """
    @book{book1,
        author = {Іваненко, О. І.},
        title = {Основи програмування},
        publisher = {Наукова думка},
        year = {2018},
        address = {Київ},
        pages = {245}
    }
    
    @article{article1,
        author = {Петренко, М. П. and Сидоренко, В. В.},
        title = {Нові методи машинного навчання},
        journal = {Вісник науки},
        year = {2020},
        volume = {12},
        number = {3},
        pages = {45--67}
    }
    
    @online{web1,
        author = {Коваленко, А. А.},
        title = {Сучасні технології веб-розробки},
        url = {https://example.com/article},
        urldate = {2024-01-15}
    }
    """

    # С нумерацией
    result = converter.convert_string_to_formatted_string(bibtex, numbered=True)
    print("Список литературы:")
    print(result)
    print()


def example_from_file():
    """Пример работы с файлом"""
    print("=" * 80)
    print("ПРИМЕР 9: Работа с .bib файлом")
    print("=" * 80)

    # Создаём тестовый файл
    test_bib = """
@book{test_book,
    author = {Тестовий, А. Б.},
    title = {Тестова книга},
    publisher = {Тестове видавництво},
    year = {2024},
    address = {Київ},
    pages = {100}
}
"""

    with open('/tmp/test_references.bib', 'w', encoding='utf-8') as f:
        f.write(test_bib)

    converter = BibTeXToDSTUConverter()

    # Конвертация из файла
    result = converter.convert_file_to_list('/tmp/test_references.bib')

    print("Файл: /tmp/test_references.bib")
    print("Результат конвертации:")
    print(result[0])
    print()


if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 15 + "РАСШИРЕННЫЕ ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ" + " " * 30 + "║")
    print("║" + " " * 15 + "BibTeX → DSTU 8302:2015 Converter" + " " * 30 + "║")
    print("╚" + "=" * 78 + "╝")
    print("\n")

    example_book()
    example_article()
    example_conference()
    example_thesis()
    example_online()
    example_multiple_authors()
    example_with_doi()
    example_bibliography_list()
    example_from_file()

    print("=" * 80)
    print("ВСЕ ПРИМЕРЫ ВЫПОЛНЕНЫ УСПЕШНО!")
    print("=" * 80)
