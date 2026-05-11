from typing import Dict

from .normalize_editor_type import normalize_editor_type


def get_editor_type(entry: Dict) -> str:
    """Повертає тип редактора з editortype (пріоритет) або note.

    Нормалізує значення: прибирає префікс "за ", приводить до канонічної форми.
    Береться перше значення, якщо editortype містить кілька (через ' and ').
    """
    editortype = entry.get('editortype', '').strip()
    note = entry.get('note', '').strip()

    # Беремо перше значення editortype
    raw = editortype.split(' and ')[0].strip() if editortype else ''

    if raw:
        return normalize_editor_type(raw)

    # Фолбек на note
    if 'редкол.' in note:
        return 'редкол.'
    if 'заг. наук. ред.' in note:
        return 'заг. наук. ред.'
    if 'голов. ред.' in note:
        return 'голов. ред.'
    if 'заг. ред.' in note or 'за заг. ред.' in note:
        return 'заг. ред.'
    if 'ред.' in note:
        return 'ред.'
    return ''