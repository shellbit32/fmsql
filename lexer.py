################################################################################
#                  Autores: Fernando Rosendo e Marcel Souza
#                             Arquivo: "lexer.py"
################################################################################

#Vamos definir nossos tokens neste arquivo

from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        #Select
        self.lexer.add('SELECT',r'select')

        #From
        self.lexer.add('FROM',r'from')

        #Where
        self.lexer.add('WHERE',r'where')

        #Separador
        self.lexer.add('SEP',r',')

        #Boxplot
        self.lexer.add('BOXPLOT',r'boxplot')

        #Strings alfanumericas
        self.lexer.add('STR',r'\w+')
#
#        #Col_select
#        self.lexer.add('COL_SEL',r'\w+')
#
#        #data_from
#        self.lexer.add('DAT_FR',r'\w+')
#
#        #Col_xbox
#        self.lexer.add('COL_XBOX',r'\w+')
#
#        #Col_ybox
#        self.lexer.add('COL_YBOX',r'\w+')

        #Maior
        self.lexer.add('GRT',r'>')

        #Menor
        self.lexer.add('LSS', r'<')

        #Igual
        self.lexer.add('EQ', r'=')

        #Numero
        self.lexer.add('NUM',r'\d')

        #Ignorar espaços em branco
        self.lexer.ignore(r'\s+')

        #Ignorar comentários
        #de uma linha (#)
        self.lexer.ignore('#(.)*\n')

        #de multiplas linhas (/* */)
        self.lexer.ignore('/\*(?s).*\*/')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
