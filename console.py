import re
from Solve import Lexer as l
from orderMap import *
from noOrderMap import *
from hashMap import *
from AVL import *

order_map = orderMap()
unorder_map = noOrderMap()
hash_map = HashMap()
avl_tree = AVL()
root = None

list_polinom = []
regex_map = {'space': r' ',
             'var': r'(\w+)',
             'plus': r'[+]*',
             'minus': r'[-]*',
             'mul': r'[*]*',
             'lpar': r'[(]',
             'rpar': r'[)]',
             'end': r''}


def input_in_data_structure(key, value):
    order_map.put(key, value)
    unorder_map.put(key, value)
    hash_map.put(key, value)
    global root
    root = avl_tree.insert(key, value, root)
    # print(hash_map)


def solve_math(s: str):
    global regex_map
    while len(s) > 0:
        f = False
        for key, value in regex_map.items():
            if key == 'end':
                f = True
                break
            res = re.match(value, s)
            if res is not None:
                s = s[res.end():]
                if key != 'space':
                    print(f'{res.group()}, {s}, {len(s)}')
                    list_polinom.append(res.group())
                break
        if f:
            print('error!', s)
    lexer = l.Lexer(list_polinom)


def getHashMap():
    return hash_map


def input_monom():
    print('Введите матемтическое выражение: ', end='')
    s_monom = input()
    solve_math(s_monom)


def input_polinom():
    print('Укажите ключ к полиному:', end=' ')
    key = input()
    print('Введите полином: ', end=' ')
    polinom_string = input()
    input_in_data_structure(key, polinom_string)


def choice():
    print('Введите, что вы хотите выполнить:')
    print('1. Ввести полином')
    print('2. Выполнить операцию по полиномам')
    print('3. Вывести все полиномы на основе (hash map)')
    print('4. Выход')
    choice_int = int(input())
    return choice_int


def output_polinoms():
    # print(';fdasf')
    print(hash_map)


# pashalka
class Console:
    pass
