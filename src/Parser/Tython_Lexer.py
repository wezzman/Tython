'''
Created on Apr 19, 2013

@author: michael
'''

import ply.lex as lex


keywords = (
    "Def",
    "For",
    "If",
    "Else",
    "Elif",
    "Class",
    "Lambda"
)

tokens = keywords + (
    "Name",
    "Integer",
    "Floating",
    "String",
    "Import",
    "While",
    "BOperator",
    "UOperator"
    "WSpace",
    "NLine",
    "LParen",
    "RParen",
    "LBrack",
    "RBrack",  
    "Brace",
    "Comma"
)

digit = r'([0-9])'
nondigit = r'([_A-Za-z])'
t_Name = r''

def find_column(input, token):
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print "Illegal character  '%s' at line '%d'" % t.value[0], t.lexer.lineno
    t.lexer.skip(1)


    
lexer = lex.lex()