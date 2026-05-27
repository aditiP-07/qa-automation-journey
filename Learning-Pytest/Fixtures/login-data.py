import pytest

@pytest.fixture
def login_username():
    return "admin"

@pytest.fixture
def login_password():
    return "123456"

def test_cred(login_username, login_password):
    assert login_username == "admin"
    assert login_password == "123456"

def test_cred_len(login_password):
    assert len(login_password) >= 5
    