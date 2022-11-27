from tag import Tag
from token import Token
from lexer import Lexer
from parser import Parser

'''
Esse eh o programa principal. Basta executa-lo.
'''

if __name__ == "__main__":
   lexer = Lexer('prog1.txt')

   parser = Parser(lexer)

   parser.Programa()

   print("\n=>Tabela de simbolos:")
   lexer.printTS()
   lexer.closeFile()
    
   print('\n=> Fim da compilacao')
