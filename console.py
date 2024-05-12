import re
from Solve.Lexer import Lexer
from Tables.orderMap import orderMap
from Tables.noOrderMap import noOrderMap
from Tables.hashMap import HashMap
from AVL.AVL import AVL
from Polinom.Polinom import polinom
from pair import Pair

order_map = orderMap()
unorder_map = noOrderMap()
hash_map = HashMap()
avl_tree = AVL()
root = None
hash_map.put('a', polinom('x^2'))
hash_map.put('b', polinom('x^2'))

list_polinom = []
regex_map = {'space': r' ',
             'var': r'(\w+)',
             'plus': r'[+]+',
             'minus': r'[-]+',
             'mul': r'[*]+',
             'lpar': r'[(]+',
             'rpar': r'[)]+',
             'end': r''}


def input_in_data_structure(key, value):
    order_map.put(key, value)
    unorder_map.put(key, value)
    # print('input - ', key, value)
    hash_map.put(key, value)
    global root
    # root = avl_tree.insert(key, value, root)
    # print(hash_map)


def solve_math(s: str):
    # Считываем строку запроса и переводим её в список токенов
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
                    # print(f'asdad {res.group()}, {s}, {len(s)}, {value}')
                    list_polinom.append(Pair(res.group(), key))
                break
        if f:
            print('error!', s)
    # отправляем строку в решение
    lexer = Lexer(list_polinom)
    print('Что вы хотите сделать:')
    print('1. Добавить новый полином в таблицу')
    print('2. Назад')
    choice = int(input())
    match choice:
        case 1:
            print('Введите ключ к таблице - ', end='')
            key = input()
            hash_map.put(key, lexer.get_monom())
        case _:
            return
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
    print(polinom(polinom_string))
    input_in_data_structure(key, polinom(polinom_string))


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
