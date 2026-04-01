from typing import Dict

from .normalize_editor_type import normalize_editor_type
from .get_editor_type import get_editor_type


def get_per_editor_types(entry: Dict) -> list:
    """Повертає список нормалізованих типів для кожного редактора.

    editortype може містити кілька значень через ' and ', кожне з яких
    відповідає окремому редактору з поля editor (теж розділених ' and ').
    Префікс "за " прибирається з кожного значення.

    Приклади:
      editortype = "заг. ред. and уклад."  -> ['заг. ред.', 'уклад.']
      editortype = "за ред."               -> ['ред.', 'ред.', ...]  (для всіх ред-рів)
      editortype = "редкол. all"           -> ['редкол.', 'редкол.', ...]
    """
    editortype = entry.get('editortype', '').strip()
    editor = entry.get('editor', '').strip()
    if not editor:
        return []
    editors_raw = [e.strip() for e in editor.split(' and ') if e.strip().lower() != 'others']
    n = len(editors_raw)

    if ' and ' in editortype:
        raw_types = [t.strip() for t in editortype.split(' and ')]
        normalized = [normalize_editor_type(t) for t in raw_types]
        # Доповнюємо до кількості редакторів останнім значенням
        while len(normalized) < n:
            normalized.append(normalized[-1] if normalized else 'ред.')
        return normalized[:n]
    else:
        # Один тип для всіх редакторів
        single = get_editor_type(entry)
        return [single] * n