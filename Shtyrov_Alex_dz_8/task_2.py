"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import timeit
import random


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


orig_list_10 = [random.uniform(-100, 100) for _ in range(10)]
orig_list_100 = [random.uniform(-100, 100) for _ in range(100)]
orig_list_1000 = [random.uniform(-100, 100) for _ in range(1000)]

# замеры 10
print(timeit.timeit("merge_sort(orig_list_10.copy())",
                    setup="from __main__ import merge_sort, orig_list_10", number=100))

# замеры 100
print(timeit.timeit("merge_sort(orig_list_100.copy())",
                    setup="from __main__ import merge_sort, orig_list_100", number=100))

# замеры 1000
print(timeit.timeit("merge_sort(orig_list_1000.copy())",
                    setup="from __main__ import merge_sort, orig_list_1000", number=100))
