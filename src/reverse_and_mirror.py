"""CodeWars String Reversing and Changing Case."""


def reverse_and_mirror(s1, s2):
    """Return s2 case-swapped and reversed + s1 case-swapped and mirrored."""
    s1 = s1.swapcase()
    return s2.swapcase()[::-1] + "@@@" + s1[::-1] + s1
