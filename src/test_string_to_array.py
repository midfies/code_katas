"""Testing solutions for CodeWars Problem string to array()."""

import pytest

# These are the tests from code wars

# Test.describe("Basic tests")
# Test.assert_equals(string_to_array("Robin Singh"), ["Robin", "Singh"])
# Test.assert_equals(string_to_array("CodeWars"), ["CodeWars"])
# Test.assert_equals(string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
# Test.assert_equals(string_to_array("1 2 3"), ["1", "2", "3"])
# Test.assert_equals(string_to_array(""), [""])


# These are my own tests

TEST_TABLE = [
    ["Robin Singh", ["Robin", "Singh"]],
    ["CodeWars", ["CodeWars"]],
    ["I love arrays they are my favorite", ["I", "love", "arrays", "they", "are", "my", "favorite"]],
    ["1 2 3", ["1", "2", "3"]],
    ["", [""]],
]


@pytest.mark.parametrize("string, result", TEST_TABLE)
def test_string_to_array(string, result):
    """Return array of first and last name given a single string name."""
    from string_to_array import string_to_array
    assert string_to_array(string) == result
