def test(n, *date, name = 'tanya', **etc):
    print(n)
    print(date)
    print(name)
    print(etc)
test(31, 5,4,2024, name = "Olya", tel = '2222', city = 'город', street = 'улица')


def factorial(num):
    if (num <= 1):
        return 1
    else:
        return (num * factorial(num-1))

print('Факториал равен: ', factorial(4))