result = 0
with open("numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
        result += int(line)
print(result)
