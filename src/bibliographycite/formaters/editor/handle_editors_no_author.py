from typing import Dict, List

from bibliographycite.extracters.compiler_from_note import extract_compiler_from_note
from bibliographycite.formaters.author.author_inverted import format_author_inverted
from bibliographycite.formaters.author.single_author import format_single_author
from bibliographycite.formaters.editor.get_editor_type import get_editor_type
from bibliographycite.formaters.editor.get_per_editor_types import get_per_editor_types


def handle_editors_no_author(entry: Dict, parts: List[str], note: str):
    """Обробляє редакторів коли немає авторів.

    note - вже нормалізований тип (з _get_editor_type) або сирий note.
    """
    editor = entry.get('editor', '')

    if not editor:
        # Перевіряємо note на наявність інформації типу "упоряд. В. Олексик"
        raw_note = entry.get('note', '')
        if raw_note and ('упоряд.' in raw_note or 'уклад.' in raw_note):
            parts.append(f"/ {raw_note}")
        return

    editors_list = [e.strip() for e in editor.split(' and ')]
    has_others = any(e.lower() == 'others' for e in editors_list)
    editors_list = [e for e in editors_list if e.lower() != 'others']

    # Отримуємо тип редактора. note вже може бути нормалізованим типом або пустим.
    etype = note  # передали вже нормалізований тип

    # Якщо пустий - визначаємо з editortype/note запису
    if not etype:
        etype = get_editor_type(entry)

    # Підтримка кількох типів редакторів (наприклад "заг. ред. and уклад.")
    per_types = get_per_editor_types(entry)
    editortype_raw = entry.get('editortype', '').strip()
    has_multiple_types = ' and ' in editortype_raw

    if has_multiple_types and len(per_types) >= 2 and not has_others:
        # Кожен редактор має свій тип: "/ заг. ред. В. І. Гарапко, уклад. А. І. Гарапко"
        parts_str = []
        for i, (ed, et) in enumerate(zip(editors_list, per_types)):
            fmt = format_author_inverted(ed)
            parts_str.append(f"{et} {fmt}")
        parts.append(f"/ {', '.join(parts_str)}")
        return

    if 'редкол' in etype.lower():
        raw_note = entry.get('note', '')
        is_for_all = 'all' in editortype_raw.lower()
        if len(editors_list) == 1:
            editor_name = format_author_inverted(editors_list[0])
            if has_others:
                editoraftertype = entry.get('editoraftertype', '').strip()
                if 'відп.' in editoraftertype or 'відп. ред.' in editoraftertype:
                    editor_name = f'{editor_name} (відп. ред.)'
                if is_for_all:
                    parts.append(f"/ редкол. : {editor_name} та ін.")
                else:
                    parts.append(f"/ редкол. {editor_name} та ін.")
            else:
                has_extra_info = ';' in raw_note and 'відп. ред.' in raw_note
                if has_extra_info:
                    parts.append(f"/ редкол. : {editor_name}")
                else:
                    parts.append(f"/ редкол.: {editor_name}")
        else:
            first_editor = format_author_inverted(editors_list[0])
            parts.append(f"/ редкол.: {first_editor} та ін.")

    elif 'голов. ред.' in etype:
        if len(editors_list) == 1:
            editor_name = format_author_inverted(editors_list[0])
            parts.append(f"/ голов. ред. {editor_name}")
        else:
            formatted_editors = [format_author_inverted(e) for e in editors_list]
            parts.append(f"/ голов. ред. : {', '.join(formatted_editors)}")

    elif 'заг. наук. ред.' in etype:
        if len(editors_list) == 1:
            editor_name = format_author_inverted(editors_list[0])
            parts.append(f"/ заг. наук. ред. {editor_name}")
        else:
            formatted_editors = [format_author_inverted(e) for e in editors_list]
            parts.append(f"/ заг. наук. ред. : {', '.join(formatted_editors)}")

    elif 'заг. ред.' in etype:
        raw_note = entry.get('note', '')
        if len(editors_list) == 1:
            editor_name = format_author_inverted(editors_list[0])
            # Перевіряємо, є ли "уклад." в note
            if 'уклад.' in raw_note or 'уклад. :' in raw_note:
                compiler_info = extract_compiler_from_note(raw_note)
                if compiler_info:
                    if 'відп. за вип.' in raw_note:
                        parts.append(f"/ {compiler_info} ; відп. за вип. {editor_name}")
                    else:
                        parts.append(f"/ заг. ред. {editor_name}; {compiler_info}")
                else:
                    parts.append(f"/ заг. ред. {editor_name}")
            else:
                parts.append(f"/ заг. ред. {editor_name}")
        else:
            formatted_editors = [format_author_inverted(e) for e in editors_list]
            parts.append(f"/ заг. ред. : {', '.join(formatted_editors)}")

    elif 'ред.' in etype:
        if len(editors_list) == 1:
            editor_name = format_author_inverted(editors_list[0])
            parts.append(f"/ ред. {editor_name}")
        else:
            formatted_editors = [format_author_inverted(e) for e in editors_list]
            parts.append(f"/ ред. : {', '.join(formatted_editors)}")

    elif 'упоряд.' in etype or 'уклад.' in etype:
        if editors_list:
            compiler = format_single_author(editors_list[0])
            keyword = 'упоряд.' if 'упоряд.' in etype else 'уклад.'
            parts.append(f"/ {keyword} {compiler}")
        else:
            compiler_info = extract_compiler_from_note(entry.get('note', ''))
            if compiler_info:
                parts.append(f"/ {compiler_info}")

    else:
        # Неізвестний тип - використовуємо "ред." за замовчуванням
        if editors_list:
            if len(editors_list) == 1:
                editor_name = format_author_inverted(editors_list[0])
                parts.append(f"/ ред. {editor_name}")
            else:
                formatted_editors = [format_author_inverted(e) for e in editors_list]
                parts.append(f"/ ред. : {', '.join(formatted_editors)}")