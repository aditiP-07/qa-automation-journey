def add(n1, n2):
    return n1+n2
def test_add():
    assert add(6, 2) != 7
    assert add(6, 2) == 8

def subtract(n1, n2):
    return n1-n2
def test_subtract():
    assert subtract(6, 2) == 4

def multiply(n1, n2):
    return n1*n2
def test_multiply():
    assert multiply(6, 2) == 12

def divide(n1, n2):
    return n1 / n2
def test_divide():
    assert divide(6, 2) == 3
