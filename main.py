import re

import polinom
from AVL import *
from console import *
from orderMap import *
from Polinom.Polinom import polinom


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
    # forTest2()
    # p = polinom('12ffds^12a^1')
    # print(p)
    s = 'x+y+z'
    from re import *
    s = ' xdsa1+dsa('
    res = re.match(r' ', s)
    print(res.group())
    s = s[res.end():]
    res = re.match(r'(\w+)', s)
    print(res.group())
    s = s[res.end():]
    res = re.match(r'[+-]*', s)
    print(res.group())
    s = s[res.end():]
    res = re.match(r'(\w+)', s)
    print(res.group())
    s = s[res.end():]
    res = re.match(r'[(]', s)
    print(res.group())
    s = s[res.end():]
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
