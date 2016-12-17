"""Testing solutions for CodeWars Problem howManyLighSabers()."""

# These are the tests from code wars

# test.assert_equals(howManyLightsabersDoYouOwn("Zach"), 18)
# test.assert_equals(howManyLightsabersDoYouOwn(""), 0)
# test.assert_equals(howManyLightsabersDoYouOwn("Bill"), 0)


# These are my own tests


def test_how_many_lightsabers_empty():
    """Return 0 if emptyString is passed."""
    from how_many_lightsabers import how_many_lightsabers_do_you_own
    assert how_many_lightsabers_do_you_own("") == 0


def test_how_many_lightsabers_not_zach():
    """Return 0 if any name other than Zach is passed."""
    from how_many_lightsabers import how_many_lightsabers_do_you_own
    assert how_many_lightsabers_do_you_own("Bill") == 0


def test_how_many_lightsabers_zach():
    """Return 18 if Zach is passed."""
    from how_many_lightsabers import how_many_lightsabers_do_you_own
    assert how_many_lightsabers_do_you_own("Zach") == 18
