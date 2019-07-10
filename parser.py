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
        #colocar + em sel_col depois pra ver se funciona
        @self.pg.production('program : SELECT sel_col FROM origem')
        def prog_sel_simples(p):
            return 
        @self.pg.production('program : SELECT sel_col FROM origem WHERE sel_col GRT NUM BOXPLOT box_x SEP box_y')
        @self.pg.production('program : SELECT sel_col FROM origem WHERE STR GRT NUM')
        def program(p):
            pass

        @self.pg.production('sel_col : STR')
        def sel_col(p):
            return p[0]

        @self.pg.production('origem : STR')
        def origem(p):
            return p[0]

        @self.pg.production('box_x : STR')
        def box_x(p):
            return p[0]

        @self.pg.production('box_y : STR')
        def box_y(p):
            return p[0]

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
