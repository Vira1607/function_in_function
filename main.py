print('Функция в функции')

# Основная ветка программы, не считая заголовков функций, состоит из одной строки кода.
#
# Это вызов функции test().
# В ней запрашивается на ввод целое число.
# Если оно положительное, то вызывается функция positive(),
# тело которой содержит команду вывода на экран слова "Положительное".
#
# Если число отрицательное, то вызывается функция negative(),
# ее тело содержит выражение вывода на экран слова "Отрицательное".


def test():
    def positive():
        print('Положительное')

    def negative():
        print('Отрицательное')

    number = int(input('Введите число: '))

    if number > 0:
        positive()
    else:
        negative()


test()
