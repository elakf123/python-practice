import random

number_of_try = 0
random_number = random.randint(1, 100)
number_guess = 0
while (number_guess != random_number):
    number_guess = int(input("Угадайте число:"))
    if number_guess > random_number:
        print("Загаданное число меньше")
    elif number_guess < random_number:
        print("Загаданное число больше")
    number_of_try += 1
print("Вы угадали загаданное число:", random_number)
print("Количество попыток:", number_of_try)
