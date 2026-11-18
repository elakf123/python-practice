import sqlite3


def add_task(conn, title):
    conn.execute("INSERT INTO tasks (title, done) VALUES (?, 0)", (title,))
    conn.commit()

def show_tasks(conn):
    for row in conn.execute("SELECT * FROM tasks"):
        if row[2] == 1:
            print(f' {row[0]}. [x] {row[1]}')
        elif row[2] == 0:
            print(f' {row[0]}. [ ] {row[1]}')

def switch_task(conn):
    try:
        task_id = int(input("Число задачи: "))
        conn.execute("UPDATE tasks SET done = 1 - done WHERE id = ?", (task_id,))
        conn.commit()
    except ValueError:
        print("Нужно ввести число")

def delete_task(conn):
    try:
        task_id = int(input("Число задачи: "))
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
    except ValueError:
        print("Нужно ввести число")

        

def main():
    conn = sqlite3.connect("tasks.db")
    conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, done INTEGER)")
    while True:
        print("""1 - добавить
2 - показать
3 - Изменить статус
4 - удалить задачу
5 - выйти""")
        number = input()
        if number == "1":
            name = input("Название задачи: ")
            add_task(conn, name)
        elif number == "2":
            show_tasks(conn)
        elif number == "3":
            show_tasks(conn)
            switch_task(conn)
        elif number == "4":
            show_tasks(conn)
            delete_task(conn)
        elif number == "5":
            break
        else: print("Такого пункта нет")
    conn.close()

if __name__ == '__main__':
    main()
