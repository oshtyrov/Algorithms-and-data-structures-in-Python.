"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
from memory_profiler import profile


@profile()
def calc(num):
    res_even = 0
    res_odd = 0
    for n in num:
        if int(n) % 2 == 0:
            res_even += 1
        else:
            res_odd += 1
    print(f'В Вашем числе: {res_even} четных чисел и {res_odd} нечетных.')


def recur(str_num, res_even=0, res_odd=0):
    num = str_num[0]
    if int(num) % 2 == 0:
        res_even += 1
    else:
        res_odd += 1
    if len(str_num) == 1:
        return f'В Вашем числе: {res_even} четных чисел и {res_odd} нечетных.'
    else:
        return recur(str_num[1:], res_even, res_odd)


"""
Для решения проблемы с множеством таблиц, просто сделал 
функцию-обертку и применил профайлер к ней. Насчет подводных камней -
в результате имеем только одну общую чтрочку данных насчет потребления
памяти. Не видно, что происходит внутри функции.
"""


@profile()
def one_tbl(num):
    recur(num)


print(calc('123'))
print(one_tbl('123'))
