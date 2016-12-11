"""Codewars problem for flattening an array of arrays."""


def flatten_me(lst):
    """Return nested lists into a singular list."""
    flat = []
    for sublist in lst:
        if type(sublist) is not list:
            flat.append(sublist)
        else:
            for next_sub in sublist:
                flat.append(next_sub)
    return flat
