import sys


def count_levels(lines):
    counts = {}
    for line in lines:
        try:
            level = line.split()[0]
        except IndexError:
            continue
        counts[level] = counts.get(level, 0) + 1
    return counts

def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Укажите имя файла: python3 log_stats.py app.log")
        sys.exit(1)
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        counts = count_levels(lines)
        print(counts)
    except FileNotFoundError:
        print("Такого файла нет")
        sys.exit(1) 


if __name__ == "__main__":
    main()
