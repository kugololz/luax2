import ply.lex as lex

num_errors = 0

reserved = {
    'and'   : 'AND',
    'do'    : 'DO',
    'else'  : 'ELSE',
    'while' : 'WHILE',
    'then'  : 'THEN',
    'end'   : 'END',
    'if'    : 'IF',
    'var'   : 'VAR',
    'or'    : 'OR',
    'not'   : 'NOT',
    'local' : 'LOCAL',
    'function' : 'FUNCTION',
    'return' : 'RETURN'
}

tokens = [
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUAL', 'NOTEQUAL', 'LESSEQUAL', 'GREATEREQUAL',
    'LESS', 'GREATER', 'ASSIGN', 'LPAREN', 'RPAREN',
    'SEMICOLON', 'COMMA', 'MOD', 'CONCAT', 'STRING'
] + list(reserved.values())

t_PLUS          = r'\+'
t_MINUS         = r'-'
t_TIMES         = r'\*'
t_DIVIDE        = r'/'
t_EQUAL         = r'=='
t_NOTEQUAL      = r'~='
t_LESSEQUAL     = r'<='
t_GREATEREQUAL  = r'>='
t_LESS          = r'<'
t_GREATER       = r'>'
t_ASSIGN        = r'='
t_LPAREN        = r'\('
t_RPAREN        = r'\)'
t_SEMICOLON     = r';'
t_COMMA         = r','
t_MOD           = r'%'          
t_CONCAT        = r'\.\.'       

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = str(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENT_SINGLELINE(t):
    r'--[^\n]*'
    pass  

def t_COMMENT_MULTILINE(t):
    r'--\[\[.*?\]\]'
    pass  

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    global num_errors
    print ("Illegal character '%s' at line: %d" % (t.value[0], t.lexer.lineno))
    num_errors += 1
    t.lexer.skip(1)

lexer = lex.lex()
