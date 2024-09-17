/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    AND = 258,                     /* AND  */
    BREAK = 259,                   /* BREAK  */
    DO = 260,                      /* DO  */
    ELSE = 261,                    /* ELSE  */
    ELSEIF = 262,                  /* ELSEIF  */
    END = 263,                     /* END  */
    FALSE = 264,                   /* FALSE  */
    FOR = 265,                     /* FOR  */
    FUNCTION = 266,                /* FUNCTION  */
    IF = 267,                      /* IF  */
    IN = 268,                      /* IN  */
    LOCAL = 269,                   /* LOCAL  */
    NIL = 270,                     /* NIL  */
    NOT = 271,                     /* NOT  */
    OR = 272,                      /* OR  */
    REPEAT = 273,                  /* REPEAT  */
    RETURN = 274,                  /* RETURN  */
    THEN = 275,                    /* THEN  */
    TRUE = 276,                    /* TRUE  */
    UNTIL = 277,                   /* UNTIL  */
    WHILE = 278,                   /* WHILE  */
    PRINT = 279,                   /* PRINT  */
    IDENTIFIER = 280,              /* IDENTIFIER  */
    STRING = 281,                  /* STRING  */
    NUMBER = 282,                  /* NUMBER  */
    EQ = 283,                      /* EQ  */
    NEQ = 284,                     /* NEQ  */
    LEQ = 285,                     /* LEQ  */
    GEQ = 286,                     /* GEQ  */
    CONCAT = 287                   /* CONCAT  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif
/* Token kinds.  */
#define YYEMPTY -2
#define YYEOF 0
#define YYerror 256
#define YYUNDEF 257
#define AND 258
#define BREAK 259
#define DO 260
#define ELSE 261
#define ELSEIF 262
#define END 263
#define FALSE 264
#define FOR 265
#define FUNCTION 266
#define IF 267
#define IN 268
#define LOCAL 269
#define NIL 270
#define NOT 271
#define OR 272
#define REPEAT 273
#define RETURN 274
#define THEN 275
#define TRUE 276
#define UNTIL 277
#define WHILE 278
#define PRINT 279
#define IDENTIFIER 280
#define STRING 281
#define NUMBER 282
#define EQ 283
#define NEQ 284
#define LEQ 285
#define GEQ 286
#define CONCAT 287

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 11 "lua_parser.y"

    int intval;
    char *str;

#line 136 "y.tab.h"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
