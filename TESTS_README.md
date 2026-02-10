# Документація до тестів DSTU 8302:2015

## Огляд

Файл `test_dstu_comprehensive.py` містить комплексний набір тестів для конвертера BibTeX → DSTU 8302:2015. Тести охоплюють всі основні випадки з файлу `docs/DSTU-8302-2015.txt`.

## Структура тестів

### 1. TestDSTU_D1_Books (18 тестів)
**Д.1: Книги (однотомні видання)**

#### Д.1.1: Один автор (7 тестів)
- `test_d1_1_single_author_basic` - Базова книга з одним автором
- `test_d1_1_single_author_no_publisher` - Без видавництва
- `test_d1_1_single_author_monograph` - Монографія
- `test_d1_1_single_author_teaching_aid` - Навчально-методичний посібник
- `test_d1_1_single_author_second_edition` - Друге видання
- `test_d1_1_single_author_english` - Англійською мовою
- `test_d1_1_single_author_with_editor` - З редактором

#### Д.1.2: Два автори (3 тести)
- `test_d1_2_two_authors_basic` - Базова книга з двома авторами
- `test_d1_2_two_authors_teaching_manual` - Навчальний посібник
- `test_d1_2_two_authors_with_url` - З URL та датою звернення

#### Д.1.3: Три автори (2 тести)
- `test_d1_3_three_authors` - Книга з трьома авторами
- `test_d1_3_three_authors_monograph` - Монографія

#### Д.1.4: Чотири автори (2 тести)
- `test_d1_4_four_authors_title_first` - Назва першою
- `test_d1_4_four_authors_with_url` - З URL

#### Д.1.5: П'ять і більше авторів (2 тести)
- `test_d1_5_five_plus_authors_ukrainian` - Українською ("та ін.")
- `test_d1_5_five_plus_authors_english` - Англійською

### 2. TestDSTU_D3_Theses (2 тести)
**Д.3: Автореферати дисертацій**

- `test_d3_phd_thesis_with_url` - Автореферат докт. філософії з URL
- `test_d3_phd_thesis_technical` - Автореферат докт. техн. наук

### 3. TestDSTU_D12_OnlineResources (2 тести)
**Д.12: Електронні ресурси**

- `test_d12_online_ukrainian` - Українською мовою
- `test_d12_online_english` - Англійською мовою

### 4. TestDSTU_D13_3_Articles (5 тестів)
**Д.13.3: Частина періодичного видання (журналу, газети)**

- `test_d13_3_article_basic` - Базова стаття
- `test_d13_3_article_two_authors` - Два автори
- `test_d13_3_article_english_with_volume` - Англійською з томом
- `test_d13_3_article_six_authors_with_doi` - Шість авторів з DOI
- `test_d13_3_article_ukrainian_with_doi` - Українською з DOI

### 5. TestDSTU_D13_4_Conferences (3 тести)
**Д.13.4: Частина видання матеріалів конференцій**

- `test_d13_4_conference_ukrainian` - Українською мовою
- `test_d13_4_conference_single_author` - Один автор
- `test_d13_4_conference_english_with_doi` - Англійською з DOI

### 6. TestDSTU_EdgeCases (6 тестів)
**Крайні випадки та особливі ситуації**

- `test_missing_fields` - Відсутність деяких полів
- `test_latex_commands_removal` - Видалення LaTeX команд
- `test_date_formats` - Різні формати дат
- `test_page_ranges` - Діапазони сторінок
- `test_cyrillic_and_latin_mixed` - Змішані кириличні та латинські символи
- `test_multiple_entries` - Обробка декількох записів

### 7. TestDSTU_FormattedOutput (2 тести)
**Відформатований вивід**

- `test_numbered_list` - Нумерований список
- `test_unnumbered_list` - Ненумерований список

## Запуск тестів

### Всі тести
```bash
python test_dstu_comprehensive.py
```

або

```bash
uv run python test_dstu_comprehensive.py
```

### Окремий тестовий клас
```bash
python -m unittest test_dstu_comprehensive.TestDSTU_D1_Books
```

### Окремий тест
```bash
python -m unittest test_dstu_comprehensive.TestDSTU_D1_Books.test_d1_1_single_author_basic
```

### З детальним виводом
```bash
python -m unittest test_dstu_comprehensive -v
```

## Покриття

Тести охоплюють:

✅ **Типи записів:**
- Книги (однотомні)
- Автореферати дисертацій
- Електронні ресурси
- Статті в журналах
- Матеріали конференцій

