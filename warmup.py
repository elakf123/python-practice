def count_vowels(text):
    counter = 0
    for i in text.lower():
        if i == "а" or i == "е" or i == "ё" or i == "и" or i == "о" or i == "у" or i == "ы" or i == "э" or i == "ю" or i == "я":
            counter += 1
    return counter

def main():
    word = input("Введите слово чтобы узнать кол-во гласных: ")
    print(count_vowels(word))

    
if __name__ == "__main__":
    main()
