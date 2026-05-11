import re


def replace_to_french_quotes(text):
    pattern = r'"([^"]*)"'

    result = re.sub(pattern, r'«\1»', text)

    return result