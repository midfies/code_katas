"""Codewar problem Friend or Foe?."""


def friend(x):
    """Return array of four letter names given array of names."""
    friends = []
    for name in x:
        if len(name) == 4:
            friends.append(name)
    return friends
