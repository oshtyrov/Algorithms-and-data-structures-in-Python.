"""
Задание 2.
Предложить еще какие-гибудь варианты (механизмы, библиотеки) оптимизации и
доказать (наглядно, кодом) их эффективность
"""

"""
Кроме использования __slots__, показанного на уроке,
для использования преимуществ словаря и экономии
потребляемой памяти, можно использовать определение в виде 
класса с доступом по имени атрибута (пример 1). Кроме того,
для экономии памяти также советуют использовать  collections.namedtuple (пример 2).
Также хорошим вариантом с минимальным потреблением памяти -
использование модуля numpy. Еще есть Cython, Dataobject, 
Recordclass: мутируемый namedtuple без GC.
"""
import sys
import collections
import numpy

# Пример 1

ob = {'x': 1, 'y': 2, 'z': 3}
print(sys.getsizeof(ob))  # 128


class MyClass:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


ob_2 = MyClass(1, 2, 3)
print(sys.getsizeof(ob_2))  # 24

# Пример 2
MyDict = {1: {'first_name': 'Ivan', 'second_name': 'Ivanov'}, }
print(sys.getsizeof(MyDict))  # 128

RES = collections.namedtuple('Resume', 'id first_name second_name')
RESUME_PARTS = RES(
    id='1',
    first_name='Ivan',
    second_name='Ivanov'
)
print(sys.getsizeof(RESUME_PARTS))  # 32

# Пример 3
Point = numpy.dtype([('x', numpy.int32), ('y', numpy.int32), ('z', numpy.int32)])
print(sys.getsizeof(Point))  # 56

