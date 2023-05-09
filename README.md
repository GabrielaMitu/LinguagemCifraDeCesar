# LogComp-APS
## Linguagem de programação utilizando a criptografia da Cifra de Cesar
A principal razão da criação desta linguagem é a consideração dos aspectos da criptografia e como essa prática pode ser aplicada na programação.

## Tradução da criptografia em questão:
![image](https://user-images.githubusercontent.com/49621844/225606246-f7666edf-9c59-4f6c-8e58-e34b2ad4d1d6.png)

E para complementar, os números também serão deslocados, respeitando a seguinte regra:
![image](https://user-images.githubusercontent.com/49621844/226198110-a76e0dc9-3075-449b-b665-13655e9abf16.png)

Sendo os números de cima em cinza os números não criptografados e os de baixo os criptografados

A tradução dos operadores em cifra de cesar terá o seguinte formato:

|                |           Tradutor            |       Cifra de Cesar        |
|----------------|-------------------------------|-----------------------------|
|       +        |            plus               |           soxv              |
|       -        |            minus              |           plqxv             |
|       *        |            mult               |           pxow              |
|       /        |            div                |           gly               |
|       .        |            dot                |           grw               |
|       (        |            openpar            |           rshqsdu           |
|       )        |            closepar           |           forvhsdu          |
|       if       |            if                 |           li                |
|       else     |            else               |           hovh              |
|       while    |            while              |           zkloh             |
|       read     |            read               |           uhdg              |
|       print    |            print              |           sulqw             |
|       !        |            not                |           qrw               |
|       =        |            equal              |           htxdo             |
|       ==       |            compare            |           frpsduh           |
|       >        |            bigger             |           eljjhu            |
|       <        |            smaller            |           vpdoohu           |
|       &&       |            and                |           dqg               |
|       \|\|     |            or                 |           ru                |
|       Int      |            Int                |           lqw               |
|       String   |            String             |           vwulqj            |



**Obs.:** Todos os símbolos não numéricos serão interpretados como lidos por extenso. Por exemplo, ao invés de ler "+", "(", "%" etc, serão lidos como "plus", "open parentheses", "percentage", etc.


### EBNF:
    PROGRAM ::= statementList;

	BLOCK ::= statementList, END | END

	STATEMENTLIST ::= STATEMENT | STATEMENTLIST, STATEMENT

	STATEMENT ::= TYPE, ASSIGNMENT | ASSIGNMENT | PRINT | WHILE | IF;

	ASSIGNMENT ::= IDENTIFIER, 'htxdo', relexpression;

	PRINT ::= 'sulqw', 'rshqsdu', RELEXPRESSION, 'forvhsdu';

	WHILE = 'zkloh', RELEXPRESSION, STATEMENT;

	IF ::= 'li', RELEXPRESSION BLOCK | 'li', RELEXPRESSION, BLOCK, 'hovh', BLOCK

	RELEXPRESSION ::= EXPRESSION, {('frpsduh'| 'eljjhu' | 'vpdoohu'), EXPRESSION};

	EXPRESSION ::= TERM, {('soxv'|'plqxv'|'ru'), TERM};

	TERM ::= FACTOR, {('pxow'|'gly'|'dqg'), FACTOR};

	FACTOR ::=  INT | STRING | IDENTIFIER | "soxv", FACTOR | "plqxv", FACTOR | "qrw", FACTOR | "rshqsdu", RELEXPRESSION, "forvhsdu" | "uhdg", "rshqsdu", "forvhsdu";

	IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;

	LETTER ::= ( "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" |
	"M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" |
	"Y" | "Z" | "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" |
	"k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" |
	"w" | "x" | "y" | "z" ) ;

	DIGIT ::= ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" ) ;
