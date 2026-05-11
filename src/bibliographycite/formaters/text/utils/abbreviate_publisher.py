import re

from bibliographycite.utils.shorten_ukr_city import shorten_ukr_city


def abbreviate_publisher(publisher: str) -> str:
    """Скорочує повні назви видавництв/організацій згідно з ДСТУ 3582:2013.

    Наприклад:
      "Інститут літератури імені Т. Г. Шевченка" -> "Ін-т літератури ім. Т. Г. Шевченка"
      "Національний університет "Одеська політехніка"" -> "Нац. ун-т "Одес. політехніка""
    """

    p = publisher
    replacements = [
        (r'\bІнститут\b', 'Ін-т'),
        (r'\bінститут\b', 'ін-т'),
        (r'\bInstitute\b', 'Inst.'),
        (r'\bімені\b', 'ім.'),
        (r'\bіменi\b', 'ім.'),  # латинська i
        (r'\bНаціональний університет\b', 'Нац. ун-т'),
        (r'\bНаціональний\b', 'Нац.'),
        (r'\bДержавний\b', 'Держ.'),
        (r'\bУніверситет\b', 'ун-т'),
        (r'\bуніверситет\b', 'ун-т'),
        (r'\bАкадемія\b', 'акад.'),
        (r'\bакадемія\b', 'акад.'),
        (r'\bМіністерство\b', 'М-во'),
        (r'\bміністерство\b', 'м-во'),
    ]

    for pattern, repl in replacements:
        p = re.sub(pattern, repl, p)
        p = process_text_in_quotes(p)

    return p


def process_text_in_quotes(text):
    pattern = r'"(.*?)"'

    def replace_func(match):
        content:str = match.group(1)  # Текст внутри кавычек
        contents = content.split(' ')
        shortened = shorten_ukr_city(contents[0])
        return f'"{shortened} {' '.join(contents[1:])}"'

    return re.sub(pattern, replace_func, text)