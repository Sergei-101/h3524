# Задача 1
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')

# Решение

def correct_link(way_link: str) -> tuple[str]:
    """
    принимает на вход строку - абсолютный путь до файла.
    возвращает кортеж из трёх элементов
    """
    way, name_file = way_link.rsplit('/', 1)
    return way, *name_file.split('.')
print(correct_link("c:/Users/Vladislav/Desktop/deep_to_python/test.txt"))

# Задача 2
# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь
# с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная
# на процент премии (решение задачи "не в одну строку" есть на 4 семинаре(5 задача))

name_list = ['Vlad', 'Den', 'Alex']
salary_list = [1000, 2000, 3000]
extra_list = ['10.25%', '15%', '20%']

extra = {name: salary * extra for name, salary, extra in zip(name_list, salary_list, list(map(lambda x: float(x[:-1]) / 100, extra_list)))}

print(extra)

# Задача 3
# Создайте функцию генератор чисел Фибоначчи

def fibo(n:int) -> int:
    """
    генератор чисел Фибоначчи
    """
    fib_0 = 0
    fib_1 = fib_2 = 1
    print(fib_0, fib_1, fib_2, end=' ')

    for i in range(2, n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        print(fib_2, end=' ')
fibo(7)