%{
#include <stdio.h>
#include <string.h>
#include "parser.tab.h"
%}

%%

[ \t\n]            ;

"soxv" { printf("Operador de adição\n"); return PLUS; }
"plqxv" { printf("Operador de subtração\n"); return MINUS; }
"pxow" { printf("Operador de multiplicação\n"); return MULT; }
"gly" { printf("Operador de divisão\n"); return DIV; }
"htxdo" { printf("Operador de atribuição\n"); return EQUAL; }
"eljjhu" { printf("Operador maior que\n"); return BIGGER; }
"vpdoohu" { printf("Operador menor que\n"); return SMALLER; }
"ru" { printf("Operador lógico OR\n"); return OR; }
"dqg" { printf("Operador lógico AND\n"); return AND; }
"qrw" { printf("Operador lógico NOT\n"); return NOT; }
"frpsduh" { printf("Operador de comparação\n"); return COMPARE; }
"zkloh" { printf("Instrução WHILE\n"); return WHILE; }
"li" { printf("Instrução IF\n"); return IF; }
"uhdg" { printf("Instrução READ\n"); return READ; }
"sulqw" { printf("PRINT:\n"); return PRINT; }
"rshqsdu" { printf("Abertura de parênteses\n"); return OPENPAR; }
"forvhsdu" { printf("Fechamento de parênteses\n"); return CLOSEPAR; }


[0-9]+                         { yylval = atoi(yytext); return INT; }
[a-zA-Z_][_a-zA-Z0-9]          { printf("Identificador: \n"); return IDENTIFIER; }

.                              printf("Token desconhecido!"); yyterminate();


%%

int yywrap() {
  return 1;
}