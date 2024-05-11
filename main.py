from console import *
from Tables.orderMap import *
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
    pol1 = a.polinom('x^2')
    pol2 = a.polinom('y^1')
    pol3 = a.polinom('z^2')
    mon1 = m.Monom(pol1)
    mon2 = m.Monom(pol2)
    mon3 = m.Monom(pol3)
    mon4 = mon1 + mon2
    mon5 = mon4 * mon3
    print(mon5)
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
