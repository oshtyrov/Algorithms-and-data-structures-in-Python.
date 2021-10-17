"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
import cProfile

number = 123456789


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


#  Проблема в рекурсии, функция вызывает сама себя = количеству цифр в числе.
#  Этого можно избежать, по тому решение худшее.


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


#  Решение быстрее, т.к. тут цикл внутри фукнции работает, функция не вызывает саму себя,
#  как в 1 варианте.

def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# привести число к строке и взять срез - лучший вариант, за 2 шага.

cProfile.run('revers(number)')
cProfile.run('revers_2(number)')
cProfile.run('revers_3(number)')

print(
    timeit(
        'revers(number)',
        setup='from __main__ import revers, number',
        number=100000))

print(
    timeit(
        'revers_2(number)',
        setup='from __main__ import revers_2, number',
        number=100000))

print(
    timeit(
        'revers_3(number)',
        setup='from __main__ import revers_3, number',
        number=100000))

# timeit результаты
# 0.5623154
# 0.3008588
# 0.0726443 - вариант 3 является лучшим
