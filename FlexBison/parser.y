%{
  #include<stdio.h>
  int yylex();
  void yyerror(const char *s) { printf("ERROR: %s", s); }
%}

%token IDENTIFIER INT
%token WHILE IF ELSE PRINT READ
%token EQUAL COMPARE NOT PLUS MINUS MULT DIV AND OR BIGGER SMALLER
%token OPENPAR CLOSEPAR

%start program

%%

program : block 
        ;

block : statement
      | block statement
      ;

statement : assigment
          | print
          | while
          | if
          ;

relexpression: expression COMPARE expression
             | expression BIGGER expression
             | expression SMALLER expression
             | expression
             ;

expression: term PLUS term
          | term MINUS term
          | term OR term
          | term
          ;

term: factor
    | factor MULT factor
    | factor DIV factor
    | factor AND factor
    ;

factor: INT         { printf("INT: %d\n", yylval); $$ = yylval; }
    | IDENTIFIER    
    | PLUS factor   
    | MINUS factor  
    | NOT factor
    | OPENPAR relexpression CLOSEPAR
    | READ OPENPAR CLOSEPAR
    ;

while: WHILE relexpression statement;
if: IF relexpression statement else | IF relexpression statement;
assigment: IDENTIFIER EQUAL relexpression;
print: PRINT OPENPAR relexpression CLOSEPAR;
else: ELSE statement;

%%

int main() {
    yyparse();
    return 0;
}