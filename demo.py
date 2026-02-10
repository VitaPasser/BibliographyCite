#!/usr/bin/env python3
"""
Демонстрационный скрипт работы BibTeX → DSTU 8302:2015 конвертера
"""

from bibtex_to_dstu import BibTeXToDSTUConverter


def print_header(title):
    """Выводит красивый заголовок"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")


def demo():
    """Основная демонстрация"""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "КОНВЕРТЕР BIBTEX → DSTU 8302:2015" + " " * 25 + "║")
    print("╚" + "=" * 78 + "╝")

    converter = BibTeXToDSTUConverter()

    # Пример 1: Простая книга
    print_header("ПРИМЕР 1: Книга с одним автором")

    bibtex1 = """@book{example1,
        author = {Дичківська, О. О.},
        title = {Інноваційний менеджмент},
        publisher = {ДІА},
        year = {2018},
        address = {Київ},
        pages = {82}
    }"""

    print("BibTeX:")
    print(bibtex1)
    print("\nДСТУ 8302:2015:")
    print(converter.convert_string_to_list(bibtex1)[0])

    # Пример 2: Статья с URL
    print_header("ПРИМЕР 2: Статья в журнале с URL и датой обращения")

    bibtex2 = """@article{example2,
        author = {Хміль, А. А.},
        title = {Функції державної служби за законодавством України},
        journal = {Юридичний науковий електронний журнал},
        year = {2017},
        number = {5},
        pages = {115--118},
        url = {http://lsej.org.ua/5_2017/32.pdf},
        urldate = {2022-12-04}
    }"""

    print("BibTeX:")
    print(bibtex2)
    print("\nДСТУ 8302:2015:")
    print(converter.convert_string_to_list(bibtex2)[0])

    # Пример 3: Много авторов
    print_header("ПРИМЕР 3: Статья с 6 авторами (5+ → первый + 'та ін.')")

    bibtex3 = """@article{example3,
        author = {Zadereyko, О. and Trofymenko, O. and Prokop, Y. and Loginova, N. and Dyka, A. and Kukharenko, S.},
        title = {Research of potential data leaks in information and communication systems},
        journal = {Radio electronic and Computer Systems},
        year = {2022},
        number = {4},
        pages = {64--84},
        doi = {10.32620/reks.2022.4.05}
    }"""

    print("BibTeX:")
    print(bibtex3)
    print("\nДСТУ 8302:2015:")
    print(converter.convert_string_to_list(bibtex3)[0])

    # Пример 4: Материалы конференции
    print_header("ПРИМЕР 4: Материалы конференции")

    bibtex4 = """@inproceedings{example4,
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

    print("BibTeX:")
    print(bibtex4)
    print("\nДСТУ 8302:2015:")
    print(converter.convert_string_to_list(bibtex4)[0])

    # Пример 5: Электронный ресурс
    print_header("ПРИМЕР 5: Электронный ресурс (веб-сайт)")

    bibtex5 = """@online{example5,
        author = {Зінченко, Т.},
        title = {Про Soft Skills в окремо взятій європейській країні},
        url = {https://dou.ua/lenta/articles/soft-skills-eu/},
        urldate = {2025-01-06}
    }"""

    print("BibTeX:")
    print(bibtex5)
    print("\nДСТУ 8302:2015:")
    print(converter.convert_string_to_list(bibtex5)[0])

    # Пример 6: Полный список литературы
    print_header("ПРИМЕР 6: Полный библиографический список (нумерованный)")

    bibtex_list = """
    @book{ref1,
        author = {Іваненко, О. І.},
        title = {Основи програмування},
        publisher = {Наукова думка},
        year = {2018},
        address = {Київ},
        pages = {245}
    }
    
    @article{ref2,
        author = {Петренко, М. П. and Сидоренко, В. В.},
        title = {Нові методи машинного навчання},
        journal = {Вісник науки},
        year = {2020},
        volume = {12},
        number = {3},
        pages = {45--67}
    }
    
    @online{ref3,
        author = {Коваленко, А. А.},
        title = {Сучасні технології веб-розробки},
        url = {https://example.com/article},
        urldate = {2024-01-15}
    }
    """

    result = converter.convert_string_to_formatted_string(bibtex_list, numbered=True)
    print(result)

    # Финальная статистика
    print("\n")
    print("=" * 80)
    print("  КОНВЕРТЕР ГОТОВ К ИСПОЛЬЗОВАНИЮ!")
    print("=" * 80)
    print("\nПоддерживаемые типы записей:")
    print("  • book, inbook - Книги и части книг")
    print("  • article - Статьи в журналах")
    print("  • inproceedings, conference - Материалы конференций")
    print("  • phdthesis, mastersthesis - Диссертации и авторефераты")
    print("  • online - Электронные ресурсы")
    print("  • techreport - Технические отчёты и стандарты")
    print("  • misc - Прочие типы")
    print("\nОсобенности:")
    print("  ✓ Автоматическое форматирование авторов (1-3, 4, 5+ авторов)")
    print("  ✓ Обработка URL и DOI")
    print("  ✓ Форматирование дат обращения")
    print("  ✓ Очистка от LaTeX команд")
    print("  ✓ Поддержка украинского и русского языков")
    print("\nИспользование:")
    print("  from bibtex_to_dstu import BibTeXToDSTUConverter")
    print("  converter = BibTeXToDSTUConverter()")
    print("  result = converter.convert_file_to_list('references.bib')")
    print("=" * 80)
    print("\n")


if __name__ == "__main__":
    demo()
