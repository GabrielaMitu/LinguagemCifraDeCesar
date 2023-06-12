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
|       ,        |            comma              |           frppd             |
|       (        |            openpar            |           rshqsdu           |
|       )        |            closepar           |           forvhsdu          |
|       if       |            if                 |           li                |
|       else     |            else               |           hovh              |
|       end      |            end                |           hqg               |
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
|       return   |            return             |           uhwxuq            |
|       function |            function           |           ixqfwlrq          |
|       ::       |            type               |           wbsh              |


**Obs.:** Todos os símbolos não numéricos serão interpretados como lidos por extenso. Por exemplo, ao invés de ler "+", "(", "%" etc, serão lidos como "plus", "open parentheses", "percentage", etc.


### EBNF:
	BLOCK ::= statement | END

	STATEMENT ::=  ( λ | ASSIGNMENT, ( "htxdo", RELEXPRESSION | "rshqsdu", "RELEXPRESSION", (λ | "frppd"), "forvhsdu" ) | RETURN, RELEXPRESSION | PRINT | WHILE | IF | FUNCTION), "\n" ;

	ASSIGNMENT ::= IDENTIFIER, 'htxdo', relexpression | IDENTIFIER, "wbsh", TYPE;

	PRINT ::= 'sulqw', 'rshqsdu', RELEXPRESSION, 'forvhsdu';

	WHILE = 'zkloh', RELEXPRESSION, STATEMENT;

	IF ::= 'li', RELEXPRESSION BLOCK | 'li', RELEXPRESSION, BLOCK, 'hovh', BLOCK

	RELEXPRESSION ::= EXPRESSION, {('frpsduh'| 'eljjhu' | 'vpdoohu' | 'grw'), EXPRESSION};

	EXPRESSION ::= TERM, {('soxv'|'plqxv'|'ru'), TERM};

	TERM ::= FACTOR, {('pxow'|'gly'|'dqg'), FACTOR};

	FACTOR ::=  INT | STRING | IDENTIFIER | "soxv", FACTOR | "plqxv", FACTOR | "qrw", FACTOR | "rshqsdu", RELEXPRESSION, "forvhsdu" | "uhdg", "rshqsdu", "forvhsdu";

	IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
	
	FUNCTION = IDENTIFIER , "rshqsdu" , ( λ | IDENTIFIER, "wbsh", TYPE ( λ | "frppd" )), "forvhsdu", "wbsh", TYPE, "\n", STATEMENT
	
	NUMBER = DIGIT, { DIGIT } ;

	TYPE = STRING | INT ;

	LETTER ::= ( "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" |
	"M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" |
	"Y" | "Z" | "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" |
	"k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" |
	"w" | "x" | "y" | "z" ) ;

	DIGIT ::= ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" ) ;

## Como rodar o compilador

	python main.py input.ccl

## Como testar em Flex e Bison

	flex tokens.l
	bison -d -t parser.y
	gcc lex.yy.c parser.tab.c
	a < teste.txt

## Exemplos de testes

#### If/Else

	li y eljjhu x
	    sulqw rshqsdu "khoor zruog" forvhsdu
	    hqg

	li x eljjhu y
	    sulqw rshqsdu "qrw jrrg" forvhsdu
	    hqg
	hovh
	    sulqw rshqsdu x soxv y forvhsdu
	    hqg

#### While

	zkloh rshqsdu rshqsdu x_1 eljjhu 6 forvhsdu ru rshqsdu x_1 frpsduh 6 forvhsdu forvhsdu 
	    x_1 htxdo x_1 plqxv 6
	    sulqw rshqsdu x_1 forvhsdu
	hqg

#### Função

	ixqfwlrq vrpd rshqsdu a wbsh lqw frppd b wbsh lqw forvhsdu wbsh lqw
		uhwxuq a soxv b
	hqg

	z wbsh lqw htxdo vrpd rshqsdu 1 frppd 2 forvhsdu
	
#### Teste geral

	sulqw rshqsdu 5 forvhsdu

	x wbsh lqw htxdo 2
	y wbsh lqw 
	y htxdo 3

	li y eljjhu x
	    sulqw rshqsdu "khoor zruog" forvhsdu
	    hqg

	li x eljjhu y
	    sulqw rshqsdu "qrw jrrg" forvhsdu
	    hqg
	hovh
	    sulqw rshqsdu x soxv y forvhsdu
	    hqg

	ixqfwlrq vrpd rshqsdu a wbsh lqw frppd b wbsh lqw forvhsdu wbsh lqw
		uhwxuq a soxv b
	hqg

	z wbsh lqw htxdo vrpd rshqsdu 1 frppd 2 forvhsdu
