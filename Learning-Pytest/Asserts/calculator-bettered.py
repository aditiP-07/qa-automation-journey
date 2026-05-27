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

def test_calc():
    assert calc(4, 2, "+") == 6
    assert calc(7, 2, "-") == 5
    assert calc(0, 20, "*") != 20
    assert calc(0, 20, "*") == 0
    assert calc(0, 0, "/") == "Undefined"
    assert calc(0, 4, "/") == 0
    assert calc(4, 0, "/") == "Cannot be divided by 0!"
    assert calc(18, 2, "/") == 9
    assert calc(5, 5, "%") == 9