from typing import List

from utils.replace_to_french_quotes import replace_to_french_quotes


def finalize_entry(parts: List[str]) -> str:
    """Фіналізує запис, об'єднуючи частини і додаючи крапку в кінці"""
    if not parts:
        return ""

    result_parts = []
    for i, part in enumerate(parts):
        if i == 0:
            result_parts.append(part)
        else:
            # Якщо частина починається з "/" або ";"
            if part.startswith(('/', '  ;', '; ')):
                result_parts.append(' ' + part)
            # Якщо попередня частина закінчується квадратною дужкою
            elif result_parts[-1].endswith(']'):
                result_parts.append(' ' + part)
            # Якщо попередня частина закінчується крапкою
            elif result_parts[-1].endswith('.'):
                result_parts.append(' ' + part)
            # Якщо попередня частина закінчується дужкою
            elif result_parts[-1].endswith(')'):
                result_parts.append('. ' + part)
            else:
                result_parts.append('. ' + part)

    result = ''.join(result_parts)
    # Переконуємося, що результат закінчується крапкою (але не якщо закінчується слешем)
    if not result.endswith('.') and not result.endswith('/'):
        result += '.'
    result = replace_to_french_quotes(result)
    return result