import sys
import re

# ---------- Árvore sintática abstrata (AST) -----------------

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbolTable):
        pass

class BinOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbolTable):
        n0 = self.children[0].evaluate(symbolTable)
        n1 = self.children[1].evaluate(symbolTable)
        if (n0[0] == "lqw" and n1[0] == "lqw"):
            if self.value == '+':
                return ("lqw", n0[1] + n1[1])
            elif self.value == '-':
                return ("lqw", n0[1] - n1[1])
            elif self.value == '*':
                return ("lqw", n0[1] * n1[1])
            elif self.value == "gly":
                return ("lqw", n0[1] // n1[1])
            elif self.value == "dqg":
                return ("lqw", n0[1] and n1[1])
            elif self.value == "ru":
                return ("lqw", n0[1] or n1[1])
            elif self.value == "eljjhu":
                return ("lqw", int(n0[1] > n1[1]))
            elif self.value == "vpdoohu":
                return ("lqw", int(n0[1] < n1[1]))
            elif self.value == '==':
                return ("lqw", int(n0[1] == n1[1]))
            elif self.value == "grw":
                result = str(str(n0[1]) + str(n1[1]))
                return ("vwulqj", str(result))
            else:
                raise Exception("Error")
        elif (n0[0] == "vwulqj" and n1[0] == "vwulqj"):
            if self.value == "grw":
                result = str(str(n0[1]) + str(n1[1]))
                return ("vwulqj", str(result))
            elif self.value == "eljjhu":
                return ("lqw", int(n0[1] > n1[1]))
            elif self.value == "vpdoohu":
                return ("lqw", int(n0[1] < n1[1]))
            elif self.value == '==':
                return ("lqw", int(n0[1] == n1[1]))
            else:
                raise Exception("Error")
        elif (n0[0] == "vwulqj" or n1[0] == "vwulqj"):
            if self.value == "grw":
                return ("vwulqj", str(str(n0[1]) + str(n1[1])))
            elif self.value == "frpsduh":
                return ("lqw", int(n0[0] == n1[0]))
            else:
                raise Exception("Error")
        else:
            raise Exception("Error")

class UnOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbolTable):
        n0 = self.children[0].evaluate(symbolTable)
        if self.value == "-":
            return ("lqw", -n0[1])
        elif self.value == "!":
            return ("lqw", not(n0[1]))
        return ("lqw", n0[1])

class NoOp(Node):
    def evaluate(self, symbolTable):
        pass

class Identifier(Node):
    def __init__(self, value):
        self.value = value
    def evaluate(self, symbolTable):
        var = symbolTable.getter(self.value)
        return (var[0], var[1])

class Print(Node):
    def __init__(self, value, children):
        self.value = value
        self.child = children

    def evaluate(self, symbolTable):
        #print("print: ", self.child.evaluate(symbolTable)[1])
        vCriptografado = self.child.evaluate(symbolTable)[1]
        if (vCriptografado == 0):
            vCriptografado = 5
        elif (vCriptografado == 1):
            vCriptografado = 6
        elif (vCriptografado == 2):
            vCriptografado = 7
        elif (vCriptografado == 3):
            vCriptografado = 8
        elif (vCriptografado == 4):
            vCriptografado = 9
        elif (vCriptografado == 5):
            vCriptografado = 0
        elif (vCriptografado == 6):
            vCriptografado = 1
        elif (vCriptografado == 7):
            vCriptografado = 2
        elif (vCriptografado == 8):
            vCriptografado = 3
        elif (vCriptografado == 9):
            vCriptografado = 4
        print(vCriptografado)

