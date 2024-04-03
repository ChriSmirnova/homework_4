money = input('Обери валюту : EUR , USD , UAH?')
amount = int(input('Введи кількість.'))
if money == 'EUR':
    dollar = amount * 1.0768
    grivna = amount * 42.2576
    print(f'Конвертація в USD = {dollar}, UAH = {grivna}')
elif money == 'USD':
    grivna = amount * 39.2442
    euro = amount * 0.9287
    print(f'Конвертація в EUR = {euro}, UAH = {grivna}')
else:
    euro = amount * 0.0237
    dollar = amount * 0.0255
    print(f'Конвертація в EUR = {euro}, USD = {dollar}')
