# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = 143
b = 234


def palindrome(number):
    return str(number) == str(number)[::-1]


def counter(a, b):
    k = 0
    for i in range(a, b + 1):
        palindrome(i)
        k += 1
#   print(k)
    return k

print("Количество чисел, являющихся палиндромами:", counter(a, b))
