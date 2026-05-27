def get_weather():
    return "Sunny"

def suggest_activity():
    weather = get_weather()
    if weather == "Rainy":
        return "Stay inside"
    else:
        return "Go outdoors"

def fake_weather():
    return "Rainy"

def test_suggest_activity(monkeypatch):
    monkeypatch.setattr(
        "weather.get_weather", fake_weather
    )
    assert suggest_activity() == "Stay inside"