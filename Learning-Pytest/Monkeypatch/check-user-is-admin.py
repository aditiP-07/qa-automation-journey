def get_role():
    return "user"

def access_panel():
    role = get_role()
    if role == "admin":
        return "Access granted!"
    else:
        return "Access denied!"

def fake_role():
    return "admin"

#monkeypatch in pytest is a built-in fixture used to temporarily change or replace things during a test.
def test_access_panel(monkeypatch):
    monkeypatch.setattr(
        "check-user-is-admin.get_role", fake_role #module_name.function_name -> module name as in whatever you are naming your file
    )
    assert access_panel() == "Access granted!"