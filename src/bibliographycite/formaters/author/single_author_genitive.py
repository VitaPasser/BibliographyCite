from .utils.split_author_no_comma import split_author_no_comma
from .utils.to_genitive import to_genitive


def format_single_author_genitive(author: str) -> str:
    """Форматує одного автора у родовому відмінку: І. Б. Прізвища"""
    author = ' '.join(author.split())

    if ',' in author:
        parts = author.split(',', 1)
        lastname = parts[0].strip()
        firstnames = parts[1].strip() if len(parts) > 1 else ''

        initials = []
        for name in firstnames.split():
            name = name.strip().replace('.', '')
            if name:
                initials.append(name[0].upper() + '.')

        if initials:
            genitive_lastname = to_genitive(lastname)
            return f"{' '.join(initials)} {genitive_lastname}"
        return to_genitive(lastname)
    else:
        parts = author.split()
        if len(parts) >= 2:
            lastname, firstnames = split_author_no_comma(parts)
            initials = [name[0].upper() + '.' for name in firstnames if name]
            if initials:
                genitive_lastname = to_genitive(lastname)
                return f"{' '.join(initials)} {genitive_lastname}"
            return to_genitive(lastname)
        return author