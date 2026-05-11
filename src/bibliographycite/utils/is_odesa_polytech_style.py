def is_odesa_polytech_style(entry: dict) -> bool:
    return entry.get('style', '') == 'odesa_polytech'