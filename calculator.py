operation = input("Какой знак у операции которую вы хотите выполнить? ")
x = int(input("Первое число: "))
y = int(input("Второе число: "))
if (operation == "+"):
    print(x+y)
elif (operation == "-"):
    print(x-y)
elif (operation == "*"):
    print(x*y)
elif (operation == "/" and y != 0):
    print(x/y)
elif (operation == "/" and y == 0):
    print("Деление на 0")
else: print("Ошибка операции!")
