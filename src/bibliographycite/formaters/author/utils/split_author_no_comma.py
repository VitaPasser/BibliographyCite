def split_author_no_comma(parts: list) -> tuple[str, list]:
    """Визначає прізвище і решту імені для автора без коми.

    Якщо всі частини - довгі слова без крапок (формат Прізвище Ім'я По-батькові),
    то перше слово вважається прізвищем.
    Інакше (стандартний BibTeX "FirstName LastName") - останнє слово прізвище.
    """
    if len(parts) >= 2 and all(len(p.replace('.', '')) > 1 and '.' not in p for p in parts):
        # Прізвище Ім'я [По-батькові]
        return parts[0], parts[1:]
    else:
        # BibTeX стандарт: FirstName(s) LastName
        return parts[-1], parts[:-1]