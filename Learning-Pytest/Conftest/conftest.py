import pytest

@pytest.fixture
def login_username():
    return "admin"

@pytest.fixture
def login_password():
    return "123456"