################################################################################
#                  Autores: Fernando Rosendo e Marcel Souza
#                            Arquivo: "parser.py"
################################################################################

from rply import ParserGenerator
from ast import Num,Grt, Select, From, Where, Boxplot

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['SELECT','FROM','WHERE','SEP','BOXPLOT','STR','GRT','NUM']
        )

    def parse(self):
        @self.pg.production('program : SELECT STR FROM STR WHERE STR GRT NUM BOXPLOT STR SEP STR')
        def program(p):
            return print(str(p))

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
