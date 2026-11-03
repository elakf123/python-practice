def read_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Не число!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    else: return a / b

def main():
    a = read_number("Введите первое число: ")
    b = read_number("Введите второе число: ")
    sign = input("Знак операции: ")
    signs = {"+": add, "-": subtract, "*": multiply, "/": divide}
    if sign in signs:
        result = signs[sign](a, b)
        if result == None:
            print("Деление на 0")
        else: print(result)
    else: print("Неизвестный знак")

        
if __name__ == "__main__":
    main()
