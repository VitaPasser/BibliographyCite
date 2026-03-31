def to_genitive(lastname: str) -> str:
    """Просте перетворення прізвища у родовий падіж"""
    if lastname.endswith('ко') or lastname.endswith('енко'):
        return lastname[:-1] + 'а'
    elif lastname.endswith('ук') or lastname.endswith('юк'):
        return lastname + 'а'
    elif lastname.endswith('ський') or lastname.endswith('цький'):
        return lastname.replace('ий', 'ого')
    elif lastname.endswith('ов') or lastname.endswith('ев') or lastname.endswith('ёв'):
        return lastname + 'а'
    elif lastname.endswith('ін') or lastname.endswith('їн'):
        return lastname + 'а'
    elif lastname.endswith('ня'):
        return lastname[:-2] + 'ні'
    elif lastname.endswith('й'):
        return lastname[:-1] + 'я'
    else:
        if any(char in lastname.lower() for char in 'абвгдежзийклмнопрстуфхцчшщъыьэюяієїґ'):
            return lastname + 'а'
        return lastname