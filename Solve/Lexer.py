import console
from pair import Pair
from Polinom.Monom import Monom
from Polinom.Polinom import polinom


class Lexer:
    def __init__(self, list_token):
        self.__list_token = list_token
        self.hash_table = console.hash_map
        self.list_monom = []
        self.list_operator = []
        self.solve()
        self.debug_print()
        print(self.hash_table)

    def solve(self):
        for item in self.list_token:
            if item.second == 'var':
                # s = self.hash_table.get(item.first)
                # print("dada ", s)
                pol = self.hash_table.get(item.first)
                print("dsasdasd", pol)
                self.list_monom.append(Monom(pol))
            else:
                self.list_operator.append(item.first)

    @property
    def list_token(self):
        return self.__list_token

    @list_token.setter
    def list_token(self, list_token_):
        self.__list_token = list_token_

    def debug_print(self):
        for monom in self.list_monom:
            print(monom)
        print('<<<<<<<<<>>>>>>>>>')
        for oper in self.list_operator:
            print(oper)

