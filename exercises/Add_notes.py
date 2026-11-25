with open("notes.txt", "a", encoding="utf-8") as file:
    text = input("Введите текст: ")
    file.write(f"{text}\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
