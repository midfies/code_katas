"""Testing solutions for CodeWars Problem reverse and mirror."""

import pytest

# These are the tests from code wars

# s1, s2 ="FizZ", "buZZ"
# test.assert_equals(reverseAndMirror(s1,s2), "zzUB@@@zZIffIZz")

# s1, s2 ="String Reversing", "Changing Case"
# test.assert_equals(reverseAndMirror(s1,s2), "ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING")


# These are my own tests

TEST_TABLE = [
    ["FizZ", "buZZ", "zzUB@@@zZIffIZz"],
    ["String Reversing", "Changing Case", "ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING"],
]


@pytest.mark.parametrize("first, second, result", TEST_TABLE)
def test_reverse_and_mirror(first, second, result):
    """Return strings with swapped cases. 1 reversed, the other mirrored."""
    from reverse_and_mirror import reverse_and_mirror
    assert reverse_and_mirror(first, second) == result
