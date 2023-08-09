from __future__ import print_function
from tokens import *


def lex_numbers(equ: str):
    i = 0
    result = ""
    while i < len(equ):
        char = equ[i]
        if char.isdigit():
            number = ""
            try:
                while equ[i].isdigit():
                    number += equ[i]
                    i += 1
            except IndexError:
                result += str(INT(number))
                continue
            result += str(INT(number))
            continue
        else:
            result += char
        i += 1

    return result


def lex_operators(equ: str):
    """
    The function `lex_operators` takes a string as input and returns a modified version of the string
    where consecutive operators are replaced with a single operator.
    
    #### param equ: The parameter `equ` is a string representing an equation
    #### type equ: str
    #### return: The function `lex_operators` returns a modified version of the input string `equ` where the
    operators (+, -, *, /) are replaced with the result of applying the `OPER` token to the operator.
    """
    i = 0
    result = ""
    while i < len(equ):
        char = equ[i]
        if char in "+-*/":
            number = ""
            try:
                while equ[i] in "+-*/":
                    number += equ[i]
                    i += 1
            except IndexError:
                result += str(OPER(number))
                continue
            result += str(OPER(number))
            continue
        else:
            result += char
        i += 1

    return result
