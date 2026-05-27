import pytest

@pytest.mark.parametrize("n1, n2, op, expected", [
    (2, 3, "+", 5),
    (10, 2, "/", 5),
    (4, 3, "-", 1),
    (8, 4, "**", 32)
])

def test_calc(n1, n2, op, expected):
    assert calc(n1, n2, op) == expected


def calc(n1, n2, operator):
    if operator == "+":
        return n1 + n2
    elif operator == "-":
        return n1 - n2
    elif operator == "*":
        return n1 * n2
    elif operator == "/":
        if n1 == 0 and n2 == 0:
            return "Undefined"
        elif n2 == 0:
            return "Cannot be divided by 0!"
        else:
            return n1 / n2
    else:
        return "Current calculator doesn't cover this operator!"