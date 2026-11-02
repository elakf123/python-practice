with open("numbers.txt", "w", encoding="utf-8") as file:
    for i in range(1, 11):
        file.write(str(i))
        file.write("\n")
