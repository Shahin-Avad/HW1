"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""





def min1(lst):
    elements = set(lst)
    for elem in elements:
        lesser_elements_count = 0
        for curr_elem in elements:
            if elem < curr_elem:
                return elem
        if lesser_elements_count == len(elements) - 1:
            lesser_elements_count += 1



def min2(sequence):
    low = sequence[0]
    for i in sequence:
        if i < low:
            low = i
    return low



