"""Testing solutions for CodeWars Problem reverse and mirror."""

# These are the tests from code wars

# s1, s2 ="FizZ", "buZZ"
# test.assert_equals(reverseAndMirror(s1,s2), "zzUB@@@zZIffIZz")

# s1, s2 ="String Reversing", "Changing Case"
# test.assert_equals(reverseAndMirror(s1,s2), "ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING")


# These are my own tests

def test_reverse_and_mirror_single():
    """Return strings with swapped cases. 1 reversed, the other mirrored."""
    from reverse_and_mirror import reverse_and_mirror
    assert reverse_and_mirror("FizZ", "buZZ") == "zzUB@@@zZIffIZz"


def test_reverse_and_mirror_multiple():
    """Return strings with swapped cases. 1 reversed, the other mirrored."""
    from reverse_and_mirror import reverse_and_mirror
    assert reverse_and_mirror("String Reversing", "Changing Case") == "ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING"
