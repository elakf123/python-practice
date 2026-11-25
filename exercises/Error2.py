while True:
    try:
        a = int(input("Введите число: "))
        print(a*a)
        break
    except ValueError:
        print("Не число!")
