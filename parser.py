################################################################################
#                  Autores: Fernando Rosendo e Marcel Souza
#                            Arquivo: "parser.py"
################################################################################

from rply import ParserGenerator
from ast import Num, Grt, Select, String, Lss, Eq, Condition

#Trocar o GRT STR por GRT NUM depois quando terminar

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['SELECT','FROM','WHERE','SEP','BOXPLOT','STR','GRT', 'LSS', 'EQ']
            #Adicionar o NUM no final, agora é tudo string
        )

    def parse(self):
        #colocar + em sel_col depois pra ver se funciona
        #não funciona colocar +, o que faz sentido já que não é coisa de GLC
        @self.pg.production('program : SELECT sel_col FROM origem')
        def prog_sel_simples(p):
            return Select(p[1], origem=p[3])

        @self.pg.production('program : SELECT sel_col FROM origem WHERE condition')
        def prog_sel_where(p):
            return Select(p[1], origem=p[3],where=p[5])

        @self.pg.production('program : SELECT sel_col FROM origem WHERE condition BOXPLOT box_x SEP box_y')
        def prog_sel_where_box(p):
            return Select(p[1],origem=p[3],where=p[5],box_x=p[7],box_y=p[9])

        @self.pg.production('condition : sel_col operator STR')
        def condition(p):
            left = p[0]
            right = p[2]
            if p[1].gettokentype() == 'GRT':
                return Condition(left, Grt(left,right), right.getstr())
            elif p[1].gettokentype() == 'LSS':
                return Condition(left, Lss(left, right), right.getstr())
            elif p[1].gettokentype() == 'EQ':
                return Condition(left, Eq(left, right), right.getstr())
            else:
                raise ValueError('Oops, isso não é possível.')

        @self.pg.production('operator : GRT')
        @self.pg.production('operator : LSS')
        @self.pg.production('operator : EQ')
        def operator(p):
            return p[0]

        @self.pg.production('sel_col : STR')
        def sel_col(p):
            return String(p[0].getstr())

        @self.pg.production('origem : STR')
        def origem(p):
            return String(p[0].getstr())

        @self.pg.production('box_x : STR')
        def box_x(p):
            return String(p[0].getstr())

        @self.pg.production('box_y : STR')
        def box_y(p):
            return String(p[0].getstr())

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
