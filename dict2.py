counts = {}
word = input("Введите слово: ")
for letter in word:
    counts[letter.lower()] = counts.get(letter.lower(), 0) + 1

for key, value in counts.items():
    print(key, value)
