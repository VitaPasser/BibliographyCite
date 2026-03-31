def format_edition(edition: str, is_english: bool = False) -> str:
    """Форматує номер видання залежно від мови"""
    edition = edition.lower().replace('edition', '').strip()

    number_map = {
        'first': '1', '1st': '1',
        'second': '2', '2nd': '2',
        'third': '3', '3rd': '3',
        'fourth': '4', '4th': '4',
        'fifth': '5', '5th': '5',
    }

    edition_lower = edition.lower()
    edition_num = None

    for key, value in number_map.items():
        if key in edition_lower:
            edition_num = value
            break

    if not edition_num and edition.isdigit():
        edition_num = edition

    if edition_num:
        if is_english:
            if edition_num == '1':
                return "1st ed."
            elif edition_num == '2':
                return "2nd ed."
            elif edition_num == '3':
                return "3rd ed."
            else:
                return f"{edition_num}th ed."
        else:
            if edition_num == '3':
                return "3-тє вид."
            else:
                return f"{edition_num}-ге вид."

    return edition