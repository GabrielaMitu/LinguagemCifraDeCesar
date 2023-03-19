# LogComp-APS
## Linguagem de programação utilizando a criptografia da Cifra de Cesar

## Tradução da criptografia em questão:
![image](https://user-images.githubusercontent.com/49621844/225606246-f7666edf-9c59-4f6c-8e58-e34b2ad4d1d6.png)

E para complementar, os números também serão deslocados, respeitando a seguinte regra:
![image](https://user-images.githubusercontent.com/49621844/226198110-a76e0dc9-3075-449b-b665-13655e9abf16.png)

Sendo os números de cima em cinza os números não criptografados e os de baixo os criptografados

**Obs.:** Todos os símbolos não numéricos serão interpretados como lidos por extenso. Por exemplo, ao invés de ler "+", "(", "%" etc, serão lidos como "plus", "open parentheses", "percentage", etc.


### EBNF:
PROGRAM ::= {STATEMENT}.

STATEMENT ::= ASSIGNMENT | PRINT | IF.

ASSIGNMENT ::= IDENTIFIER '=' EXPRESSION.

PRINT ::= "print" '(' EXPRESSION ')'.

IF ::= 'if' EXPRESSION ':' SUITE ['else' ':' SUITE].

SUITE ::= STATEMENT | '{' {statement} '}'.

EXPRESSION ::= TERM {('+'|'-') TERM}.

TERM ::= FACTOR {('*'|'/'|'%'|'//') FACTOR}.

FACTOR ::= IDENTIFIER | NUMBER | STRING | '(' EXPRESSION ')' | '-' FACTOR | 'not' FACTOR | CALL.

CALL ::= IDENTIFIER '(' [ARGS] ')'.

ARGS ::= EXPRESSION {',' EXPRESSION}.

IDENTIFIER ::= LETTER {LETTER | DIGIT | '_'}.

NUMBER ::= DIGIT {DIGIT} ['.' DIGIT {DIGIT}].

STRING ::= """, (LETTER | DIGIT), """.

LETTER ::= ( "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" |
"M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" |
"Y" | "Z" | "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" |
"k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" |
"w" | "x" | "y" | "z" ) ;

DIGIT ::= ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" ) ;
