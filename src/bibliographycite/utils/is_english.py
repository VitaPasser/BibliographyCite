import re
from typing import Dict


def is_english(entry: Dict) -> bool:
    """Визначає, чи є запис англомовним"""
    author = entry.get('author', '')
    title = entry.get('title', '')
    journal = entry.get('journal', '')

    cyrillic_pattern = re.compile('[а-яА-ЯіїєґІЇЄҐ]')

    # Підраховуємо кириличні символи
    all_text = f"{author} {title} {journal}"
    cyrillic_count = len(cyrillic_pattern.findall(all_text))
    total_letters = len(re.findall(r'[a-zA-Zа-яА-ЯіїєґІЇЄҐ]', all_text))

    # Якщо кириличних букв менше 10% від загальної кількості, вважаємо англомовною
    if total_letters > 0 and cyrillic_count / total_letters < 0.1:
        return True

    # Якщо немає кириличних символів взагалі
    if cyrillic_count == 0:
        return True

    return False