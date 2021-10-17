"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from statistics import median
import random
import timeit

orig_list_11 = [random.randint(-100, 100) for _ in range(11)]
print(orig_list_11)
print(median(orig_list_11))


def shell_median(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data[len(data) // 2]  # т.к. всегда число будет заканчиваться на .5,
    # будет округление в большую сторону, получаем индекс медианы.


print(shell_median(orig_list_11))


# мой вариант без сортировки
def no_sort_median(data):
    index = len(data) // 2
    for i in range(index):
        data.remove(max(data))
    return max(data)


print(no_sort_median(orig_list_11))


print(timeit.timeit("shell_median(orig_list_11.copy())",
                    setup="from __main__ import shell_median, orig_list_11", number=100))


print(timeit.timeit("no_sort_median(orig_list_11.copy())",
                    setup="from __main__ import no_sort_median, orig_list_11", number=100))
