from typing import Dict, List

from ..author.author_inverted import format_author_inverted
from .get_editor_type import get_editor_type


def handle_editors_with_authors(entry: Dict, parts: List[str], note: str):
    """Обробляє редакторів коли є 4+ авторів"""
    editor = entry.get('editor', '')

    if not editor:
        return

    editors_list = [e.strip() for e in editor.split(' and ')]
    has_others = any(e.lower() == 'others' for e in editors_list)
    editors_list = [e for e in editors_list if e.lower() != 'others']

    # Визначаємо тип редактора з editortype (пріоритет) або note
    editor_type = get_editor_type(entry)
    if not editor_type:
        editor_type = "заг. ред."

    if has_others and editors_list:
        first_editor = format_author_inverted(editors_list[0])
        if 'відп. ред.' in note:
            parts.append(f"; {editor_type} {first_editor} (відп. ред.) та ін.")
        else:
            parts.append(f"; {editor_type} {first_editor} та ін.")
    elif len(editors_list) == 1:
        editor_name = format_author_inverted(editors_list[0])
        parts.append(f"; {editor_type} {editor_name}")
    else:
        formatted_editors = [format_author_inverted(e) for e in editors_list]
        parts.append(f"; {editor_type} {', '.join(formatted_editors)}")