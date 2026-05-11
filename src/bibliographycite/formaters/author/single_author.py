from .utils.split_author_no_comma import split_author_no_comma


def format_single_author(author: str) -> str:
    """Форматує одного автора: Прізвище І. Б."""
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
            return f"{lastname} {' '.join(initials)}"
        return lastname
    else:
        parts = author.split()
        if len(parts) >= 2:
            lastname, firstnames = split_author_no_comma(parts)
            initials = [name[0].upper() + '.' for name in firstnames if name]
            return f"{lastname} {' '.join(initials)}"
        return author