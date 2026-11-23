from calculator import add, divide, subtract, multiply

def test_add():
    assert add(2, 3) == 5

def test_divide_by_zero():
    assert divide(5, 0) is None

def test_subtract():
    assert subtract(3, 2) == 1

def test_multiply():
    assert multiply(2, 2) == 4

def test_divide():
    assert divide(9, 3) == 3
