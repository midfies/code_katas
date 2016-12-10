"""Codewars problem Crazed Templating. Mstching letters in same length words."""


def letter_pattern(words):
    """Return letter that appears in the same place of all strings."""
    result = list(max(words, key=len))

    for i, letter in enumerate(words[0]):
        for word in words:
            if word[i] != letter:
                result[i] = '*'
    return ''.join(result)
