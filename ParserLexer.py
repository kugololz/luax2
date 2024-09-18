import ply.lex as lex
import ply.yacc as yacc

# Define reserved words and their corresponding tokens
reserved = {
    'do': 'DO',
    'while': 'WHILE',
    'repeat': 'REPEAT',
    'if': 'IF',
    'then': 'THEN',
    'end': 'END',
    'for': 'FOR',
    'function': 'FUNCTION',
    'local': 'LOCAL',
    'return': 'RETURN',
    'break': 'BREAK',
    'nil': 'NIL',
    'false': 'FALSE',
    'true': 'TRUE',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'until': 'UNTIL',
    'in': 'IN',
    'print': 'PRINT'  # Treat 'print' as a reserved word
}

tokens = list(reserved.values()) + [
    'NAME', 'NUMBER', 'STRING', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'MOD',
    'CONCAT', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE', 'AND', 'OR', 'NOT', 'LEN',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACK', 'RBRACK', 'SEMI', 'COMMA', 'DOT',
    'COLON', 'ASSIGN', 'ELLIPSIS'
]

# Token definitions
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_MOD = r'%'
t_CONCAT = r'\.\.'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'~='
t_AND = r'and'
t_OR = r'or'
t_NOT = r'not'
t_LEN = r'\#'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_SEMI = r';'
t_COMMA = r','
t_DOT = r'\.'
t_COLON = r':'
t_ASSIGN = r'='
t_ELLIPSIS = r'\.\.\.'

def t_NUMBER(t):
    r'\d+(\.\d*)?([eE][+-]?\d+)?'
    t.value = float(t.value) if '.' in t.value or 'e' in t.value.lower() else int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\" | \'([^\\\n]|(\\.))*?\''
    t.value = t.value[1:-1]
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Check if it is a reserved word
    t.type = reserved.get(t.value, 'NAME')  # Check for reserved words
    return t

# Ignore spaces, tabs, and newlines
t_ignore = ' \t'

# Single-line comment rule
def t_SINGLE_COMMENT(t):
    r'--.*'
    pass  # No return value. Token discarded

# Multi-line comment rule
def t_MULTI_COMMENT(t):
    r'\[\[.*?\]\]'
    pass  # No return value. Token discarded

# Rule to handle newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Define operator precedence and associativity
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'),
    ('left', 'CONCAT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'POWER'),
    ('right', 'UNARY'),  # For unary minus, not, length
)

# List of reserved words that should not be redefined as variables
reserved_words = {'print'}

# Symbol Table to track variable and function definitions
symbol_table = {}

def add_to_symbol_table(name, entry_type, lineno):
    # Check if 'name' is a reserved word
    if name in reserved_words:
        print(f"Semantic error: '{name}' cannot be redefined as a variable or function at line {lineno}.")
    elif name in symbol_table:
        print(f"Semantic error: '{name}' already defined at line {symbol_table[name]['line']}.")
    else:
        symbol_table[name] = {'type': entry_type, 'line': lineno}

def check_symbol_table(name, lineno):
    if name not in symbol_table:
        print(f"Semantic error: '{name}' used before declaration at line {lineno}.")
    else:
        print(f"Symbol '{name}' found in symbol table at line {lineno}.")

def p_chunk(p):
    '''chunk : statlist
             | statlist laststat'''
    p[0] = p[1] if len(p) == 2 else p[1] + [p[2]]

def p_statlist(p):
    '''statlist : statlist stat SEMI
                | statlist stat
                | empty'''
    if p[1] == []:
        p[0] = []
    elif len(p) == 4:  # statlist stat SEMI
        p[0] = p[1] + [p[2]]
    elif len(p) == 3:  # statlist stat
        p[0] = p[1] + [p[2]]
    else:  # empty
        p[0] = []

def p_stat(p):
    '''stat : varlist ASSIGN explist
            | functioncall
            | DO block END
            | WHILE exp DO block END
            | REPEAT block UNTIL exp
            | IF exp THEN block elseiflist opt_else END
            | FOR NAME ASSIGN exp COMMA exp opt_comma_exp DO block END
            | FOR namelist IN explist DO block END
            | FUNCTION funcname funcbody
            | LOCAL FUNCTION NAME funcbody
            | LOCAL namelist opt_assign'''
    if p[1] == 'local' and len(p) > 3 and p[2] == 'function':
        add_to_symbol_table(p[3], 'function', p.lineno(3))
    elif p[1] == 'local':
        if len(p) > 3:
            for var in (p[3] if p[3] else []):
                add_to_symbol_table(var, 'local variable', p.lineno(1))
    elif len(p) > 1 and p[2] == '=':
        for var in p[1]:
            check_symbol_table(var, p.lineno(1))
    p[0] = p[1]

def p_laststat(p):
    '''laststat : RETURN opt_explist
                | BREAK'''

def p_funcname(p):
    '''funcname : NAME nameparts opt_colon_name'''
    add_to_symbol_table(p[1], 'function', p.lineno(1))

def p_varlist(p):
    '''varlist : var varlist_tail'''
    p[0] = [p[1]] + (p[2] if p[2] else [])

