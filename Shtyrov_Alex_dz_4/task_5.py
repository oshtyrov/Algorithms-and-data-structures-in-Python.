"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""

from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


inp_1 = 5
print(simple(inp_1))


def primes(n=2):
    yield n
    yield from filter(lambda x: x % n, primes(n + 1))


def erast(num):
    a = []
    for p in primes():
        a.append(p)
        if len(a) == num:
            return a[-1]


inp_2 = 5
print(erast(inp_2))

print(
    timeit(
        'simple(inp_1)',
        setup='from __main__ import simple, inp_1',
        number=100000))

print(
    timeit(
        'erast(inp_2)',
        setup='from __main__ import erast, inp_2',
        number=100000))

#  0.88 - решение из уловия работает быстрее. Сложность О(n2)
#  1.64 - функцию генератора содрал из интернета, eras написал сам. Правда не
# уверен, что мое решение соответствует условию задания.
