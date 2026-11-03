while True:
    try:
        a = int(input("Введите число: "))
        break
    except ValueError:
        print("Не число!")
