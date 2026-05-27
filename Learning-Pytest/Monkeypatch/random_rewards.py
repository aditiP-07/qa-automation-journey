import random

def lucky_num():
    return random.random()

def rewards():
    reward = lucky_num()
    if reward == 7:
        return "Woohoo, you won!"
    else:
        return "Nope, child."

def fake_lucky_num():
    return 7

def test_lucky_num(monkeypatch):
    monkeypatch.setattr(
        "random_rewards.lucky_num", fake_lucky_num
    )
    assert rewards() == "Woohoo, you won!"