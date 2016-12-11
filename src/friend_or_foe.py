"""Codewar problem Friend or Foe?."""


def friend(x):
    """Return array of four letter names given array of names."""
    return [name for name in x if len(name) == 4]
