#-*- coding: utf-8 -*-
import parenthetic
import pytest

PAREN_TESTS = [
            (u'blahblah(())', 0),
            (u'))))((((', -1),
            (u'(()stuff', 1),
]

@pytest.mark.parametrize('input, result', PAREN_TESTS)
def test_valid_parenthetic(input, result):
    assert parenthetic.valid_parenthetic(input) == result
