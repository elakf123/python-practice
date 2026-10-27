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
    if sign == "+":
        print(add(a, b))
    elif sign == "-":
        print(subtract(a, b))
    elif sign == "*":
        print(multiply(a, b))
    elif sign == "/":
        result = divide(a, b)
        if result is None:
            print("Деление на ноль")
        else: print(result)
    else: print("Неизвестный знак")
    
if __name__ == "__main__":
    main()  
