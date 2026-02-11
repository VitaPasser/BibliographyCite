"""
Конвертер библиографических записей из формата BibTeX в формат DSTU 8302:2015
Главный модуль для демонстрации работы
"""

from bibliographycite import BibTeXToDSTUConverter


def main():
    """Основная функция для демонстрации работы конвертера"""

    print("=" * 80)
    print("Конвертер BibTeX → DSTU 8302:2015")
    print("=" * 80)
    print()

    converter = BibTeXToDSTUConverter()

    # Примеры различных типов записей
    sample_bibtex = """
    @book{dychkivska2018,
        author = {Дичківська, О. О.},
        title = {Інноваційний менеджмент},
        subtitle = {конспект лекцій},
        publisher = {ДІА},
        year = {2018},
        address = {Київ},
        pages = {82}
    }
    
    @book{ivanov2025,
      author = {Иванов, И. И. and Петров, П. П. and Сидоров, С. С. and Бондаренко, Б. Б.},
      title = {Основы Pandoc},
      type = {конспект лекцій},
      year = {2025},
      publisher = {Наука}
    }
    
    @book{martynenko2017,
        author = {Мартиненко, З. Е. and Макар, І. В.},
        title = {Управління підприємством: теоретико-методичні засади},
        type = {монографія},
        publisher = {Щедра садиба плюс},
        year = {2017},
        address = {Харків},
        pages = {296}
    }
    
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
    
    @online{zinchenko2025,
        author = {Зінченко, Т.},
        title = {Про Soft Skills в окремо взятій європейській країні},
        url = {https://dou.ua/lenta/articles/soft-skills-eu/},
        urldate = {2025-01-06}
    }
    
    @article{zadereyko2022,
        author = {Zadereyko, О. and Trofymenko, O. and Prokop, Y. and Loginova, N. and Dyka, A. and Kukharenko, S.},
        title = {Research of potential data leaks in information and communication systems},
        journal = {Radio electronic and Computer Systems},
        year = {2022},
        number = {4},
        pages = {64--84},
        doi = {10.32620/reks.2022.4.05},
        urldate = {2022-11-03}
    }
    """

    print("ПРИКЛАД КОНВЕРТАЦІЇ:\n")
    print("Вхідні дані (BibTeX):")
    print("-" * 80)
    print(sample_bibtex.strip())
    print("-" * 80)
    print()

    # Конвертуємо в список
    bibliography_list = converter.convert_string_to_list(sample_bibtex)

    print("Результат (ДСТУ 8302:2015):")
    print("-" * 80)
    for i, entry in enumerate(bibliography_list, 1):
        print(f"{i}. {entry}")
        print()
    print("-" * 80)
    print()

    # Також можна отримать как одну строку
    formatted_string = converter.convert_string_to_formatted_string(sample_bibtex, numbered=True)

    print("ІНСТРУКЦІЯ З ВИКОРИСТАННЯ:")
    print("-" * 80)
    print("""
1. Імпортуйте конвертер:
   from bibliographycite import BibTeXToDSTUConverter

2. Створіть екземпляр:
   converter = BibTeXToDSTUConverter()

3. Конвертуйте файл:
   result = converter.convert_file_to_list('references.bib')
   
4. Або конвертуйте строку:
   result = converter.convert_string_to_list(bibtex_string)

5. Отримайте відформатовану строку:
   formatted = converter.convert_file_to_string('references.bib')

Підтримувані типи записів:
- book, inbook (книги та частини книг)
- article (статті в журналах)
- inproceedings, conference (матеріали конференцій)
- phdthesis, mastersthesis (дисертації)
- online (електронні ресурси)
- techreport (технічні звіти та стандарти)
- misc (інші типи)

Конвертер автоматично:
- Форматує авторів згідно правил ДСТУ (Прізвище І. О.)
- Обробляє різну кількість авторів (1-3, 4, 5+)
- Додає правильні розділові знаки
- Форматує URL та дати звернення
- Обробляє DOI
- Очищає текст від LaTeX команд
- Конвертує спеціальні символи
    """)
    print("-" * 80)


if __name__ == '__main__':
    main()

