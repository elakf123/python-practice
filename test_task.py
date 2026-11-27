from task import Task

def test_new_task_is_not_done():
    task = Task("Купить хлеб")
    assert task.done == False

def test_mark_done():
    task = Task("Купить хлеб")
    task.mark_done()
    assert task.done == True

def test_str_not_done():
    task = Task("Купить хлеб")
    assert str(task) ==  "[ ] Купить хлеб"

def test_str_done():
    task = Task("Купить хлеб")
    task.mark_done()
    assert str(task) == "[x] Купить хлеб"
