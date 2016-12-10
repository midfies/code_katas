"""CodeWars problem string to array - 8th Kyu."""


def string_to_array(string):
    """Return array split by whitespace to an array."""
    if string == '':
        return ['']
    return string.split()
