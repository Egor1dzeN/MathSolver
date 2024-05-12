from pair import *
import bisect

type Vector = polinom


class polinom:
    def __init__(self, s: str):
        self.__const = 0
        self.__variable = []
        i = 0
        if not (s[0].isdigit()):
            self.__const = 1
        else:
            while s[i].isdigit():
                # print(self.const)
                self.__const = self.__const * 10 + int(s[i])
                i += 1
        s = s[i:]
        i = 0
        # print(s)
        while i < len(s):
            variable = ''
            degree = 1
            # считываем переменную
            while i < len(s) and not (s[i] == '^'):
                variable += s[i]
                i += 1
            if i >= len(s) or s[i] != '^':
                self.__variable.append(Pair(variable, degree))
                continue
            i += 1
            degree = 0
            # считываем степень
            while i < len(s) and s[i].isdigit():
                degree = degree * 10 + int(s[i])
                i += 1
                # print(Pair(__variable, degree))
            self.__variable.append(Pair(variable, degree))
            # print(Pair(__variable, degree))
        # for el in self.__variable:
        #     print(el.first, el.second)
        # print(self.__variable)
        self.__variable = sorted(self.__variable, key=lambda x: x.first)
        # for el in self.__variable:
        #     print(el.first, el.second)

    def __str__(self):
        # print('Polinom')
        res = f'{self.const}'
        for el in self.__variable:
            res += f'{el.first}^{el.second}'
        return res

    @property
    def const(self):
        return self.__const

    @const.setter
    def const(self, c):
        self.__const = c

    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, variable):
        self.__variable = variable

    def __eq__(self, other: Vector):
        # print(self.__variable)
        # print(other.__variable)
        return self.variable == other.variable

    def __mul__(self, other):
        self.const *= other.const
        for i in range(len(self.variable)):
            for j in range(len(other.variable)):
                if self.variable[i].first == other.variable[j].first:
                    self.variable[i].second += other.variable[j].second
                    other.variable.pop(j)
                    break
        for pair in other.variable:
            self.variable.append(pair)
        self.variable = sorted(self.variable, key=lambda x: x.first)
        # print(self)
        return self
