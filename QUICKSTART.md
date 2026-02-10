# 🚀 Швидкий старт

Посібник для швидкого початку роботи з BibliographyCite.

## ⚡ За 30 секунд

```bash
# 1. Клонуємо репозиторій
git clone <repository>
cd BibliographyCite

# 2. Встановлюємо залежності
uv sync

# 3. Тестуємо
python -c "from bibliographycite import BibTeXToDSTUConverter; print('✅ Працює!')"
```

## 📝 Перший приклад

Створіть файл `my_first_conversion.py`:

```python
from bibliographycite import BibTeXToDSTUConverter

# Створюємо конвертер
converter = BibTeXToDSTUConverter()

# BibTeX запис
bibtex = """
@book{ivanov2020,
    author = {Іванов, О. І.},
    title = {Програмування на Python},
    publisher = {Наукова думка},
    year = {2020},
    address = {Київ},
    pages = {250}
}
"""

# Конвертуємо
result = converter.convert_string_to_list(bibtex)
print(result[0])
```

**Запуск:**
```bash
python my_first_conversion.py
```

**Результат:**
```
Іванов О. І. Програмування на Python. Київ : Наукова думка, 2020. 250 с.
```

## 📚 Конвертація з файлу

1. Створіть файл `references.bib`:
```bibtex
@book{example2020,
    author = {Петренко, П. П. and Сидоренко, С. С.},
    title = {Основи алгоритмів},
    publisher = {Техніка},
    year = {2020},
    address = {Харків},
    pages = {300}
}

@article{article2021,
    author = {Коваленко, К. К.},
    title = {Нові методи машинного навчання},
    journal = {Вісник науки},
    year = {2021},
    number = {5},
    pages = {10--20}
}
```

2. Створіть `convert_file.py`:
```python
from bibliographycite import BibTeXToDSTUConverter

converter = BibTeXToDSTUConverter()

# Конвертуємо файл
references = converter.convert_file_to_list('references.bib')

# Виводимо
for i, ref in enumerate(references, 1):
    print(f"{i}. {ref}")
```

3. Запустіть:
```bash
python convert_file.py
```

## 🧪 Запуск тестів

```bash
# Всі тести
pytest

# Повне покриття (81 тест)
pytest tests/test_dstu_all_81_points.py -v

# З детальним виводом
pytest -v --tb=short
```

## 📖 Наступні кроки

1. Прочитайте [README.md](../README.md) для повної документації
2. Перегляньте [приклади](../examples/)
3. Вивчіть [звіти про тестування](docs/reports/)
4. Перегляньте [стандарт ДСТУ](docs/DSTU-8302-2015.txt)

## 🆘 Потрібна допомога?

- Дивіться [приклади](../examples/)
- Читайте [документацію](../README.md)
- Створіть [issue](https://github.com/yourusername/bibliographycite/issues)

---

**Готово!** Тепер ви можете конвертувати BibTeX у ДСТУ 8302:2015! 🎉
