import random


lotto_numbers = list(range(1, 50))
rnd_numbers = []


for i in range(6):
    random.shuffle(lotto_numbers)
    x = lotto_numbers.pop()
    rnd_numbers.append(x)

# print(rnd_numbers)





def comparison(user_numbers):
    # user_numbers = list(user_number1, user_number2, user_number3, user_number4, user_number5, user_number6)
    print('Die Ziehung ergab die Zahlen: ')
    print(rnd_numbers)
    for i in rnd_numbers:
        if i == int(user_numbers[0]):
            print("Du hast die erste Zahl richtig")
        if i == int(user_numbers[1]):
            print("Du hast die zweite Zahl richtig")
        if i == int(user_numbers[2]):
            print("Du hast die dritte Zahl richtig")
        if i == int(user_numbers[3]):
            print("Du hast die vierte Zahl richtig")
        if i == int(user_numbers[4]):
            print("Du hast die fünfte Zahl richtig")
        if i == int(user_numbers[5]):
            print("Du hast die sechste Zahl richtig")
        else:
            print('Kein Treffer')

    return
