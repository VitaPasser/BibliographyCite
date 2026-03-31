import re


def format_access_date(date_string: str) -> str:
    """Форматує дату звернення до ресурсу"""
    if not date_string:
        return ""

    date_string = date_string.replace('дата звернення:', '').strip()
    date_string = date_string.replace('accessed:', '').strip()

    if re.match(r'\d{2}\.\d{2}\.\d{4}', date_string):
        return date_string

    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_string)
    if match:
        return f"{match.group(3)}.{match.group(2)}.{match.group(1)}"

    match = re.search(r'(\d{2})[-/](\d{2})[-/](\d{4})', date_string)
    if match:
        return f"{match.group(1)}.{match.group(2)}.{match.group(3)}"

    return date_string