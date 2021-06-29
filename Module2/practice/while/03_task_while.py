# По данному натуральному n выведите лесенку из n ступенек, i-я ступень состоит из чисел от 1 до i без пробелов.
# Формат входных данных: Вводится натуральное число n.
# Формат выходных данных: Выведите ответ на задачу.
# Пример:
# Для n = 4
# Нужно вывести:
# 1
# 12
# 123
# 1234

number = int(input('Число: '))
i = 1   # номер ряда
row = i     # содержимое ряда
while i <= number:
    print(row)
    i += 1
    row = row * 10 + i
