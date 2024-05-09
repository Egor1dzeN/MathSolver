from pair import *
import bisect


class polinom:
    def __init__(self, s: str):
        self.count = 0
        self.variable = []
        i = 0
        if not (s[0].isdigit()):
            self.count = 1
        else:
            while s[i].isdigit():
                # print(self.count)
                self.count = self.count * 10 + int(s[i])
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
                self.variable.append(Pair(variable, degree))
                continue
            i += 1
            degree = 0
            # считываем степень
            while i < len(s) and s[i].isdigit():
                degree = degree * 10 + int(s[i])
                i += 1
                # print(Pair(variable, degree))
            self.variable.append(Pair(variable, degree))
            # print(Pair(variable, degree))
        # for el in self.variable:
        #     print(el.first, el.second)
        # print(self.variable)
        self.variable = sorted(self.variable, key=lambda x: x.first)
        # for el in self.variable:
        #     print(el.first, el.second)

    def __str__(self):
        res = f'{self.count}  '
        for el in self.variable:
            res += f'(var={el.first}, pow={el.second}), '
        return res[:len(res)-2]
