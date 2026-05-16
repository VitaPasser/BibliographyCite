from .author_inverted import format_author_inverted
from .single_author import format_single_author
from ...utils.is_english import is_english


def format_authors(authors_string: str, max_authors: int = 3, inverted: bool = False, force_all: bool = False) -> \
tuple[str, int]:
    """
    Форматує авторів згідно з ДСТУ 8302:2015.

    Args:
        authors_string: Строка авторів (розділені 'and')
        max_authors: Максимальна кількість авторів для відображення
        inverted: Використовувати формат "І.О. Прізвище" замість "Прізвище І.О."
        force_all: Форсувати вивід всіх авторів незалежно від кількості
    """
    if not authors_string:
        return "", 0

    # Розділяємо авторів і фільтруємо "others"
    authors = [a.strip() for a in authors_string.split(' and ')]
    authors = [a for a in authors if a.lower() != 'others']
    author_count = len(authors)

    format_func = format_author_inverted if inverted else format_single_author

    # Якщо force_all=True, виводимо всіх авторів
    if force_all:
        formatted_authors = [format_func(a) for a in authors]
        return ', '.join(formatted_authors), author_count

    formatted_authors = []
    for author in authors[:max_authors]:
        formatted_authors.append(format_func(author))

    if author_count <= 3:
        return ', '.join(formatted_authors), author_count
    elif author_count == 4 and max_authors >= 4:
        all_formatted = [format_func(a) for a in authors]
        return ', '.join(all_formatted), author_count
    else:
        # 5+ авторів
        _is_english = is_english({'author': authors_string})
        et_al = ' et al.' if _is_english else ' та ін.'
        return formatted_authors[0] + et_al, author_count