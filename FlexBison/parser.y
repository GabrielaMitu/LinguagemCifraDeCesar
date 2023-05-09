%{
  #include<stdio.h>
  int yylex();
  void yyerror(const char *s) { printf("ERROR: %s", s); }
%}

%token IDENTIFIER
%token WHILE IF ELSE PRINT READ END
%token EQUAL COMPARE NOT PLUS MINUS MULT DIV AND OR BIGGER SMALLER
%token OPENPAR CLOSEPAR
%token TYPE STRING INT

%start program

%%

program : statementList 
        ;

block : statementList END
      | END
      ;

statementList  : statement
               | statementList statement
               ;

statement : TYPE IDENTIFIER EQUAL relexpression;
          | IDENTIFIER EQUAL relexpression;
          | PRINT OPENPAR relexpression CLOSEPAR          
          | WHILE relexpression statement;
          | IF relexpression block
          | IF relexpression block ELSE block
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

factor  : INT
        | STRING
        | IDENTIFIER    
        | PLUS factor   
        | MINUS factor  
        | NOT factor
        | OPENPAR relexpression CLOSEPAR
        | READ OPENPAR CLOSEPAR
        ;

%%

int main() {
    yyparse();
    return 0;
}