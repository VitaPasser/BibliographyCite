def normalize_editor_type(raw: str) -> str:
    """Нормалізує одне значення типу редактора.

    Убирає префікс "за " в початку (за ред. -> ред., за заг. ред. -> заг. ред.),
    а також приводить до канонічного вигляду.
    """
    t = raw.strip()
    # Убираємо префікс "за " в початку
    if t.lower().startswith('за '):
        t = t[3:].strip()

    tl = t.lower()
    if 'редкол' in tl:
        return 'редкол.'
    if 'заг. наук. ред.' in tl:
        return 'заг. наук. ред.'
    if 'голов. ред.' in tl:
        return 'голов. ред.'
    if 'заг. ред.' in tl:
        return 'заг. ред.'
    if 'упоряд. та відп. ред.' in tl or 'упоряд. і відп. ред.' in tl:
        return t  # зберігаємо дослівно
    if 'відпов. за вип.' in tl or 'відп. за вип.' in tl:
        return t
    if 'уклад.' in tl:
        return 'уклад.'
    if 'упоряд.' in tl:
        return 'упоряд.'
    if 'ред.' in tl:
        return 'ред.'
    if 'ed. by' in tl:
        return 'ed. by'
    return t