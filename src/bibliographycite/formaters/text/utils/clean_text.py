import re


def clean_text(text: str) -> str:
    """Очищує текст від спеціальних символів LaTeX і зайвих пробілів"""
    if not text:
        return ""

    text = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\[a-zA-Z]+', '', text)

    text = text.replace('{', '').replace('}', '')

    text = text.replace('``', '"').replace("''", '"')
    text = text.replace('`', "'")

    text = ' '.join(text.split())

    return text.strip()