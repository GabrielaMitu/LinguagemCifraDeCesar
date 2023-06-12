%{
  #include<stdio.h>
  int yylex();
  void yyerror(const char *s) { printf("ERROR: %s", s); }
%}

%token IDENTIFIER
%token WHILE IF ELSE PRINT READ END
%token EQUAL COMPARE NOT PLUS MINUS MULT DIV AND OR BIGGER SMALLER CONCAT
%token OPENPAR CLOSEPAR
%token TYPE STRING INT TYPE_REF
%token FUNCTION RETURN COMMA 

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

statement : IDENTIFIER TYPE_REF TYPE EQUAL relexpression
          | IDENTIFIER TYPE_REF TYPE
          | IDENTIFIER EQUAL relexpression
          | IDENTIFIER OPENPAR parameterList CLOSEPAR
          | PRINT OPENPAR printList CLOSEPAR
          | WHILE relexpression statement block
          | IF relexpression block
          | IF relexpression block ELSE block
          | FUNCTION IDENTIFIER OPENPAR parameterList CLOSEPAR TYPE_REF TYPE block
          | RETURN relexpression
          ;

parameterList : IDENTIFIER TYPE_REF TYPE
              | parameterList COMMA IDENTIFIER TYPE_REF TYPE
              | parameterList COMMA IDENTIFIER 
              | COMMA relexpression 
              | IDENTIFIER
              ;

printList : relexpression
          | printList COMMA relexpression
          ;

relexpression: expression COMPARE expression
             | expression BIGGER expression
             | expression SMALLER expression
             | expression CONCAT expression
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
        | IDENTIFIER OPENPAR relexpression parameterList CLOSEPAR
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