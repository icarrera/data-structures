# -*- coding: utf-8 -*-
import pytest
from proper_parenthetics import proper_parens


open_1 = u"(((open)"
balanced_1 = u"balanced(())"
broken_1 = u"broken)"
broken_2 = u")))((("

def test_open():
    assert proper_parens(open_1) == 1

def test_balanced():
    assert proper_parens(balanced_1) == 0

def test_broken_1():
    assert proper_parens(broken_1) == -1

def test_broken_2():
    assert proper_parens(broken_2) == -1