def p_varlist_tail(p):
    '''varlist_tail : COMMA var varlist_tail
                    | empty'''
    p[0] = [p[2]] + (p[3] if len(p) > 3 else []) if len(p) == 4 else []

def p_var(p):
    '''var : NAME
           | prefixexp LBRACK exp RBRACK
           | prefixexp DOT NAME'''
    if isinstance(p[1], str) and p.slice[1].type == 'NAME':
        check_symbol_table(p[1], p.lineno(1))
    p[0] = p[1]

def p_functioncall(p):
    '''functioncall : NAME LPAREN opt_explist RPAREN
                    | prefixexp COLON NAME args'''
    if p[1] == 'print' and p.slice[1].type == 'NAME' and p[1] in symbol_table:
        print(f"Semantic error: '{p[1]}' is redefined as a variable at line {p.lineno(1)}.")
    elif p[1] not in symbol_table:
        print(f"Semantic error: Undefined function '{p[1]}' called at line {p.lineno(1)}.")

def p_args(p):
    '''args : LPAREN opt_explist RPAREN
            | tableconstructor
            | STRING'''

def p_namelist(p):
    '''namelist : NAME namelist_tail'''
    p[0] = [p[1]] + (p[2] if p[2] else [])

def p_namelist_tail(p):
    '''namelist_tail : COMMA NAME namelist_tail
                     | empty'''
    p[0] = [p[2]] + (p[3] if p[3] else []) if len(p) == 4 else []

def p_explist(p):
    '''explist : exp exp_tail'''
    p[0] = [p[1]] + (p[2] if p[2] else [])

def p_exp_tail(p):
    '''exp_tail : COMMA exp exp_tail
                | empty'''
    p[0] = [p[2]] + (p[3] if p[3] else []) if len(p) == 4 else []

def p_exp(p):
    '''exp : NIL
           | FALSE
           | TRUE
           | NUMBER
           | STRING
           | ELLIPSIS
           | function
           | prefixexp
           | tableconstructor
           | exp binop exp
           | unop exp'''
    # Depending on the type of expression, perform semantic checks if necessary

def p_prefixexp(p):
    '''prefixexp : var
                 | functioncall
                 | LPAREN exp RPAREN'''

def p_function(p):
    '''function : FUNCTION funcbody'''

def p_funcbody(p):
    '''funcbody : LPAREN opt_parlist RPAREN block END'''

def p_parlist(p):
    '''parlist : namelist opt_comma_ellipsis
               | ELLIPSIS'''

def p_tableconstructor(p):
    '''tableconstructor : LBRACE opt_fieldlist RBRACE'''

def p_fieldlist(p):
    '''fieldlist : field field_tail'''

def p_field_tail(p):
    '''field_tail : fieldsep field field_tail
                  | empty'''
    p[0] = [p[2]] + (p[3] if p[3] else []) if len(p) == 4 else []

def p_field(p):
    '''field : LBRACK exp RBRACK ASSIGN exp
             | NAME ASSIGN exp
             | exp'''

def p_fieldsep(p):
    '''fieldsep : COMMA
                | SEMI'''

def p_binop(p):
    '''binop : PLUS
             | MINUS
             | TIMES
             | DIVIDE
             | POWER
             | MOD
             | CONCAT
             | LT
             | LE
             | GT
             | GE
             | EQ
             | NE
             | AND
             | OR'''

def p_unop(p):
    '''unop : MINUS %prec UNARY
            | NOT %prec UNARY
            | LEN %prec UNARY'''

def p_opt_explist(p):
    '''opt_explist : explist
                   | empty'''
    p[0] = p[1] if p[1] else []

def p_opt_comma_exp(p):
    '''opt_comma_exp : COMMA exp
                     | empty'''
    p[0] = [p[2]] if len(p) > 1 else []

def p_opt_assign(p):
    '''opt_assign : ASSIGN explist
                  | empty'''

def p_opt_fieldlist(p):
    '''opt_fieldlist : fieldlist
                     | empty'''

def p_opt_parlist(p):
    '''opt_parlist : parlist
                   | empty'''

def p_opt_else(p):
    '''opt_else : ELSE block
                | empty'''

def p_opt_comma_ellipsis(p):
    '''opt_comma_ellipsis : COMMA ELLIPSIS
                          | empty'''

def p_elseiflist(p):
    '''elseiflist : elseiflist ELSEIF exp THEN block
                  | empty'''

def p_nameparts(p):
    '''nameparts : DOT NAME nameparts
                 | empty'''

def p_opt_colon_name(p):
    '''opt_colon_name : COLON NAME
                      | empty'''

def p_block(p):
    '''block : chunk'''

def p_empty(p):
    '''empty :'''
    p[0] = []

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()


def parse_lua_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read() 

        # Tokenize and parse the data
        lexer.input(data)
        # print("Tokens:")
        # while True:
        #     tok = lexer.token()
        #     if not tok:
        #         break
        #     print(tok)

        print("\nParsing:")
        parser.parse(data)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


filename = input()
parse_lua_file(filename)