"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

"""Класс collections.deque()"""
# простые операции с очередью
from collections import deque
from timeit import timeit


# simple_lst = list("abcdefghijklmnopqrstuvwxyz")
# simple_lst_2 = list("abcdefghijklmnopqrstuvwxyz")
# deq_obj = deque(simple_lst)


# print(deq_obj)  # -> deque(['b', 'c', 'd'])
# print(simple_lst)


# добавим элемент в конец очереди
def app_deq():
    simple_lst = list("abcdefghijklmnopqrstuvwxyz")
    simple_lst_2 = list("abcdefghijklmnopqrstuvwxyz")
    deq_obj = deque(simple_lst)
    for _el in simple_lst:
        deq_obj.append(_el)


# добавим элемент в конец листа
def app_lst():
    simple_lst = list("abcdefghijklmnopqrstuvwxyz")
    simple_lst_2 = list("abcdefghijklmnopqrstuvwxyz")
    deq_obj = deque(simple_lst)
    for _el in simple_lst:
        simple_lst_2.append(_el)


# добавим элемент в начало очереди
def applft_deq():
    simple_lst = list("abcdefghijklmnopqrstuvwxyz")
    simple_lst_2 = list("abcdefghijklmnopqrstuvwxyz")
    deq_obj = deque(simple_lst)
    for _el in simple_lst:
        deq_obj.appendleft(_el)


# добавим элемент в начало списка
def applft_lst():
    simple_lst = list("abcdefghijklmnopqrstuvwxyz")
    simple_lst_2 = list("abcdefghijklmnopqrstuvwxyz")
    deq_obj = deque(simple_lst)
    for _el in simple_lst:
        simple_lst_2.insert(0, _el)


# удаляем последний елемент из очереди
def poprght_deq():
    simple_lst = list("abcdefghijklmnopqrstuvwxyz")
    simple_lst_2 = list("abcdefghijklmnopqrstuvwxyz")
    deq_obj = deque(simple_lst)
    for i in range(10):
        deq_obj.pop()


# удаляем последний елемент из списка
def poprght_lst():
    simple_lst = list("abcdefghijklmnopqrstuvwxyz")
    simple_lst_2 = list("abcdefghijklmnopqrstuvwxyz")
    deq_obj = deque(simple_lst)
    for i in range(10):
        simple_lst_2.pop()


# удаляем последний елемент из очереди слева
def poplft_deq():
    simple_lst = list("abcdefghijklmnopqrstuvwxyz")
    simple_lst_2 = list("abcdefghijklmnopqrstuvwxyz")
    deq_obj = deque(simple_lst)
    for i in range(10):
        deq_obj.popleft()


# удаляем последний елемент из списка слева
def poplft_lst():
    simple_lst = list("abcdefghijklmnopqrstuvwxyz")
    simple_lst_2 = list("abcdefghijklmnopqrstuvwxyz")
    deq_obj = deque(simple_lst)
    for i in range(10):
        del simple_lst_2[0]


print("app_deq()")
print(timeit(
    "app_deq()",
    setup='from __main__ import app_deq',
    number=1000000))

print("app_lst()")
print(timeit(
    "app_lst()",
    setup='from __main__ import app_lst',
    number=1000000))

print("applft_deq()")
print(timeit(
    "applft_deq()",
    setup='from __main__ import applft_deq',
    number=1000000))

print("applft_lst()")
print(timeit(
    "applft_lst()",
    setup='from __main__ import applft_lst',
    number=1000000))


print("poprght_deq()")
print(timeit(
    "poprght_deq()",
    setup='from __main__ import poprght_deq',
    number=1000000))


print("poprght_lst()")
print(timeit(
    "poprght_lst()",
    setup='from __main__ import poprght_lst',
    number=1000000))

print("poplft_deq()")
print(timeit(
    "poplft_deq()",
    setup='from __main__ import poplft_deq',
    number=1000000))

print("poplft_lst()")
print(timeit(
    "poplft_lst()",
    setup='from __main__ import poplft_lst',
    number=1000000))

# app_deq()
# 5.3970861999999995
# app_lst()
# 6.267244499999999
# applft_deq()
# 5.949115000000001
# applft_lst()
# 8.6009907
# poprght_deq()
# 4.5180577
# poprght_lst()
# 4.940894199999999
# poplft_deq()
# 4.707579100000004
# poplft_lst()
# 5.357204199999998

# общая тенденция - deq быстрее lst, особенно при добавлении и удалении
# первых элементов коллекции (слева). В остальных случаях разница не так существенна.

