%{
#include <stdio.h>
#include <string.h>
#include "parser.tab.h"

int position = 0;

%}

%%

[ \t\n]            ;

"soxv"          { printf("Operador de adicao: %s\n", yytext); position++; return PLUS; }
"plqxv"         { printf("Operador de subtracao: %s\n", yytext); position++; return MINUS; }
"pxow"          { printf("Operador de multiplicacao: %s\n", yytext); position++; return MULT; }
"gly"           { printf("Operador de divisao: %s\n", yytext); position++; return DIV; }
"htxdo"         { printf("Operador de atribuicao: %s\n", yytext); position++; return EQUAL; }
"eljjhu"        { printf("Operador maior que: %s\n", yytext); position++; return BIGGER; }
"vpdoohu"       { printf("Operador menor que: %s\n", yytext); position++; return SMALLER; }
"ru"            { printf("Operador OR: %s\n", yytext); position++; return OR; }
"dqg"           { printf("Operador AND: %s\n", yytext); position++; return AND; }
"qrw"           { printf("Operador NOT: %s\n", yytext); position++; return NOT; }
"frpsduh"       { printf("Operador de comparacao: %s\n", yytext); position++; return COMPARE; }
"zkloh"         { printf("Instrucao WHILE: %s\n", yytext); position++; return WHILE; }
"li"            { printf("Instrucao IF: %s\n", yytext); position++; return IF; }
"hovh"          { printf("Instrucao ELSE: %s\n", yytext); position++; return ELSE; }
"uhdg"          { printf("Instrucao READ: %s\n", yytext); position++; return READ; }
"sulqw"         { printf("PRINT: %s\n", yytext); position++; return PRINT; }
"rshqsdu"       { printf("Abertura de parenteses: %s\n", yytext); position++; return OPENPAR; }
"forvhsdu"      { printf("Fechamento de parenteses: %s\n", yytext); position++; return CLOSEPAR; }
"hqg"           { printf("END: %s\n", yytext); position++; return END; }
"ixqfwlrq"      { printf("Instrução de Função: %s\n", yytext); position++; return FUNCTION; }
"uhwxuq"        { printf("Instrução de Return: %s\n", yytext); position++; return RETURN; }
"frppd"         { printf("Instrução de vírgula: %s\n", yytext); position++; return COMMA; }  
"wbsh"          { printf("Instrução de Type: %s\n", yytext); position++; return TYPE_REF; }
"grw"           { printf("Instrução de Type: %s\n", yytext); position++; return CONCAT; }


"lqw"           { printf("Int(type)\n"); position++; return TYPE;}
"vwulqj"        { printf("String(type)\n"); position++; return TYPE;}


\"([^\\\n]|(\\.))*\"           { printf("String: %s\n", yytext); position++; return STRING;}
[0-9]+                         { printf("Integer: %s\n", yytext); position++; return INT; }
[a-zA-Z_][a-zA-Z_0-9]*         { printf("Identificador: %s\n", yytext); position++; return IDENTIFIER; }

.                              { printf("Token desconhecido!"); position++; yyterminate(); }


%%

int yywrap() {
  return 1;
}

