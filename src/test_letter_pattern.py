"""Tests for codewars Crazed Templating."""

import pytest

# These are the tests from code wars

# test_list = ['war', 'rad', 'dad']
# test.assert_equals(letter_pattern(test_list), "*a*")

# test_list = ['general', 'admiral', 'piglets', 'secrets']
# test.assert_equals(letter_pattern(test_list), "*******")

# test_list = ['family']
# test.assert_equals(letter_pattern(test_list), "family")

# These are my own tests


PATTERN_TABLE = [
    [['war', 'rad', 'dad'], "*a*"],
    [['general', 'admiral', 'piglets', 'secrets'], "*******"],
    [['family'], "family"],

]


@pytest.mark.parametrize("words, result", PATTERN_TABLE)
def test_letter_pattern(words, result):
    """Test letter_pattern returns mathching letters from all stings."""
    from letter_pattern import letter_pattern
    assert letter_pattern(words) == result
