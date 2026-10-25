operation = input("Какой знак у операции которую вы хотите выполнить? ")
x = float(input("Первое число: "))
y = float(input("Второе число: "))
if (operation == "+"):
    print(x+y)
elif (operation == "-"):
    print(x-y)
elif (operation == "*"):
    print(x*y)
elif (operation == "/"):
    if (y != 0):
        print(x/y)
    else: print("Деление на 0")
else: print("Ошибка операции!")
