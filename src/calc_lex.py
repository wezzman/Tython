
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    "Plus",
    "Minus",
    "Times",
    "Divide",
    "LParen",
    "RParen",
    "Integer",
    "Floating"
)


t_Plus = r'\+'
t_Minus = r'\-'
t_Divide = r'\/'
t_Times = r'\*'

t_LParen = r'\('
t_RParen = r'\)'

def t_Integer(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_Floating(t):
    r'\d+.d+'
    t.value = float(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print "Illegal character " + t.value[0]
    t.lexer.skip(1)
    
lexer = lex.lex() 


import ply.yacc as yacc


def p_bin_op(p):
    """expression : expression Plus term
                  |  expression Minus term
       term       : term Times factor
                  | term Divide factor"""
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_term_factor(p):
    """expression : term
       term : factor
       factor : Integer
              | Floating
    """
    p[0] = p[1]

def p_paren_factor(p):
    """factor : LParen expression RParen""" 
    p[0] = p[2]
    

def p_error(p):
    print "Syntax error in input"

parser = yacc.yacc()

s =  "(3 + 4) * 10 + 20 * 2"
result = parser.parse(s)
print result




