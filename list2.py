numbers = []
for i in range (1, 6):
    number = int(input(f"Введите число {i}: "))
    numbers.append(number)
max_n = numbers[0]
min_n = numbers[0]
mean_value = 0
for x in numbers:
    max_n = max(max_n, x)
    min_n = min(min_n, x)
    mean_value += x
mean_value /= len(numbers)
print(max_n, min_n, mean_value)
