import json


def add_task(tasks, title):
    task = {"title": title, "done": False}
    tasks.append(task)

def show_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        if task["done"]:
            print(f'{i}. [x] {task["title"]}')
        else: print(f'{i}. [ ] {task["title"]}')


def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
        
    
def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False)



def main():
    tasks = load_tasks()
    while True:
        print("""1 - добавить
2 - показать
3 - отметить выполненной
4 - выйти""")
        number = input()
        if number == "1":
            name = input("Название задачи: ")
            add_task(tasks, name)
            save_tasks(tasks)
        elif number == "2":
            show_tasks(tasks)
        elif number == "3":
            show_tasks(tasks)
            try:
                nummber_done = int(input("Номер выполненной задачи: "))
                if 1 <= nummber_done <= len(tasks):
                    tasks[nummber_done-1]["done"] = not tasks[nummber_done-1]["done"]
                    save_tasks(tasks)
                else: print("Нет такой задачи")
            except ValueError:
                print("Нужно ввести число")
        elif number == "4":
            break
        else: print("Такого пункта нет")

if __name__ == "__main__":
    main()

