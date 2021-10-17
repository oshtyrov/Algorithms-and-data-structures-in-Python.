"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib

# решил воспользоваться сплитом вместо цикла срезов по строке.

papa = 'papa pap pa ap apa p a papa pap pa ap apa p a papa pap pa ap apa p a'
res = set()
papa_lst = papa.split(' ')
for el in papa_lst:
    hash_el = hashlib.sha3_256(el.encode()).hexdigest()
    res.add(hash_el)
print(len(res))


