import lexer
import parser
import sys
from sys import argv

if __name__ == '__main__':
    filename = "test.lua"
    f = open(filename)
    code = f.read()
    
    
    #   Start the lexer first
    lexer.lexer.input(code)
    while True:
        tok = lexer.lexer.token()
        if not tok:
            break
        
    if lexer.num_errors > 0:
        sys.exit()
        
    #   Keep the count of the lines of code
    parser.num_lines = lexer.lexer.lineno - 1
    
    #   We start the parser now
    result = parser.parser.parse(code, lexer.lexer, tracking = True)
    
    if parser.num_errors > 0:
        sys.exit()