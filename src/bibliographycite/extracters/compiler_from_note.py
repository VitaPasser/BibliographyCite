import re


def extract_compiler_from_note(note: str) -> str:
    """Витягує інформацію про укладача з note"""
    if 'уклад.' in note:
        # Знаходимо текст після "уклад."
        match = re.search(r'уклад\.\s*([^;]+)', note)
        if match:
            return f"уклад. {match.group(1).strip()}"
    return ""