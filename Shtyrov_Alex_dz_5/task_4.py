"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import collections
from timeit import timeit

nd = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
nod = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

my_list = ['e', 'd', 'c', 'b', 'a']

print(timeit(
    "nd.items()",
    setup='from __main__ import nd',
    number=1000000))

print(timeit(
    "nod.items()",
    setup='from __main__ import nod',
    number=1000000))


def get_from_d():
    for key in my_list:
        nd.get(key)


def get_from_od():
    for key in my_list:
        nod.get(key)


def popitem_d():
    _nd = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    for i in range(4):
        _nd.popitem()


def popitem_od():
    _nod = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
    for i in range(4):
        _nod.popitem()


print(timeit(
    "get_from_d()",
    setup='from __main__ import get_from_d, nd',
    number=1000000))

print(timeit(
    "get_from_od()",
    setup='from __main__ import get_from_od, nod',
    number=1000000))

print(timeit(
    "popitem_d()",
    setup='from __main__ import popitem_d, nd',
    number=1000000))

print(timeit(
    "popitem_od()",
    setup='from __main__ import popitem_od, nod',
    number=1000000))

# время по результатам items и get постоянно меняются то в одну, то в другую пользу.
# popitem с orderdict работает в раза 3 медленнее.
# наколько я понял из прочитанного, с версии 3.6 пайтон словари теперь упорядоченны,
# по тому иэто преимущество od отпало.
