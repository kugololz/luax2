import ply.yacc as yacc
from lexer import tokens

symbol_table = {
    'variables': {},  
    'functions': {
        'print': {'params': [], 'return': 'nil'},  
    }
}

num_errors = 0
num_lines = 0
open_parentheses = 0 

precedence = (
    ('nonassoc', 'AND', 'OR'),
    ('nonassoc', 'EQUAL', 'NOTEQUAL'),
    ('nonassoc', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'MOD', 'CONCAT'),  
    ('right', 'UMINUS', 'NOT')  
)

def p_empty(p):
    'empty :'
    pass

def p_program(p):
    '''program : block'''
    p[0] = p[1]

def p_block(p):
    '''block : blocklist'''
    p[0] = p[1]

def p_blocklist(p):
    '''blocklist : command blockterminator blocklist
                 | empty'''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[1]] + p[3]

def p_blockterminator(p):
    '''blockterminator : empty
                       | SEMICOLON'''
    pass

def p_command(p):
    '''command : ID ASSIGN exp
               | functioncall
               | vardeclaration
               | localdeclaration
               | functiondeclaration
               | varassignmultiple
               | WHILE exp DO block END
               | IF exp THEN block elsestnt END
               | RETURN explist'''
    if len(p) == 4:  
        var_name = p[1]
        var_type = p[3] if isinstance(p[3], str) else 'number'  
        symbol_table['variables'][var_name] = var_type
        p[0] = ('assign', var_name, p[3])
    elif len(p) == 8:  
        p[0] = ('while', p[2], p[4])
    elif len(p) == 7:  
        p[0] = ('if', p[2], p[4], p[5])
    else:
        p[0] = p[1]

# Define expassign to resolve the missing symbol error
def p_expassign(p):
    '''expassign : ASSIGN exp
                 | empty'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None

# Handle local variable declaration
def p_localdeclaration(p):
    '''localdeclaration : LOCAL ID expassign'''
    var_name = p[2]
    var_type = 'number'  
    if isinstance(p[3], str):
        var_type = 'string'
    symbol_table['variables'][var_name] = var_type
    p[0] = ('localdeclaration', var_name, p[3])

# Handle multiple variable assignments
def p_varassignmultiple(p):
    '''varassignmultiple : LOCAL ID COMMA ID ASSIGN functioncall'''
    var1 = p[2]
    var2 = p[4]
    symbol_table['variables'][var1] = 'number'
    symbol_table['variables'][var2] = 'number'
    p[0] = ('multiple_assign', var1, var2, p[6])

# Variable declaration with the 'VAR' token
def p_vardeclaration(p):
    '''vardeclaration : VAR ID expassign'''
    var_name = p[2]
    var_type = 'number'
    if isinstance(p[3], str):
        var_type = 'string'
    symbol_table['variables'][var_name] = var_type
    p[0] = ('vardeclaration', var_name, p[3])

def p_functiondeclaration(p):
    '''functiondeclaration : LOCAL FUNCTION ID LPAREN paramlist RPAREN block END'''
    func_name = p[3]
    params = p[5] if p[5] is not None else []
    if func_name in symbol_table['functions']:
        line = (p.lineno(1))/2
        line = int(line)
        print(f"Semantic error at line {line}: Function '{func_name}' already declared")
    symbol_table['functions'][func_name] = {'params': params, 'return': 'number'}
    p[0] = ('functiondeclaration', func_name, params, p[7])

def p_functioncall(p):
    '''functioncall : ID LPAREN explist RPAREN'''
    func_name = p[1]
    args = p[3]
    if func_name not in symbol_table['functions']:
        line = (p.lineno(1))/2
        line = int(line)
        print(f"Semantic error at line {line}: Function '{func_name}' not declared")
    else:
        expected_params = symbol_table['functions'][func_name]['params']
        if len(args) != len(expected_params) and func_name != 'print':
            line = (p.lineno(1))/2
            line = int(line)  
            print(f"Semantic error at line {line}: Function '{func_name}' expects {len(expected_params)} arguments, got {len(args)}")
    p[0] = ('function-call', func_name, args)

def p_paramlist(p):
    '''paramlist : empty
                 | paramseq'''
    p[0] = p[1]

def p_paramseq(p):
    '''paramseq : ID
                | ID COMMA paramseq'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_explist(p):
    '''explist : empty
               | exp
               | exp COMMA explist'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_exp(p):
    '''exp : NUMBER
           | ID
           | STRING
           | functioncall
           | exp PLUS exp
           | exp MINUS exp
           | exp TIMES exp
           | exp DIVIDE exp
           | exp MOD exp
           | exp AND exp
           | exp OR exp
           | exp LESS exp
           | exp LESSEQUAL exp
           | exp GREATER exp
           | exp GREATEREQUAL exp
           | exp EQUAL exp
           | exp NOTEQUAL exp
           | exp CONCAT exp
           | NOT exp
           | MINUS exp %prec UMINUS'''

    if p.slice[1].type == 'ID' and p[1] not in symbol_table['variables'] and p[1] not in symbol_table['functions']:
        line = (p.lineno(1))/2
        line = int(line)
        print(f"Semantic error at line {line}: Variable '{p[1]}' not declared")

    if len(p) == 4 and p[2] in ['+', '-', '*', '/', '%']:
        left_type = 'number' if isinstance(p[1], (int, float)) else symbol_table['variables'].get(p[1], 'number')
        right_type = 'number' if isinstance(p[3], (int, float)) else symbol_table['variables'].get(p[3], 'number')
        if left_type != 'number' or right_type != 'number':
            line = (p.lineno(2))/2
            line = int(line)
            print(f"Semantic error at line {line}: Type mismatch in operation '{p[2]}' between {left_type} and {right_type}")

    p[0] = p[1]

def p_elsestnt(p):
    '''elsestnt : empty
                | ELSE block'''
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = p[2]

def p_error(p):
    global num_errors
    global open_parentheses

    if open_parentheses > 0:
        print("Syntax error: Unclosed parentheses")
        open_parentheses = 0  
    elif p is None:
        print("Syntax error: Unexpected EOF")
    else:
        print(f"Syntax error in input at token '{p.type}' at line: {p.lineno}")

    num_errors += 1

parser = yacc.yacc(start='program', debug=True)
