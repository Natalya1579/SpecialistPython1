# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of=-10, to=10):
    import random
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(of, to))
    return result_list


my_list = gen_list(15)
print(my_list)
