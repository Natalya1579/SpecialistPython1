# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random import random

# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint

import random

numbers = []
n = 10
for i in range(n):
    numbers.append(random.randint(-100, 100))
# print(random.randint(-100, 100))
print(numbers)
