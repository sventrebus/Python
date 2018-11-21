from generator import *


alpha_numbers = {
    1: 'Erste',
    2: 'Zweite',
    3: 'Dritte',
    4: 'Vierte',
    5: 'Fünfte',
    6: 'Sechste'
}


def init():

    loop_count = 0
    user_numbers = []
    while loop_count < 6:
        loop_count += 1

        user_numbers.append(input(alpha_numbers.get(loop_count) + ' Zahl eigeben: [1-49] ' + '\n'))

    seperator = ', '
    print('Deine Zahlen sind ' + seperator.join(user_numbers) + '\n')
    print(comparison(user_numbers))










if __name__ == '__main__':
    init()
