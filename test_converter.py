"""Тест конвертера для отладки"""
from bibtex_to_dstu import BibTeXToDSTUConverter

converter = BibTeXToDSTUConverter()

# Простой тест
bibtex = """
@book{test2018,
    author = {Дичківська, О. О.},
    title = {Інноваційний менеджмент},
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
print("Длина:", len(result[0]))
print()

# Поиск двойных точек
if '..' in result[0]:
    print("НАЙДЕНЫ ДВОЙНЫЕ ТОЧКИ!")
    idx = result[0].index('..')
    print(f"Позиция: {idx}")
    print(f"Контекст: '{result[0][max(0, idx-10):idx+10]}'")
else:
    print("Двойных точек нет - всё правильно!")

print()
print("Проверка на соответствие эталону:")
expected = "Дичківська О. О. Інноваційний менеджмент. Київ : ДІА, 2018. 82 с."
print(f"Эталон:    '{expected}'")
print(f"Получено:  '{result[0]}'")
print(f"Совпадает: {result[0] == expected}")
