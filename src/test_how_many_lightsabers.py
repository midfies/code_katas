"""Testing solutions for CodeWars Problem howManyLighSabers()."""

import pytest

# These are the tests from code wars

# test.assert_equals(howManyLightsabersDoYouOwn("Zach"), 18)
# test.assert_equals(howManyLightsabersDoYouOwn(""), 0)
# test.assert_equals(howManyLightsabersDoYouOwn("Bill"), 0)


# These are my own tests

TEST_TABLE = [
    ["", 0],
    ["Bill", 0],
    ["Zach", 18],
]


@pytest.mark.parametrize("string, result", TEST_TABLE)
def test_how_many_lightsabers_empty(string, result):
    """Return 0 if emptyString is passed."""
    from how_many_lightsabers import how_many_lightsabers_do_you_own
    assert how_many_lightsabers_do_you_own(string) == result
