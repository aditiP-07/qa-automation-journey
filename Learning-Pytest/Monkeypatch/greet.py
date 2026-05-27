'''
 Time-based function — e.g. a greet() that returns "Good morning" / "Good afternoon" / "Good evening" based on datetime.now().hour. Test by monkeypatching the hour to 9, 14,20.
'''

from datetime import datetime

def finding_time():
    hour = datetime.now().hour
    return hour 

def greetings():
    timestamp = finding_time()
    if 6 <= timestamp < 12:
        return "Good Morning"
    elif 12 <= timestamp < 17:
        return "Good Afternoon"
    elif 17 <= timestamp < 21:
        return "Good Evening"
    elif 21 <= timestamp <= 24:
        return "Good Night"
    else:
        return "Please give correct timestamp. Imma cry if you break it."

def fake_morning():
    return 9

def fake_afternoon():
    return 14

def fake_night():
    return 21

def test_morning(monkeypatch):
    monkeypatch.setattr(
        "greet.finding_time", fake_morning,
    )
    assert greetings() == "Good Morning"

def test_afternoon(monkeypatch):
    monkeypatch.setattr(
        "greet.finding_time", fake_afternoon,
    )
    assert greetings() == "Good Afternoon"

def test_night(monkeypatch):
    monkeypatch.setattr(
        "greet.finding_time", fake_night,
    )
    assert greetings() == "Good Night"