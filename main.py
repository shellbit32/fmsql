################################################################################
#                  Autores: Fernando Rosendo e Marcel Souza
#                             Arquivo: "main.py"
################################################################################

#Combinando os componentes do compilador neste arquivo

from lexer import Lexer
from parser import Parser

f = open('input.fmsql','r')
text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

#for token in tokens:
#    print(token)

pg = Parser()
pg.parse()
parser = pg.get_parser()
print(parser.parse(tokens).eval())
