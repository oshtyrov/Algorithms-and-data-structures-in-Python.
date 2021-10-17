"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

my_dict = {
    'Qwe': 6,
    'Asd': 2,
    'Zxc': 3,
    'Rty': 5,
    'Fgh': 4,
    'Vbn': 1
}


# Первые два решения плохие. Третье лучшее.

# O(n2)
def find_3max_1(some_dict):
    values_list = list(some_dict.values())
    three_max_values_list = []
    three_max_keys_list = []
    for i in range(3):
        max_value = max(values_list)
        three_max_values_list.append(max_value)
        values_list.remove(max_value)
    for k, v in some_dict.items():
        if v in three_max_values_list:
            three_max_keys_list.append(k)
    return three_max_keys_list


print(find_3max_1(my_dict))


# O(n2)
def find_3max_2(some_dict):
    three_max_values_list = (sorted(some_dict.values()))[3:]
    three_max_keys_list = []
    for k, v in some_dict.items():
        if v in three_max_values_list:
            three_max_keys_list.append(k)
    return three_max_keys_list


print(find_3max_2(my_dict))


# O(n log n)
def find_3max_3(some_dict):
    list_d = list(some_dict.items())
    list_d.sort(key=lambda i: i[1])
    dict_three_max = dict(list_d[3:])
    return list(dict_three_max.keys())


print(find_3max_3(my_dict))
