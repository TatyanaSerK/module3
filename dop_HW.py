data_structure = [  # исходные данные - список
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    # '''функция для подсчёта суммы всех чисел и длин всех строк.
    # данные преобразуем в список _list и рассматриваем элемент [0].
    # каждый сложный элемент "распаковываем"  и записываем в конец.
    # (пока не получим просто числа и буквы) которые суммируем'''

    sum_int = 0
    new_int = []
    new_str = []
    _list = list(args)
    while len(_list) > 0:  # с помощью цикла перебираем элементы списка
        k = _list[0]  # берем каждый раз первый элемент [0]
        if isinstance(k, list):  # если элемент = список распаковываем и пишем в конец
            for i in k:
                _list.append(i)
            _list.remove(k)

        if isinstance(k, int):  # если элемент = число. перезапишем в новый список
            new_int.append(k)
            _list.remove(k)

        if isinstance(k, str):  # если элемент = строка
            for i in k:  # проверим поэлементно содержит ли числа
                if i.isdigit():  # если есть число - запишем в список с цифрами
                    char = int(i)
                    new_int.append(char)
                else:
                    new_str.append(i)  # если буква, то запишем в список с буквами
            _list.remove(k)

        if isinstance(k, dict):  # если элемент = словарь
            _list.remove(k)
            value_ = list(k.values()) + list(k.keys())  # формируем список из значений и ключей. пишем  в конец
            _list.append(value_)

        if isinstance(k, tuple):  # если элемент = кортеж
            _list.remove(k)
            k = list(k)  # преобразуем в список и запишем в конец списка
            _list.append(k)

        if isinstance(k, set):  # если элемент = множество
            _list.remove(k)
            k = list(k)  # преобразуем в список и запишем в конец списка
            _list.append(k)

    for i in new_int:  # находим сумму всех чисел(записаны в список)
        sum_int += i

    result = sum_int + len(new_str)  # сумма чисел и длин строк
    return result  # результат сумма


result = calculate_structure_sum(data_structure)  # вызываем функцию для списка
print(result)  # выводим результат
