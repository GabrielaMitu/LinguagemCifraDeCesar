# LogComp-APS
## Linguagem de programação utilizando a criptografia da Cifra de Cesar

## Tradução da criptografia em questão:
![image](https://user-images.githubusercontent.com/49621844/225606246-f7666edf-9c59-4f6c-8e58-e34b2ad4d1d6.png)

E para complementar, os números também serão deslocados, respeitando a seguinte regra:
![image](https://user-images.githubusercontent.com/49621844/226198110-a76e0dc9-3075-449b-b665-13655e9abf16.png)

Sendo os números de cima em cinza os números não criptografados e os de baixo os criptografados

Portanto, a tradução dos operadores em cifra de cesar terá o seguinte formato:

|                |           Tradutor            |       Cifra de Cesar        |
|----------------|-------------------------------|-----------------------------|
|       +        |            plus               |           soxv              |
|       -        |            minus              |           plqxv             |
|       *        |            mult               |           pxow              |
|       /        |            div                |           gly               |
|       //       |            divdiv             |           glygly            |
|       ,        |            comma              |           frppd             |
|       .        |            dot                |           grw               |
|       :        |            colon              |           frorq             |
|       %        |            percent            |           shufhqw           |
|       "        |            Qmarks             |           Tpdunv            |
|       _        |            underline          |           xqghuolqh         |
|       (        |            openP              |           rshqS             |
|       )        |            closeP             |           forvhS            |
|       {        |            OcurlyB            |           RfxuobE           |
|       }        |            CcurlyB            |           FfxuobE           |
|       if       |            if                 |           li                |
|       else     |            else               |           hovh              |
|       not      |            not                |           qrw               |

**Obs.:** Todos os símbolos não numéricos serão interpretados como lidos por extenso. Por exemplo, ao invés de ler "+", "(", "%" etc, serão lidos como "plus", "open parentheses", "percentage", etc.


### EBNF:
    PROGRAM ::= {STATEMENT};

	STATEMENT ::= ASSIGNMENT | PRINT | IF;

	ASSIGNMENT ::= IDENTIFIER 'htxdo' EXPRESSION;

	PRINT ::= "sulqw" 'rshqsS' EXPRESSION 'forvhS';

	IF ::= 'li' EXPRESSION 'frorq' SUITE ['hovh' 'frorq' SUITE];

	SUITE ::= STATEMENT | 'RfxuobE' {statement} 'Ffxuobe';

	EXPRESSION ::= TERM {('soxv'|'plqxv') TERM};

	TERM ::= FACTOR {('pxow'|'gly'|'shufhqw'|'glygly') FACTOR};

	FACTOR ::= IDENTIFIER | NUMBER | STRING | 'rshqsS' EXPRESSION 'forvhS' | 'plqxv' FACTOR | 'qrw' FACTOR | CALL;

	CALL ::= IDENTIFIER 'rshqsS' [ARGS] 'forvhS';

	ARGS ::= EXPRESSION {'frppd' EXPRESSION};

	IDENTIFIER ::= LETTER {LETTER | DIGIT | 'xqghuolqh'};

	NUMBER ::= DIGIT {DIGIT} ['grw' DIGIT {DIGIT}];

	STRING ::= "Tpdunv", (LETTER | DIGIT), "Tpdunv";

	LETTER ::= ( "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" |
	"M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" |
	"Y" | "Z" | "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" |
	"k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" |
	"w" | "x" | "y" | "z" ) ;

	DIGIT ::= ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" ) ;
