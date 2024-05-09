import re

import Polinom.Polinom
import polinom
from AVL import *
from console import *
from orderMap import *
import Polinom.Polinom as a
import Polinom.Monom as m


def forTest():
    Tree = AVL()
    rt = None
    rt = Tree.insert(1, 10, rt)
    Tree.preorder(rt)


def forTest2():
    map1 = orderMap()
    map1.put('d', 'hjasd')
    map1.put('4', 'hjasdsad')
    map1.put('2', 'hjasddas')
    map1.put('3', 'hjasddasd')
    print(map1.get('2'))


if __name__ == '__main__':
    a0 = a.polinom('x^2y^2')
    a2 = a.polinom('x^2y^21')
    # print(a0)
    a1 = m.Monom(a0,'-')
    a3 = m.Monom(a2, '+')
    a11 = a1 + a3
    print(a11)
    # a2 = m.Monom(a.polinom('x^2y^2'))
    # a2 = a.polinom('y^2x^2')
    # print(a1 == a2)
    while True:
        choice_int = choice()
        match choice_int:
            case 1:
                input_polinom()
            case 2:
                input_monom()
            case 3:
                output_polinoms()
            case _:
                break
