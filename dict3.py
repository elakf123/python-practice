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
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
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
