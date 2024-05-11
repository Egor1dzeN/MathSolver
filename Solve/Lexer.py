import copy

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
        # self.debug_print()
        # print(self.hash_table)

    def solve(self):
        for item in self.list_token:
            if item.second == 'var':
                # s = self.hash_table.get(item.first)
                # print("dada ", s)
                pol = self.hash_table.get(item.first)
                # print("dsasdasd", pol)
                self.list_monom.append(copy.deepcopy(Monom(pol)))
            else:
                self.list_operator.append(copy.deepcopy(item.first))
        i = 0
        # print('!!!!!!!!!!!!!!!!!')
        while i < len(self.list_operator):
            if self.list_operator[i] == '*':
                self.list_monom[i] = self.list_monom[i] * self.list_monom[i + 1]
                self.list_monom.pop(i + 1)
                self.list_operator.pop(i)
                # print('UMNOZH')
                # self.debug_print()
                continue

            """
            if self.list_operator[i] == ')':
                l = i
                while self.list_operator[l] != '(':
                    l -= 1
                r = l + 1
                print(f'l = {l}, r = {r}')
                while r < i:
                    if self.list_operator[r] == '+':
                        self.list_monom[r] = self.list_monom[r] + self.list_monom[r + 1]
                        self.list_monom.pop(r + 1)
                        self.list_operator.pop(r)
                    if self.list_operator[r] == '-':
                        self.list_monom[r] = self.list_monom[r] - self.list_monom[r + 1]
                        self.list_monom.pop(r + 1)
                        self.list_operator.pop(r)
            """
            i += 1
            # self.debug_print()
        i = 0
        # print('!!!ghjgjh!!!!')
        # print(self.hash_table.get('a'))
        while i < len(self.list_operator):
            if self.list_operator[i] == '+':
                self.list_monom[i] = self.list_monom[i] + self.list_monom[i + 1]
                self.list_monom.pop(i + 1)
                self.list_operator.pop(i)
            elif self.list_operator[i] == '-':
                self.list_monom[i] = self.list_monom[i] + self.list_monom[i + 1]
                self.list_monom.pop(i + 1)
                self.list_operator.pop(i)
            else:
                i += 1
            # self.debug_print()

    @property
    def list_token(self):
        return self.__list_token

    @list_token.setter
    def list_token(self, list_token_):
        self.__list_token = list_token_

    def debug_print(self):
        print('begin')
        for monom in self.list_monom:
            print(monom)
        print('<<<<<<<<<>>>>>>>>>')
        for oper in self.list_operator:
            print(oper)
        print('end')
