"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib


url_1 = 'http_url_1'
url_2 = 'http_url_2'
url_3 = 'http_url_3'

url_database = {
    'http_url_1': '5f799093365a935f18a57dcac39cd757f4a776ace31f04e38ceb940c18f2b74a',
}


def hashing_url(some_url):
    salt = 'salt'
    if some_url not in url_database:
        hash_url = hashlib.sha3_256(salt.encode() + some_url.encode()).hexdigest()
        url_database[some_url] = hash_url
        print(f'Ссылка {some_url} кеширована в базу данных')
    else:
        print(f'Ссылка {some_url} уже присутствует в базе данных')


hashing_url(url_1)
hashing_url(url_3)








