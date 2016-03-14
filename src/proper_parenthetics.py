# -*- coding: utf-8-*-
"""Whiteboard challenge - Proper Parentheses"""

def proper_parens(text):
    """Finds if the parentheses in a string are open, balanced, or broken."""
    paren_val = 0
    for char in text:
        if char == "(":
            paren_val += 1
        elif char == ")":
            paren_val -= 1
            if paren_val < 0:
                break
    if paren_val > 0:
        return 1
    elif paren_val < 0:
        return -1
    return paren_val
