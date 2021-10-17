"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit

a = (1, 4, 3, 4, 5, 4, 7, 4, 9, 4, 11, 4, 13, 4, 15)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit("""
a = (1, 4, 3, 4, 5, 4, 7, 4, 9, 4, 11, 4, 13, 4, 15)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
"""))


def func_2(num):
    new_arr = [i for i in range(len(num)) if num[i] % 2 == 0]
    return new_arr


print(timeit("""
a = (1, 4, 3, 4, 5, 4, 7, 4, 9, 4, 11, 4, 13, 4, 15)


def func_2(num):
    new_arr = [i for i in range(len(num)) if num[i] % 2 == 0]
    return new_arr
"""))


def func_3(nums):
    new_arr = []
    i = 0
    for el in nums:
        if el % 2 == 0:
            new_arr.append(i)
            i += 1
    return new_arr


print(timeit("""
a = (1, 4, 3, 4, 5, 4, 7, 4, 9, 4, 11, 4, 13, 4, 15)


def func_3(nums):
    new_arr = []
    i = 0
    for el in nums:
        if el % 2 == 0:
            new_arr.append(i)
            i += 1
    return new_arr
"""))

print(
    timeit(
        'func_1(a)',
        setup='from __main__ import func_1, a',
        number=100000))

print(
    timeit(
        'func_2(a)',
        setup='from __main__ import func_2, a',
        number=100000))

print(
    timeit(
        'func_3(a)',
        setup='from __main__ import func_3, a',
        number=100000))

# 0.252721
# 0.243185 - 1 и 2 решения приблизительно одинаковы. Как я понял генератор - просто синтаксический сахар.
# 0.186127 - лучший вариант через for in
