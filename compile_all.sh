#!/bin/bash

# Set the file names
YACC_FILE="lua_parser.y"
LEX_FILE="lua_lexer.l"
OUTPUT_EXECUTABLE="lua_compiler"

echo "Generating parser from YACC file..."
yacc -d $YACC_FILE
if [ $? -ne 0 ]; then
  echo "Error: Failed to generate parser."
  exit 1
fi

echo "Generating lexer from FLEX file..."
flex $LEX_FILE
if [ $? -ne 0 ]; then
  echo "Error: Failed to generate lexer."
  exit 1
fi

echo "Compiling YACC output..."
gcc -c y.tab.c
if [ $? -ne 0 ]; then
  echo "Error: Failed to compile YACC output."
  exit 1
fi

echo "Compiling FLEX output..."
gcc -c lex.yy.c
if [ $? -ne 0 ]; then
  echo "Error: Failed to compile FLEX output."
  exit 1
fi

echo "Linking the lexer and parser..."
gcc -o $OUTPUT_EXECUTABLE y.tab.o lex.yy.o -lfl
if [ $? -ne 0 ]; then
  echo "Error: Failed to link lexer and parser."
  exit 1
fi

echo "Compilation successful! You can run ./$OUTPUT_EXECUTABLE with your Lua script."
