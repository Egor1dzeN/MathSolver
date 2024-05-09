# from Polinom import polinom

type Vector = Monom


class Monom:
    def __init__(self, polinom_, char='+'):
        self.__list_polinom = [polinom_]
        self.list_operator = [char]
        # print(self.__list_polinom)

    @property
    def list_polinom(self):
        return self.__list_polinom

    @list_polinom.setter
    def list_polinom(self, list_polinom):
        self.__list_polinom = list_polinom

    def __str__(self):
        res = ''
        for i in range(len(self.list_polinom)):
            res += str(self.list_operator[i]) + '\n'
            res += str(self.list_polinom[i]) + '\n'
        return res

    def __add__(self, other: Vector):
        for i in range(len(self.list_polinom)):
            cur_polinom = self.list_polinom[i]
            for j in range(len(other.list_polinom)):
                cur_polinom2 = other.list_polinom[j]
                print(type(cur_polinom2))
                if cur_polinom == cur_polinom2:
                    # pass
                    if (self.list_operator[i] == other.list_operator[j] == '+'
                            or
                            self.list_operator[i] == other.list_operator[j] == '-'):
                        cur_polinom.const += cur_polinom2.const
                    elif (self.list_operator[i] == '+' and other.list_operator[j] == '-'
                          or
                          self.list_operator[i] == '-' and other.list_operator[j] == '+'):
                        cur_polinom.const -= cur_polinom2.const
                    if cur_polinom.const == 0:
                        self.list_polinom.remove(cur_polinom)
                        self.list_operator.pop(i)
                    other.list_polinom.remove(cur_polinom2)
                    other.list_operator.pop(j)

                    break
        print('ghfd', other.list_polinom)
        for i in range(len(other.list_polinom)):
            self.list_polinom.append(other.list_polinom[i])
            self.list_operator.append(other.list_operator[i])
        print(self)
