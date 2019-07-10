################################################################################
#                  Autores: Fernando Rosendo e Marcel Souza
#                    Arquivo: "ast.py" (Arvore Sintatica)
################################################################################

#Árvore Sintática da nossa linguagem

#Não tenho certeza se precisa de uma classe pro separador ','

#Tudo está retornando strings

class Num():
    def __init__(self,value):
        self.value = value

    def eval(self):
        return str(int(self.value))

class OpBinaria():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Grt(OpBinaria):
    def eval(self):
        return str(self.left.eval > self.right.eval)

class Select():

    def __init__(self,*args):
        self.cols = args

    def eval(self):
        return 'Selecionadas colunas ' + str(self.cols)

class From():

    def __init__(self, origem):
        self.origem = origem

    def eval(self):
        return 'da base ' + str(self.origem)

class Where():

    def __init__(self, col, op, val):
        self.col = col
        self.op = op
        self.val = val

    def eval(self):
        return ' onde ' + self.col + self.op + ' ' + str(self.val)

class Boxplot():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eval(self):
        return ' fazer boxplot de x: ' + self.x + ' e y: ' + self.y
