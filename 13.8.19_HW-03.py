price = 0

while True:
    try:
        number_of_tickets = int(input('Количество билетов:'))
        if type(number_of_tickets) == int:
            break
    except ValueError:
        print('Введите целое число!!!')

for i in range(number_of_tickets):
    i += 1
    while True:
        try:
            age = int(input(f'Возраст для билета №{i}:'))
            if age < 18:
                print('Билет бесплатный')
            elif 18 <= age < 25:
                price += 990
                print('Стоимость билета 990 руб.')
            else:
                price += 1390
                print('Стоимость билета 1390 руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Введите целое число!!!')
if number_of_tickets > 3:
    price *= 0.9
    print(f'К оплате {price} руб. с учётом скидки')
else:
    print(f'К оплате {price} руб.')