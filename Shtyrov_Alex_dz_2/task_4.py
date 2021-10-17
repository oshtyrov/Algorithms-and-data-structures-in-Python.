"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


# def recur(res=0, n='1 -0.5 0.25 -0.125', user_input=None, counter=None):
#     if type(n) is str:
#         n = list(n.split(' '))
#     if len(n) == 4:
#         user_input = int(input('Введите количество элементов: '))
#         counter = user_input
#     num = float(n[0])
#     res += num
#     if counter == 1:
#         return f'Количество элементов - {user_input}, их сумма - {res}.'
#     n.pop(0)
#     return recur(res, n, user_input, counter - 1)

def recur(res=1, n=1.0, user_input=None, counter=None):
    if n == 1.0:
        user_input = int(input('Введите количество элементов: '))
        counter = user_input - 1
    if user_input != 1:
        n = n / -2
        res += n
    if counter <= 1:
        return f'Количество элементов - {user_input}, их сумма - {res}.'
    return recur(res, n, user_input, counter - 1)


print(recur())
