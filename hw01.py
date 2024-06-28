calls = 0 #глобальная переменная


def count_calls():   #подсчитывающая вызовы остальных функций.
    global calls
    calls += 1


def string_info(string): #возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре
    count_calls()
    print([len(string), string.upper(), string.lower()])


def is_contains(string, list_to_search): #возвращает True, если строка находится в этом списке, False - если отсутствует
    count_calls()
    my_list = []
    for _ in list_to_search:        # Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
        my_list.append(_.upper())
    print(string.upper() in my_list)



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)