import os 

def get_environment():
    return os.getenv("ENV")
def show_message():
    env = get_environment()
    if env == "production":
        return "OK"
    else:
        return "Not OK"

def test_prod_env(monkeypatch):
    monkeypatch.setenv("ENV", "production")
    assert show_message() == "OK"