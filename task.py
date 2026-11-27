class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        if self.done:
            return f"[x] {self.title}"
        else: return f"[ ] {self.title}"

if __name__ == "__main__":
    task1 = Task("Купить хлеб")
    task2 = Task("Понять классы")
    task1.mark_done()
    print(task1)
    print(task2)
