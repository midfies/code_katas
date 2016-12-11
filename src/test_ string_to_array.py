"""Testing solutions for CodeWars Problem string to array()."""

# These are the tests from code wars

# Test.describe("Basic tests")
# Test.assert_equals(string_to_array("Robin Singh"), ["Robin", "Singh"])
# Test.assert_equals(string_to_array("CodeWars"), ["CodeWars"])
# Test.assert_equals(string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
# Test.assert_equals(string_to_array("1 2 3"), ["1", "2", "3"])
# Test.assert_equals(string_to_array(""), [""])


# These are my own tests


def test_string_to_array_name():
    """Return array of first and last name given a single string name."""
    from string_to_array import string_to_array
    assert string_to_array("Robin Singh") == ["Robin", "Singh"]


def test_string_to_array_single():
    """Return array of single word when given a single word string."""
    from string_to_array import string_to_array
    assert string_to_array("CodeWars") == ["CodeWars"]


def test_string_to_array_sentence():
    """Return array of multiple words when given a sentence."""
    from string_to_array import string_to_array
    assert string_to_array("I love arrays they are my favorite") == ["I", "love", "arrays", "they", "are", "my", "favorite"]


def test_string_to_array_numbers():
    """Return array of string numbers when given a string of multiple #s."""
    from string_to_array import string_to_array
    assert string_to_array("1 2 3") == ["1", "2", "3"]


def test_string_to_array_empty():
    """Return array with empty string when given empty string."""
    from string_to_array import string_to_array
    assert string_to_array("") == [""]
