
import ply.lex as lex

tokens = (
    "Name",
    "Plus",
    "Minus",
    "Times",
    "Divide",
    "LParen",
    "RParen",
    "Integer",
    "Floating",
    "NewLine",
    "Equal"
)


t_Plus = r'\+'
t_Minus = r'\-'
t_Divide = r'\/'
t_Times = r'\*'

t_LParen = r'\('
t_RParen = r'\)'
t_Name = r'[a-zA-Z]+[a-zA-Z1-9_]+'
t_Equal = r'='
t_NewLine = '\\n'


def t_Floating(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t


def t_Integer(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print "Illegal character " + t.value[0]
    t.lexer.skip(1)
    
lexer = lex.lex() 


import ply.yacc as yacc

class Assign:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
    
    def __str__(self):
        return str(self.name) + " = " + str(self.expr)
        
    def __repr__(self):
        return str(self.name) + " = " + str(self.expr)

def p_var_declaration(p):
    """line :  Name Equal line NewLine line""" 
    p[0] = (Assign(p[1], p[3]),) + p[5]

def p_bin_op(p):
    """expression : expression Plus term
                  |  expression Minus term
       term       : term Times factor
                  | term Divide factor"""
    if p[2] == '+':
        p[0] = (p[1], '+', p[3])
    elif p[2] == '-':
        p[0] = (p[1], '-', p[3])
    elif p[2] == '*':
        p[0] = (p[1], '*', p[3])
    elif p[2] == '/':
        p[0] = (p[1], '/', p[3])


def p_term_factor(p):
    """line : expression
       expression : term
       term : factor
       factor : Integer
              | Floating
    """
    p[0] = p[1]

def p_term_var_name(p):
    """factor : Name"""
    p[0] = p[1]

def p_paren_factor(p):
    """factor : LParen expression RParen""" 
    p[0] = p[2]

    
def p_error(p):
    print "Syntax error in input"

parser = yacc.yacc()

s =  """var = (3.0 + 4) * 10 + 20 * 2
        var1 = 2 + 4.5 + var1
        1 + var"""
result = parser.parse(s)
print result

