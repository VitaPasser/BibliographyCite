import re


def shorten_ukr_city(name: str) -> str:
    if " " in name:
        parts = name.split()
        return " ".join([shorten_ukr_city(p) for p in parts])

    match = re.search(r'^([^аеиоуюяіїє]*[аеиоуюяіїє][^аеиоуюяіїє])', name)

    if match:
        return match.group(1).capitalize() + '.'
    return name[:3] + "."