class Assignment(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children 
        
    def evaluate(self, symbolTable):
        symbolTable.setter(self.children[0].value, self.children[1].evaluate(symbolTable))

class VarDec(Node):
    def __init__(self, value, children):
        self.value = value 
        self.children = children

    def evaluate(self, symbolTable):
        symbolTable.create(self.children[0].value, self.children[1].evaluate(symbolTable))

class StrVal(Node):
    def __init__(self, value):
        self.value = value 

    def evaluate(self, symbolTable):
        return ["vwulqj", self.value]
    
class IntVal(Node):

    def __init__(self, value):
        self.value = value 

    def evaluate(self, symbolTable):
        return ["lqw", self.value]

class Block(Node):
    def __init__(self, children):
        self.value = "Block"
        self.children = children

    def evaluate(self, symbolTable):
        for child in self.children:
            if type(child) == Return:
                return child.evaluate(symbolTable)
            child.evaluate(symbolTable)
            
class Read(Node):
    def evaluate(self, symbolTable):
        return ("lqw", int(input()))
    
class While(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbolTable):        
        n0 = self.children[0]
        n1 = self.children[1]
        while (n0.evaluate(symbolTable)[1]):
            n1.evaluate(symbolTable)
            
class If(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbolTable):
        if self.children[0].evaluate(symbolTable):
            self.children[1].evaluate(symbolTable)
        elif len(self.children) > 2:
            self.children[2].evaluate(symbolTable)

# ---------- Tables ----------------------

class SymbolTable:
    def __init__(self):
        self.symbol_table = {}

    def create(self, key, value):
        if key in self.symbol_table:
            raise Exception("Error")
        self.symbol_table[key] = value        

    def getter(self, key):
        return self.symbol_table[key]
    
    def setter(self, key, value):
        if key not in self.symbol_table:
            raise Exception("Error")
        
        if(self.symbol_table[key][0] == value[0]):
            self.symbol_table[key] = value

        else:
            raise Exception("Error")

class FuncTable:
    def __init__(self):
        self.table = {}

    def create(self, key, value):
        if(key in self.table.keys()):
            raise Exception("Error")
        self.table[key] = value       

    def getter(self, key):
        return self.table[key]
    
    def setter(self, key, value):
        if key not in self.table:
            raise Exception("Error")
            
        self.table[key] = value

funcTable = FuncTable()

# ---------- Funcs ----------------------

class FuncDec(Node):
    def __init__(self, value, children):
        self.value = value # type
        self.children = children # ident, args (VarDecs) and block

    def evaluate(self, symbolTable):
        funcTable.create(self.children[0], self.value[1])
        funcTable.setter(self.children[0], self)

class FuncCall(Node):
    def __init__(self, value, children):
        self.value = value 
        self.children = children        

    def evaluate(self, symbolTable):
        func = funcTable.getter(self.value)
        self.FuncST = SymbolTable()

        if len(self.children) == len(func.children[1]):
            if len(self.children) == 0:
                return func.children[2].evaluate(self.FuncST)        
            
            else:
                var_names = []
                for i in range(len(func.children[1])):
                    func.children[1][i].evaluate(self.FuncST)
                    var_names.append(func.children[1][i].children[0].value)

                for j in range(len(self.children)):
                    self.FuncST.setter(var_names[j], self.children[j].evaluate(symbolTable))

                return func.children[2].evaluate(self.FuncST)     
        else:
            raise Exception("Error")


class Return(Node):
    def __init__(self, value, child):
        self.value = value
        self.child = child

    def evaluate(self, symbolTable):
        return self.child.evaluate(symbolTable)

# ---------- Diagrama Sintático -----------------

class Token:
    def __init__(self, value, type):
        self.value = value
        self.type = type

class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.position = 0 
        self.next = Token(None, None)

    def selectNext(self):
        keywords = ["sulqw", "hovh", "li", "uhdg", "zkloh", "hqg", "vwulqj", "lqw", "uhwxuq", "ixqfwlrq", "soxv", "plqxv", "pxow", "gly", "qrw", "eljjhu", "vpdoohu", "rshqsdu", "ru", "dqg", "frppd", "htxdo", "wbsh", "frpsduh", "grw", "rshqsdu", "forvhsdu", "tpdunv"]

        while self.position < len(self.source) and self.source[self.position] == " ":
             self.position+=1

        if self.position >= len(self.source):
            self.next = Token("", "EOF")

        elif self.source[self.position].isalpha(): # ve se o prox conjunto de caracteres corresponde a uma keyword
            word = ""
            while self.position < len(self.source) and (self.source[self.position].isalpha() or self.source[self.position].isdigit() or self.source[self.position] == "_"):
                word += self.source[self.position]
                self.position += 1
            if word in keywords:
                if word == "sulqw":
                    self.next = Token("sulqw", "PRINTLN")
                elif word == "hovh":
                    self.next = Token("hovh", "ELSE")
                elif word == "li":
                    self.next = Token("li", "IF")
                elif word == "uhdg":
                    self.next = Token("uhdg", "READ")
                elif word == "zkloh":
                    self.next = Token("zkloh", "WHILE")
                elif word == "hqg":
                    self.next = Token("hqg", "END")
                elif word == "vwulqj":
                    self.next = Token("vwulqj", "TYPE")
                elif word == "lqw":
                    self.next = Token("lqw", "TYPE")
                elif word == "ixqfwlrq":
                    self.next = Token("ixqfwlrq", "FUNCTION")
                elif word == "uhwxuq":
                    self.next = Token("uhwxuq", "RETURN")
                elif word == "soxv":
                    self.next = Token("+", "PLUS")
                elif word == "plqxv":
                    self.next = Token("-", "MINUS")
                elif word == "pxow":
                    self.next = Token("*", "MULT")
                elif word == "gly":
                    self.next = Token("/", "DIV")
                elif word == "qrw":
                    self.next = Token("!", "NOT")
                elif word == "eljjhu":
                    self.next = Token(">", "BIGGER")
                elif word == "vpdoohu":
                    self.next = Token("<", "SMALLER")
                elif word == "ru":
                    self.next = Token("||", "OR")
                elif word == "dqg":
                    self.next = Token("&&", "AND")
                elif word == "frppd":
                    self.next = Token(",", "COMMA") 
                elif word == "htxdo":
                    self.next = Token("=", "EQUAL")
                elif word == "wbsh":
                    self.next = Token("::", "TYPE_REF")
                elif word == "frpsduh":
                    self.next = Token("==", "COMPARE")
                elif word == "grw":
                    self.next = Token(".", "CONCAT")
                elif word == "rshqsdu":
                    self.next = Token("rshqsdu", "OPENPAR")
                elif word == "forvhsdu":
                    self.next = Token("forvhsdu", "CLOSEPAR")
            else:
                self.next = Token(word, "IDENTIFIER") # guarda variavel
        elif self.source[self.position].isdigit():
            value = 0
            while self.position < len(self.source) and self.source[self.position].isdigit():
                valor_cifra = int(self.source[self.position])
                #print("valor_cifra: ", valor_cifra)
                if (valor_cifra == 0):
                    valor_cifra = 5
                elif (valor_cifra == 1):
                    valor_cifra = 6
                elif (valor_cifra == 2):
                    valor_cifra = 7
                elif (valor_cifra == 3):
                    valor_cifra = 8
                elif (valor_cifra == 4):
                    valor_cifra = 9
                elif (valor_cifra == 5):
                    valor_cifra = 0
                elif (valor_cifra == 6):
                    valor_cifra = 1
                elif (valor_cifra == 7):
                    valor_cifra = 2
                elif (valor_cifra == 8):
                    valor_cifra = 3
                elif (valor_cifra == 9):
                    valor_cifra = 4
                value = value*10 + valor_cifra
                self.position += 1
            self.next = Token(value, "INT")
        elif self.source[self.position] == '"':
            string = ""
            self.position += 1
            while self.source[self.position] != '"':
                string += self.source[self.position]
                self.position += 1
            self.next = Token(string, "STRING")
            self.position += 1
        elif self.source[self.position] == "\n":
            self.next = Token("\n", "ENTER")
            self.position += 1
        return self.next


class PrePro:
    def filter(s):
        filtered_string = re.sub(r'#.*', '', s) # "#.*" é usada como padrão de substituição para remover qualquer coisa que comece com o caractere
        if len(filtered_string) <= 0:
            raise Exception("Error")
        return filtered_string
    
class Parser: # semantico
    tokenizer = None

    def parseBlock(tokenizer):
        statements = []
        while tokenizer.next.type != 'EOF':
            statements.append(Parser.parseStatement(tokenizer))
        node = Block(statements)
        return node
    
    def parseStatement(tokenizer):
        node = NoOp(None, None)
        if tokenizer.next.type == 'IDENTIFIER':
            variable = Identifier(tokenizer.next.value)
            tokenizer.selectNext() 
            if tokenizer.next.type == 'TYPE_REF':
                tokenizer.selectNext()
                if tokenizer.next.type == 'TYPE':
                    Type = tokenizer.next.value
                    tokenizer.selectNext()
                    if Type == "lqw":
                        node = VarDec([Type, 0], [variable, IntVal(0)])
                    elif Type == "vwulqj":
                        node = VarDec([Type, ''], [variable, StrVal('')])
                    if tokenizer.next.type == 'EQUAL':
                        tokenizer.selectNext()
                        node.children[1] = Parser.parseRelExpression(tokenizer)
            
            elif tokenizer.next.type == 'EQUAL':
                tokenizer.selectNext()
                node = Assignment(tokenizer.next.value, [variable, Parser.parseRelExpression(tokenizer)])

        elif tokenizer.next.type == 'RETURN':
            tokenizer.selectNext()
            node = Return("Return", Parser.parseRelExpression(tokenizer))
        
        elif tokenizer.next.type == 'PRINTLN':
            tokenizer.selectNext()
            if tokenizer.next.type != 'OPENPAR':
                raise Exception("Error")
            tokenizer.selectNext()
            node = Print(node, Parser.parseRelExpression(tokenizer))
            if tokenizer.next.type == 'CLOSEPAR':
                tokenizer.selectNext()
            else:
                raise Exception("Error")
        
        elif tokenizer.next.type == 'WHILE' or tokenizer.next.type == 'IF':
            if tokenizer.next.type == 'IF':                 
                tokenizer.selectNext()
                child0 = Parser.parseRelExpression(tokenizer)
                if tokenizer.next.type == 'ENTER':
                    tokenizer.selectNext()
                    statement = []
                    while tokenizer.next.value != 'hqg' and tokenizer.next.value != "hovh":            
                        statement.append(Parser.parseStatement(tokenizer))
                    if tokenizer.next.value == 'hqg':
                        tokenizer.selectNext()
                    else:
                        raise Exception("Error")
                    tokenizer.selectNext()
                    child1 = Block(statement)
                    if tokenizer.next.type == 'ELSE':
                        tokenizer.selectNext()
                        if tokenizer.next.type == 'ENTER':
                            tokenizer.selectNext()
                            statement2 = []
                            while tokenizer.next.value != 'hqg':
                                statement2.append(Parser.parseStatement(tokenizer))
                            child2 = Block(statement2)
                            node = If(tokenizer.next.value, [child0, child1, child2])
                        else:
                            raise Exception("Error")
                    else:
                        node = If(tokenizer.next.value, [child0, child1])
                else:
                    raise Exception("Error")

            elif tokenizer.next.type == 'WHILE':
                tokenizer.selectNext()
                child0 = Parser.parseRelExpression(tokenizer)
                if tokenizer.next.type == 'ENTER':
                    tokenizer.selectNext()
                    statement = []
                    while tokenizer.next.type != 'END':
                        statement.append(Parser.parseStatement(tokenizer))
                        if tokenizer.next.type == 'EOF':
                            raise Exception("Error")
                    child1 = Block(statement)
                    node = While(tokenizer.next.value, [child0, child1])
                else:
                    raise Exception("Error")
            if tokenizer.next.value == 'hqg':
                tokenizer.selectNext()

        if tokenizer.next.type == "FUNCTION":
            tokenizer.selectNext()
            if tokenizer.next.type == "IDENTIFIER":
                funcName = tokenizer.next.value
                tokenizer.selectNext()
                if tokenizer.next.type == "OPENPAR":
                    tokenizer.selectNext()
                    if tokenizer.next.type == "CLOSEPAR":
                        tokenizer.selectNext()
                        if tokenizer.next.type == 'TYPE_REF':
                            tokenizer.selectNext()
                            if tokenizer.next.type != "TYPE":
                                raise Exception("Error")
                            funcType = tokenizer.next.value
                            tokenizer.selectNext()
                            if tokenizer.next.type != 'ENTER':
                                raise Exception("Error")
                            tokenizer.selectNext()                                    
                            statement = []
                            while tokenizer.next.type != "END":
                                statement_parser = Parser.parseStatement(tokenizer)                                            
                                statement.append(statement_parser)
                                if tokenizer.next.type == "EOF":
                                    raise Exception('need a new line after ixqfwlrq expression!')
                            if tokenizer.next.type == "END":
                                tokenizer.selectNext()
                                node = FuncDec(funcType, [funcName, [], Block(statement)])
                    elif tokenizer.next.type != "CLOSEPAR":
                        args = []
                        while tokenizer.next.type != "CLOSEPAR":
                            if tokenizer.next.type == "IDENTIFIER":
                                variable = Identifier(tokenizer.next.value)
                                tokenizer.selectNext()
                                if tokenizer.next.type != 'TYPE_REF':
                                    raise Exception("Error")
                                tokenizer.selectNext()
                                if tokenizer.next.type != "TYPE":
                                    raise Exception("Error")
                                Type = tokenizer.next.value
                                tokenizer.selectNext()
                                if Type == "lqw":
                                    vardec = VarDec([Type, 0], [variable, IntVal(0)])
                                elif Type == "vwulqj":
                                    vardec = VarDec([Type, ''], [variable, StrVal('')])
                                args.append(vardec)
                                if tokenizer.next.type == "COMMA":
                                    tokenizer.selectNext()                                            
                                elif tokenizer.next.type == "CLOSEPAR":
                                    break
                                else:
                                    raise Exception("Error")

                        if tokenizer.next.type == "CLOSEPAR":
                            tokenizer.selectNext()
                            if tokenizer.next.type == 'TYPE_REF':
                                tokenizer.selectNext()
                                if tokenizer.next.type != "TYPE":
                                    raise Exception("Error")
                                funcType = tokenizer.next.value
                                tokenizer.selectNext()                                    
                                if tokenizer.next.type != 'ENTER':
                                    raise Exception("Error")
                                tokenizer.selectNext()                                        
                                statement = []
                                while tokenizer.next.type != "END":
                                    statement_parser = Parser.parseStatement(tokenizer)                                            
                                    statement.append(statement_parser)
                                    if tokenizer.next.type == "EOF":
                                        raise Exception("Error")
                                if tokenizer.next.type == "END":
                                    tokenizer.selectNext()
                                    node = FuncDec(funcType, [funcName, args, Block(statement)])
              
        if tokenizer.next.type == 'ENTER':
            tokenizer.selectNext()
            return node
        if tokenizer.next.type == 'EOF':
            return node
    
        else:
            raise Exception("Error")

    def parseRelExpression(tokenizer):
        node = Parser.parseExpression(tokenizer)
        while tokenizer.next.type == "COMPARE" or tokenizer.next.type == "BIGGER" or tokenizer.next.type == "SMALLER" or tokenizer.next.type == "CONCAT":
            if tokenizer.next.type == "COMPARE":
                tokenizer.selectNext() 
                node = BinOp('==', [node, Parser.parseExpression(tokenizer)])
            elif tokenizer.next.type == "BIGGER":
                tokenizer.selectNext() 
                node = BinOp("eljjhu", [node, Parser.parseExpression(tokenizer)])
            elif tokenizer.next.type == "SMALLER":
                tokenizer.selectNext() 
                node = BinOp("vpdoohu", [node, Parser.parseExpression(tokenizer)])
            elif tokenizer.next.type == "CONCAT":
                tokenizer.selectNext() 
                node = BinOp("grw", [node, Parser.parseExpression(tokenizer)])
            else:
                raise Exception("Error")
        return node

    def parseExpression(tokenizer):
        node = Parser.parseTerm(tokenizer)
        while tokenizer.next.type == "PLUS" or tokenizer.next.type == "MINUS" or tokenizer.next.type == "OR":
            if tokenizer.next.type == "PLUS":
                tokenizer.selectNext() 
                node = BinOp('+', [node, Parser.parseTerm(tokenizer)])
            elif tokenizer.next.type == "MINUS":
                tokenizer.selectNext() 
                node = BinOp("-", [node, Parser.parseTerm(tokenizer)])
            elif tokenizer.next.type == "OR":
                tokenizer.selectNext() 
                node = BinOp("ru", [node, Parser.parseTerm(tokenizer)])
            else:
                raise Exception("Error")
        return node

        
    def parseTerm(tokenizer):
        node = Parser.parseFactor(tokenizer)
        while tokenizer.next.type == "MULT" or tokenizer.next.type == "DIV" or tokenizer.next.type == "AND":
            if tokenizer.next.type == "MULT":
                tokenizer.selectNext() 
                node = BinOp('*', [node, Parser.parseFactor(tokenizer)])
            elif tokenizer.next.type == "DIV":
                tokenizer.selectNext() 
                node = BinOp("gly", [node, Parser.parseFactor(tokenizer)])
            elif tokenizer.next.type == "AND":
                tokenizer.selectNext() 
                node = BinOp("dqg", [node, Parser.parseFactor(tokenizer)])
            else:
                raise Exception("Error")
        return node
        
    
    def parseFactor(tokenizer):
        if tokenizer.next.type == 'INT':
            #print("token: ", tokenizer.next.value)
            node = IntVal(int(tokenizer.next.value))
            tokenizer.selectNext()
            return node
        elif tokenizer.next.type == 'STRING':
            node = StrVal(tokenizer.next.value)
            tokenizer.selectNext()
            return node
        elif tokenizer.next.type == 'IDENTIFIER':
            id = tokenizer.next.value
            tokenizer.selectNext()
            if tokenizer.next.type == "OPENPAR":
                args = []
                tokenizer.selectNext()
                if tokenizer.next.type != "CLOSEPAR":
                    args.append(Parser.parseRelExpression(tokenizer))
                while tokenizer.next.type != "CLOSEPAR":
                    if tokenizer.next.type == "COMMA":
                        tokenizer.selectNext()
                        args.append(Parser.parseRelExpression(tokenizer))
                    else:                       
                        raise Exception("Error")
                if tokenizer.next.type == "CLOSEPAR":
                    tokenizer.selectNext()
                    node = FuncCall(id, args)
                else:
                    raise Exception("Error")
            else:
                node = Identifier(id)
                return node
            return node
    
        elif tokenizer.next.type == 'PLUS':   
            tokenizer.selectNext()        
            node = UnOp('+', [Parser.parseFactor(tokenizer)])
            return node
        elif tokenizer.next.type == 'MINUS':
            tokenizer.selectNext()
            node = UnOp('-', [Parser.parseFactor(tokenizer)])
            return node
        elif tokenizer.next.type == 'NOT':
            tokenizer.selectNext()
            node = UnOp('!', [Parser.parseFactor(tokenizer)])
            return node
        elif tokenizer.next.type == 'OPENPAR':         
            tokenizer.selectNext()
            node = IntVal(Parser.parseRelExpression(tokenizer)).value
            if tokenizer.next.type == 'CLOSEPAR':
                tokenizer.selectNext()            
            else:
                raise Exception("Error")
            return node
        elif tokenizer.next.type == 'READ':
            tokenizer.selectNext()
            if tokenizer.next.type == 'OPENPAR':
                tokenizer.selectNext()
                if tokenizer.next.type == 'CLOSEPAR':
                    tokenizer.selectNext()
                    node = Read(" ", [])
                    return node
                else:
                    raise Exception("Error")
        else:
            raise Exception("Error")
        
    def run(code):
        #code = code.replace(" ", "")
        code = PrePro.filter(code)
        openParCount = code.count("rshqsdu")
        closeParCount = code.count("forvhsdu")
        if openParCount == closeParCount:
            tokenizer = Tokenizer(code)
            tokenizer.selectNext() 
            resultado = Parser.parseBlock(tokenizer)
            #resultado.children.append(FuncCall(None, []))
            return resultado
        else:
            raise Exception("Error")
    
  
def main():
    arquivo = sys.argv[1]
    if arquivo.endswith('.ccl'):
        with open(arquivo, 'r') as f:
            conteudo = f.read()
            resultado = Parser.run(conteudo)
            symbolTable = SymbolTable()
            resultado.evaluate(symbolTable)

if __name__ == '__main__':
    main()