✅ **Кількість авторів:**
- 1 автор
- 2 автори
- 3 автори
- 4 автори
- 5+ авторів

✅ **Мови:**
- Українська
- Російська (кирилиця)
- Англійська (латиниця)
- Змішані

✅ **Додаткові елементи:**
- URL з датами звернення
- DOI
- Томи та номери
- Діапазони сторінок
- Видання (2-ге, 3-тє, тощо)
- Типи видань (монографія, підручник, тощо)

✅ **Крайні випадки:**
- Відсутні поля
- LaTeX команди
- Різні формати дат
- Спеціальні символи

## Очікувані результати

Всі тести повинні проходити успішно (OK). При запуску виводиться:

```
======================================================================
ПІДСУМОК ТЕСТУВАННЯ
======================================================================
Всього тестів: 36
Успішно: 36
Помилки: 0
Винятки: 0

✅ ВСІ ТЕСТИ ПРОЙДЕНО УСПІШНО!
======================================================================
```

## Приклади тестів

### Приклад 1: Книга з одним автором
```python
def test_d1_1_single_author_basic(self):
    """Д.1.1.1: Дичківська О. О. Інноваційний менеджмент"""
    bibtex = """@book{dychkivska2018,
        author = {Дичківська, О. О.},
        title = {Інноваційний менеджмент},
        publisher = {ДІА},
        year = {2018},
        address = {Київ},
        pages = {82}
    }"""
    
    result = self.converter.convert_string_to_list(bibtex)[0]
    expected = "Дичківська О. О. Інноваційний менеджмент. Київ : ДІА, 2018. 82 с."
    
    self.assertEqual(result, expected)
```

### Приклад 2: Стаття з DOI
```python
def test_d13_3_article_six_authors_with_doi(self):
    """Д.13.3.5: Zadereyko О. та ін. Research of potential data leaks"""
    bibtex = """@article{zadereyko2022,
        author = {Zadereyko, О. and Trofymenko, O. and Prokop, Y. and Loginova, N. and Dyka, A. and Kukharenko, S.},
        title = {Research of potential data leaks in information and communication systems},
        journal = {Radio electronic and Computer Systems},
        year = {2022},
        number = {4},
        pages = {64--84},
        doi = {10.32620/reks.2022.4.05}
    }"""
    
    result = self.converter.convert_string_to_list(bibtex)[0]
    
    self.assertIn("Zadereyko О. та ін.", result)
    self.assertIn("DOI: https://doi.org/10.32620/reks.2022.4.05", result)
```

## Додавання нових тестів

Для додавання нового тесту:

1. Визначте категорію (Д.1, Д.3, тощо)
2. Додайте метод до відповідного класу
3. Назвіть метод `test_dX_Y_description`
4. Додайте docstring з описом прикладу з ДСТУ
5. Створіть BibTeX запис
6. Визначте очікуваний результат
7. Додайте перевірки (assertEqual або assertIn)

### Шаблон нового тесту

```python
def test_new_case(self):
    """Д.X.Y: Опис випадку з ДСТУ"""
    bibtex = """@type{key,
        field1 = {value1},
        field2 = {value2}
    }"""
    
    result = self.converter.convert_string_to_list(bibtex)[0]
    
    # Варіант 1: Точна відповідність
    expected = "Очікуваний результат згідно ДСТУ"
    self.assertEqual(result, expected)
    
    # Варіант 2: Перевірка наявності ключових елементів
    self.assertIn("Ключовий елемент 1", result)
    self.assertIn("Ключовий елемент 2", result)
```

## Відомі обмеження

1. Деякі складні випадки можуть вимагати ручного коригування
2. LaTeX символи повинні бути правильно екрановані в BibTeX
3. Дати повинні бути в стандартному форматі ISO (YYYY-MM-DD)

## Довідка

- **ДСТУ 8302:2015** - Національний стандарт України «Бібліографічне посилання. Загальні положення та правила складання»
- **Файл стандарту**: `docs/DSTU-8302-2015.txt`
- **Основний модуль**: `bibtex_to_dstu.py`
- **Тести**: `test_dstu_comprehensive.py`

## Підтримка

При виникненні проблем:
1. Перевірте формат BibTeX запису
2. Перегляньте приклади в `docs/DSTU-8302-2015.txt`
3. Запустіть тести з детальним виводом (`-v`)
4. Перевірте логи помилок

---

**Версія документації:** 1.0  
**Дата оновлення:** 10.02.2026  
**Всього тестів:** 36
