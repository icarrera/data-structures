#-*- coding: utf-8 -*-


def valid_parenthetic(text):
    """Take text and determine if all parens are properly ordered and closed.

    return 1 if 'open' (Open parens are not close)
    return 0 if 'closed' (All parens are closed)
    return -1 if 'broken' (a closing has not been preceded by one that opens)
    """
    unclosed_parens = 0
    for char in text:
        if char == u'(':
            unclosed_parens += 1
        elif char == u')':
            if unclosed_parens == 0:
                return -1
            unclosed_parens -= 1
    if unclosed_parens > 0:
        return 1
    elif unclosed_parens < 0:
        return -1
    return unclosed_parens
