"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time

n = 1000000


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time() - t))
        return res

    return tmp


@timer
def gen_dict(items):
    _my_dict = {x: x + 10 for x in range(items)}
    return _my_dict


@timer
def gen_list(items):
    _my_list = [(i, i + 10) for i in range(items)]
    return _my_list


my_list = gen_list(n)
my_dict = gen_dict(n)


# Время выполнения функции генерации листа меньше времени выполнения
# функции генерации словаря. Вероятно, это обусловлено врменем
# создание хэш таблицы словаря. Но в дальнейшем, мы сможем
# гораздо быстрее получить доступ к значению по ключу словаря O(1),
# чем будем искать значения в листе О(n).

@timer
def operation(dict_or_list):
    if type(dict_or_list) is list:
        for el in dict_or_list:
            if el[0] == 500000:
                return el[1]
    if type(dict_or_list) is dict:
        return dict_or_list.get(500000)


operation(my_list)
operation(my_dict)
