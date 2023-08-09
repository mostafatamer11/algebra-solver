"""
# Tokens
### The above class defines different types of tokens for algebriac expressions, including INT, VAR, OPER, etc.. for the Lexer
"""

EOFs = 0


class Token(object):
    def __init__(self, value:str):
        global EOFs
        if EOFs:
            raise ExceptionGroup("EOF")
        self.value = value

    def __repr__(self) -> str:
        return f"TOKEN({self.value}) "


class INT(Token):
    def __repr__(self) -> str:
        return f"INT({self.value}) "

    def __in__(self, *args) -> bool:
        return False


class VAR(Token):
    def __repr__(self) -> str:
        return f"VAR({self.value}) "


class OPER(Token):
    def __repr__(self) -> str:
        return "OPER(" + self.value + ") "

    def isdigit(self):
        return False


class EOF(Token):
    def __init__(self):
        global EOFs
        EOFs += 1

    def __repr__(self):
        return "EOF"