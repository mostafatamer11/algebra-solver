from logic import *

if __name__ == "__main__":
    print(lex_numbers(lex_operators("1+1-1*1/1")))
    print(lex_operators(lex_numbers("1+1-1*1/1")))
