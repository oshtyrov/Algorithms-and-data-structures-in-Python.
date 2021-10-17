"""
Задание 4.

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
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

my_dict = {
    'usr_1': {'psw': '6666', 'act': True},
    'usr_2': {'psw': '5555', 'act': True},
    'usr_3': {'psw': '4444', 'act': False},
    'usr_4': {'psw': '3333', 'act': True},
    'usr_5': {'psw': '2222', 'act': False},
    'usr_6': {'psw': '1111', 'act': True}

}


# O(n)
def checking(users, user_name, user_password):
    for key, value, in users.items():
        if key == user_name:
            if value['psw'] == user_password and value['act']:
                return 'Access is allowed'
            elif value['psw'] == user_password and not value['act']:
                return 'Account is not active'
            elif value['psw'] != user_password:
                return 'Password is incorrect. Access is denied'
    return 'User does not exist'


# O(1). Откровенно говоря, не смог придумать решение сложности О(1) без разбора дз.
def checking_2(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['psw'] == user_password and users[user_name]['act']:
            return 'Access is allowed'
        elif users[user_name]['psw'] == user_password and not users[user_name]['act']:
            return 'Account is not active'
        elif users[user_name]['psw'] != user_password:
            return 'Password is incorrect. Access is denied'
    else:
        return 'User does not exist'


print(checking(my_dict, 'usr_1', '6666'))
print(checking_2(my_dict, 'usr_1', '6666'))
