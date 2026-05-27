import pytest

@pytest.mark.parametrize("n, expected", [
    (4, True), 
    (3, False), 
    (7, False), 
    (1200, True)
])

def test_even_num(n, expected):
    assert even_num(n) == expected

def even_num(n):
    if n%2 == 0:
        return True
    else:
        return False