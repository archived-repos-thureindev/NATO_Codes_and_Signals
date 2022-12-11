"""Text to NATO code"""
from nato_codes import NATO_CODES as CODES


def get_all(text):
    """Returns a <list> of <dict>"""
    translated_code = [CODES[letter.upper()] for letter in text if letter.isalnum()]
    return translated_code


def get_alphabet(text, include_phonetic=False):
    """Returns a <list> of <str> OR <list> of <dict>"""
    if include_phonetic:
        words_with_phonetics = [{"word": CODES[letter.upper()]["word"], "phonetic": CODES[letter.upper()]["phonetic"]}
                                for letter in text if letter.isalnum()]
        return words_with_phonetics

    words = [CODES[letter.upper()]["word"] for letter in text if letter.isalnum()]
    return words


def get_morse(text):
    """Returns a <list> of <str>"""
    morse = [CODES[letter.upper()]["morse"] for letter in text if letter.isalnum()]
    return morse

