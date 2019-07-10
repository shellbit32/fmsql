################################################################################
#                  Autores: Fernando Rosendo e Marcel Souza
#                            Arquivo: "parser.py"
################################################################################

from rply import ParserGenerator
from ast import Num,Grt, Select

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['SELECT','FROM','WHERE','SEP','BOXPLOT','STR','GRT','NUM']
        )

    def parse(self):
        #colocar + em sel_col depois pra ver se funciona
        @self.pg.production('program : SELECT sel_col FROM origem')
        def prog_sel_simples(p):
            return Select(p[1], origem=p[3])

        @self.pg.production('program : SELECT sel_col FROM origem WHERE sel_col GRT NUM')
        def prog_sel_where(p):
            return Select(p[1], origem=p[3],where=p[5])

        @self.pg.production('program : SELECT sel_col FROM origem WHERE sel_col GRT NUM BOXPLOT box_x SEP box_y')
        def prog_sel_where_box(p):
            return Select(p[1],origem=p[3],where=p[5],box_x=p[9],box_y=p[11])

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
