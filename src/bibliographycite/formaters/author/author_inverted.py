from .utils.split_author_no_comma import split_author_no_comma


def format_author_inverted(author: str) -> str:
    """Форматує одного автора: І.Б. Прізвище"""
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
            return f"{' '.join(initials)} {lastname}"
        return lastname
    else:
        parts = author.split()
        if len(parts) >= 2:
            lastname, firstnames = split_author_no_comma(parts)
            initials = [name[0].upper() + '.' for name in firstnames if name]
            if initials:
                return f"{' '.join(initials)} {lastname}"
            return lastname
        return author


def format_author_inverted_fullname(author: str) -> str:
    """Форматує одного автора: Ім'я По батькові Прізвище"""
    author = ' '.join(author.split())

    if ',' in author:
        return author
    else:
        parts = author.split()
        if len(parts) >= 2:
            lastname, firstnames = split_author_no_comma(parts)
            return f"{' '.join(firstnames)} {lastname}"
        return author
