# Вам даны два отсортированных списка (по возрастанию) длина которых a и b.
# Задача: создать функцию, которая будет на выходе иметь один общий отсортированный список res (по убыванию).
# Пользоваться sort или иными функциями для сортировки ЗАПРЕЩЕНО!

def bubble_sorting(list_a: list, list_b: list):
    a, b = len(list_a), len(list_b)
    res = list_a + list_b

    for i in range(a + b - 1):
        for j in range(a + b - i - 1):
            if res[j] < res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res


# example:
# print(bubble_sorting([1, 2, 3, 4, 5], [2, 4, 6, 8, 19]))
# output: [19, 8, 6, 5, 4, 4, 3, 2, 2, 1]
